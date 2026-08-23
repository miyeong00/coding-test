# 영어 단어가 적힌 카드 뭉치 두 개
# 다음 규칙으로 원하는 순서의 단어 배열 만들기
# 원하는 카드 뭉치에서 카드를 순서대로 한 장씩 사용
# 한 번 사용한 카드는 다시 사용할 수 없음.
# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없음.
# 기존에 주어진 카드 뭉치의 단어 순서는 바꿀 수 없음.
# cards1, cards2 : 문자열로 이루어진 배열
# goal : 원하는 단어 배열
# cards1과 cards2에 적힌 단어들로 goal를 만들 수 있다면 "Yes"를, 만들 수 없다면 "No"를 출력

def solution(cards1, cards2, goal):
    i = 0
    j = 0
    
    for g in goal:
        if i < len(cards1) and g == cards1[i]:
            i += 1
        elif j < len(cards2) and g == cards2[j]:
            j += 1
        else:
            return "No"
    return "Yes"
            
    