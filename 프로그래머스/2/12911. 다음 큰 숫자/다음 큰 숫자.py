# n의 다음 큰 숫자
# 1. n보다 큰 자연수
# 2. n을 2진수로 변환했을 때 1의 갯수가 같음.
# 3. 조건 1, 2를 만족하는 수 중 가장 작은 수

def solution(n):
    
    one_count = bin(n).count('1')
    n += 1
    
    while one_count != bin(n).count('1'):
        n += 1
    
    return n