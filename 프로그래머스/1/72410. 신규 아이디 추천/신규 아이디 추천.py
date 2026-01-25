def solution(new_id):
    # 1단계: 소문자 치환
    new_id = new_id.lower()
    
    # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    answer = ''
    for char in new_id:
        if char.isalnum() or char in ['-', '_', '.']:
            answer += char
            
    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    # strip()을 쓰면 앞뒤 마침표를 한 번에 싹 지울 수 있어요!
    answer = answer.strip('.')
    
    # 5단계: 빈 문자열이라면 "a" 대입
    if not answer:
        answer = 'a'
        
    # 6단계: 길이가 16자 이상이면 첫 15개만 남기고, 끝 마침표 제거
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')
        
    # 7단계: 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer