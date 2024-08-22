import openai

def generate_description(text_or_image_url):
    """텍스트 또는 사진 URL을 기반으로 설명을 생성합니다."""
    if text_or_image_url.startswith("http"):  # URL로 판단
        prompt = f"""
        다음 사진의 로고를 확인하고, 이 로고가 어떤 회사 또는 브랜드의 것인지, 그리고 그 회사나 브랜드가 제공하는 서비스나 제품에 대해 설명해 주세요.
        
        사진 URL: {text_or_image_url}
        
        설명:
        """
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                { 
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": text_or_image_url,
                            },
                        },
                    ],
                }
            ],
            max_tokens=300,
            temperature = 0,
        )
        description = response.choices[0].message.content.strip()
    else:  # 텍스트로 판단
        prompt = f"""
        {text_or_image_url}
        
        설명:
        """
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                { 
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt}
                    ],
                }
            ],
            max_tokens=300,
            temperature = 0,
        )
        description = response.choices[0].message.content.strip()
    
    return description
