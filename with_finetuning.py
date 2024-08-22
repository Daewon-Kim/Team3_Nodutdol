# finetuning 사용하는 코드

%pip install transformers

%pip install torch

from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
from io import BytesIO
import torch
import requests
from openai import AzureOpenAI
from config_azure import (
    AZURE_OPENAI_API_VERSION,
    FT_AZURE_OPENAI_ENDPOINT,
    FT_AZURE_OPENAI_KEY
)

# OpenAI 클라이언트 설정
client = AzureOpenAI(
    azure_endpoint=FT_AZURE_OPENAI_ENDPOINT,
    api_key=FT_AZURE_OPENAI_KEY,  
    api_version=AZURE_OPENAI_API_VERSION
)


# 모델과 전처리기, 토크나이저 불러오기
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

# 모델을 GPU에서 실행할 수 있는지 확인
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


# 1. 이미지 설명 생성 함수 정의
def generate_image_description(image_url):
    # URL에서 이미지 다운로드
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)
    
    # 모델 추론 및 결과 생성
    output_ids = model.generate(pixel_values, max_length=16, num_beams=4)
    description = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    return description


# 2. Azure OpenAI를 통해 설명에서 어려운 한국말을 북한말로 변환하는 응답 생성
def transform_description_to_north_korean(description):
    response = client.chat.completions.create(
        model='gpt-4o-mini-2024-07-18-northescape',  # Fine-tuned 모델명
        max_tokens=256,
        temperature=1.0,
        messages=[
            {"role": "system", "content": "이 모델은 남한의 어려운 한국말 단어를 남한어(북한어)로 변환해준다."},
            {"role": "user", "content": description}  # 이미지 설명을 입력으로 전달
        ]
    )
    return response.choices[0].message.content


# 3. 이미지 URL 정의
image_url = "https://pimg.mk.co.kr/news/cms/202301/17/news-p.v1.20230117.05097fae606c4be6bbe4e0d8ebc89f43_P1.jpg"

# 4. 이미지 설명 생성
description = generate_image_description(image_url)

# 5. 설명을 변환하여 북한말로 출력
transformed_description = transform_description_to_north_korean(description)
print(transformed_description)

# 6. 결과 출력
print(transformed_description)