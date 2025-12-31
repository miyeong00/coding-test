def solution(babbling):
    answer = 0 # 머쓱이의 조카가 발음할 수 있는 단어의 개수
    words = ["aya", "ye", "woo", "ma"] # 머쓱이의 조카가 발음할 수 있는 단어들
    
    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue
            
        for word in words:
            b = b.replace(word, " ")
            
        if len(b.strip()) == 0:
            answer += 1
            
    return answer