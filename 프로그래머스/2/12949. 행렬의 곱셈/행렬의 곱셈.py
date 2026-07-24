def solution(arr1, arr2):
    i = len(arr1) # arr1의 행의 개수
    j = len(arr1[0]) # arr1의 열의 개수 = arr2의 행의 개수
    k = len(arr2[0]) # arr2의 열의 개수 
    
    answer = [[0] * k for _ in range(i)] # i행 k열의 배열 생성 = 정답
    
    for a in range(i):
        for b in range(j):
            for c in range(k):
                answer[a][c] += arr1[a][b] * arr2[b][c]
    
    return answer