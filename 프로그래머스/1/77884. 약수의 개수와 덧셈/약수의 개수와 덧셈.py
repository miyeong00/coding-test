def solution(left, right):
    answer = 0 # 결과값
    n = left # left부터 시작
    while n <= right: # right보다 작거나 같을 때까지 반복
        divisor_num = 0 # 약수의 개수
        for i in range(1, n+1): # 1부터 n까지 다 나눠보면서 약수 찾기
            if n % i == 0:
                divisor_num += 1
        
        if divisor_num % 2 == 0: # 약수의 개수가 짝수인 경우
            answer += n # 결과값에 더하기
        else: # 홀수인 경우
            answer -= n # 빼기
        
        n += 1
        
    return answer
            
                
        
            