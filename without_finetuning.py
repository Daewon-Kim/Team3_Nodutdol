# finetuning 사용하지 않는 코드
# few-shot 프롬프팅 사용

# 1 패키지 설치

%pip install -U openai

# 2. 기본 패키지 설정 & AzureOpenAI 환경설정

from openai import AzureOpenAI

from config_azure import (
    AZURE_OPENAI_API_VERSION,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_KEY
)

client = AzureOpenAI(
  azure_endpoint = AZURE_OPENAI_ENDPOINT,
  api_key = AZURE_OPENAI_KEY,  
  api_version = AZURE_OPENAI_API_VERSION
)

# 3. 남한어-북한어 데이터셋
word_map = {
    '충분하다' : '그쯔하다',
    '값싸다' : '눅다',
    '거르다' : '번지다',
    '가르쳐주다' : '배워주다',
    '가지' : '아지',
    '그룹' : '그루빠',
    '외치다' : '웨치다',
    '위' : '우',
    '가루비누': '분말비누',
    '간 비대': '간붓기',
    '갈빗대': '갈비대',
    '감응 기뢰': '비접촉기뢰',
    '강우량': '비량',
    '개떡수제비': '개떡제비',
    '개비': '가치',
    '개양귀비': '애기아편꽃',
    '겉보기평형': '겉보기비김',
    '격납고': '비행기고',
    '경사': '비탈',
    '고정 비용': '불변비',
    '공기비': '공기곁수',
    '공비 증류': '껴끓음증류',
    '공비 혼합물': '껴끓음혼합물',
    '공중제비': '건공중잡이',
    '과린': '열매비늘',
    '구비 문학': '민간문학',
    '구비 문학': '인민창작',
    '권운': '비단구름',
    '권층운': '비단층구름',
    '규산질 비료': '규소비료',
    '금비녀': '전침',
    '기비': '육비',
    '나비경첩': '나비사개',
    '나비굴': '나비뼈굴',
    '낭비': '랑비',
    '낭비하다': '람비하다',
    '내분비물': '각성소',
    '노비': '로비',
    '노비일': '노비날',
    '녹비': '록비',
    '뇌성 마비': '소아뇌성마비',
    '누비처네': '누비포단',
    '늑연골': '갈비삭뼈',
    '능비': '릉비',
    '다다미': '누비돗자리',
    '다우 지대': '비많은지대',
    '담비': '누른돈',
    '대륙족제비': '북족제비',
    '동물질 비료': '동물성거름',
    '들이비치다': '들여비치다',
    '등비급수': '같은비합렬',
    '등비수열': '같은비수렬',
    '따개비': '따깨비',
    '로켓 비행기': '로케트비행기',
    '로프 설비': '바줄설비',
    '마그네슘 비료': '마그네시움비료',
    '멀리뛰기': '너비뛰기',
    '멧비둘기': '메비둘기',
    '무한궤도 차량': '무한궤도식주행설비',
    '물결나비': '물결뱀눈나비',
    '물수제비': '물찰찰이',
    '물시멘트비': '물세멘트비',
    '미량 원소': '미량비료',
    '밑거름': '밑비료',
    '배빗대': '배비대',
    '비': '비틀자루',
    '비결정질': '비결정체',
    '비계지다': '비게지다',
    '비교': '비김',
    '비교 문법': '대조문법',
    '비너스': '비너스성좌',
    '비늘 갑옷': '쇠찰갑',
    '비닐 인쇄': '비닐주머니인쇄',
    '비다듬다': '비듬다',
    '비단뱀': '구렝이',
    '비단옷': '단의',
    '비대발괄하다': '비두발괄하다',
    '비듬': '머리비듬',
    '비디오테이프': '록화띠',
    '비례 대표제': '비례대의제',
    '비만 요법': '비반료법',
    '비모음': '코안모음',
    '비브라토': '떨기',
    '비산칼슘': '비산칼시움',
    '비스름하다': '비스듬하다',
    '비스크': '비스끼',
    '비아냥대다': '비양대다',
    '비연': '강뇌사',
    '비엽': '코주름',
    '비음': '비자음',
    '비음': '코안자음',
    '비지': '되두부',
    '비축미': '예비곡',
    '비타민 비 원 결핍증': '비타민비하나결핍증',
    '비행운': '비행구름',
    '빗물막이': '비물막이',
    '빗발': '비발',
    '빗살': '비살',
    '빗자루': '비자루',
    '성냥개비': '성냥가치',
    '소사': '비자루사격',
    '쇳내': '쇠비린내',
    '수비수': '방어수',
    '수온 약층': '물온도비약층',
    '수중 텔레비전': '물속텔레비죤',
    '시베리아 기단': '씨비리기단',
    '싸릿개비': '싸리개비',
    '아스팔트': '원유비뜸',
    '어슷비슷하다': '어등비등하다',
    '엇비슥하다': '엇비슴하다',
    '여관비': '려관비',
    '여비': '려비',
    '여존남비': '녀존남비',
    '연비': '련비',
    '운송비': '운수비',
    '유기 비소 화합물': '비소유기화합물',
    '유산근 비료': '류산근비료',
    '유아등': '나비등',
    '유의어': '뜻비슷한말',
    '육상 비행기': '륙상비행기',
    '의붓아비': '이붓아비',
    '이병비': '리병비'
}

# 4.사진 입력, 설명 출력, translate 함수 

def translate_terms(text):
    """설명에서 남한어를 북한어로 변환합니다."""
    for south_word, north_word in word_map.items():
        if south_word in text:
            text = text.replace(south_word, f"{south_word}({north_word})")
    return text

def generate_description(image_url):
    """사진 URL을 기반으로 설명을 생성합니다."""
    prompt = f"다음 사진의 내용을 자세히 설명해주세요:\n\n사진 URL: {image_url}\n\n설명:"

    response = client.completions.create(
        model="gpt-35-turbo-instruct",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        top_p=1.0,
        n=1,
        stream=False
    )

    description = response.choices[0].text.strip()
    return description

def get_enriched_description(image_url):
    """사진에 대한 설명을 생성하고, 설명 중 어려운 단어를 변환합니다."""
    description = generate_description(image_url)
    enriched_description = translate_terms(description)
    return enriched_description

# 5. 예제 사용

# 사진 URL 예시
image_url = 'https://i.namu.wiki/i/dy0SR0CdMrN0YATu41gIgg8IWZQQFmcD62_J2a9BJbM8Okmr2La3JqoKCsT-0Oa9lR9rrnNx1v0m5secUIMLLw.web'
result_description = get_enriched_description(image_url)
print("사진에 대한 설명:", result_description)