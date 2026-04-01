# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴
# 예를 들어 n이 12345이면 [5, 4, 3, 2, 1] 리턴

def solution(n):
    answer = []

    for s in str(n):
        answer.append(int(s))

    answer.reverse()

    return answer