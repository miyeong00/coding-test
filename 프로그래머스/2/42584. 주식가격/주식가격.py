def solution(prices):
    answer = [] # 가격이 떨어지지 않은 기간을 담는 리스트
    
    for i in range(len(prices) - 1):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                if j == (len(prices) - 1):
                    answer.append(j - i)
                    break
                else:
                    continue
            else:
                answer.append(j - i)
                break
                
    answer.append(0)
    
    return answer