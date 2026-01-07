def solution(s):
    first_chr = ""
    same = 0 # 같은 문자열 나온 횟수
    diff = 0 # 다른 문자열 나온 횟수
    answer = 0 # 분해한 문자열 개수
    
    for chr in s:
        # 새로운 뭉텅이의 시작인 경우
        if same == 0 and diff == 0:
            first_chr = chr
            same += 1
            continue
        
        # 기준 글자와 비교
        if first_chr == chr:
            same += 1
        else:
            diff += 1
            
        # 같은 거랑 다른 거 횟수가 같아지는 순간
        if same == diff:
            answer += 1
            same = 0
            diff = 0
    
    # 반복문 끝났는데 아직 남아있으면 마지막 조각
    if same != 0:
        answer += 1
        
    return answer