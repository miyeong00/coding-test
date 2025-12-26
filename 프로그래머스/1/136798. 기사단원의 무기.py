def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number + 1):
        count = 0
        
        # [핵심] num까지가 아니라, num의 제곱근까지만 반복!
        # int(num ** 0.5)는 제곱근의 정수 부분입니다.
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                # i가 약수라면
                count += 1
                
                # i의 짝꿍(num // i)도 약수인데, 
                # 만약 i * i == num (예: 3*3=9)라면 중복이므로 더하지 않음
                if (i * i) != num:
                    count += 1
        
        # 약수 개수(count)를 구하자마자 바로 limit 체크
        if count > limit:
            answer += power
        else:
            answer += count
            
    return answer