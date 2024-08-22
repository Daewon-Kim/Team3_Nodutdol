from enriched_description import get_enriched_description

def main():
    kakao_links = {"5_kakao": "http://example.com/image.png"}  # 실제 카카오 링크로 변경
    is_continue = True
    kakao_5_link = kakao_links["5_kakao"]
    while is_continue:
        is_continue = False
        num = input('안녕하세요! 노둣돌입니다. 이미지는 1, 본문은 2, 끝은 3을 뽑아주세요: ')
        if num == '1':
            image_URL = kakao_5_link
            print("사진에 대한 설명:", get_enriched_description(image_URL)) 
        elif num == '2':
            text_query = input('본문을 쓰세요: ')
            print("텍스트 질문에 대한 답변:", get_enriched_description(text_query))
        elif num == '3':
            is_continue = False
        else:
            print('바르지 않은 쓰기입니다. 또 쓰세요.')
            is_continue = True
        if is_continue == False:
            print("종료합니다")

if __name__ == "__main__":
    main()
