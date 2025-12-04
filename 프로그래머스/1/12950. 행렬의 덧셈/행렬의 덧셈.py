def solution(arr1, arr2):
    row_len = len(arr1)
    col_len = len(arr1[0])
    
    answer = [[0] * col_len for _ in range(row_len)]
    
    for i in range(row_len):
        for j in range(col_len):
            answer[i][j] = arr1[i][j] + arr2[i][j]
            
    return answer