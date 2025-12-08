def solution(number):
    answer = 0
    n = len(number)
    
    def dfs(start, count, cur_sum):
        nonlocal answer
        
        # 종료조건 : 3명 다 뽑았을 때
        if count == 3:
            if cur_sum == 0:
                answer += 1
            return
        
        # 탐색
        for i in range(start, n):
            # 다음 재귀 호출
            dfs(i+1, count+1, cur_sum+number[i])
    
    dfs(0,0,0)
    
    return answer