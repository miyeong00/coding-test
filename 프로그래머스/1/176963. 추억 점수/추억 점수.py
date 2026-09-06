# 사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값이 해당 사진의 추억 점수가 됨.
# name : 사람의 이름을 담은 문자열 배열
# yearning : 각 사람별 그리움 점수를 담은 정수 배열
# photo : 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열
# 사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 출력

def solution(name, yearning, photo):
    answer = [] # 사진들의 추억 점수 배열
    score = {} # 사람 이름 : 그리움 점수
    
    for i in range(len(name)):
        score[name[i]] = yearning[i]
        
    for p in photo:
        s = 0 # 사진의 추억 점수
        for name in p:
            if name in score:
                s += score[name]
            
        answer.append(s)
            
    return answer
    