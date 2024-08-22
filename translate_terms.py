def translate_terms(text):
    """설명에서 남한어를 북한어로 변환합니다."""
    word_map = {
        "남한어_단어": "북한어_단어",  # 남한어 단어와 북한어 단어를 여기에 추가
        # 예: "휴대폰": "손전화기"
    }
    for south_word, north_word in word_map.items():
        if south_word in text:
            text = text.replace(south_word, f"{south_word}({north_word})")
    return text