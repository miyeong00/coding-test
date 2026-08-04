# 지도의 한 변의 길이 : n
# 지도의 각 칸은 공백 또는 벽(#) 두 종류
# 전체 지도는 두 장의 지도를 겹쳐야 됨.
# 지도 1과 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽
# 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백 
# 암호화된 배열은 지도의 각 가로줄에서 벽 부분은 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열

def solution(n, arr1, arr2):
    arr1_code = []
    arr2_code = []
    
    for a1 in arr1:
        arr1_code.append(bin(a1)[2:].zfill(n))
        
    for a2 in arr2:
        arr2_code.append(bin(a2)[2:].zfill(n))
        
    answer = []
    for i in range(n):
        code = ''
        for j in range(n):
            if arr1_code[i][j] == '0' and arr2_code[i][j] == '0':
                code += ' '
            else:
                code += '#'
        answer.append(code)
    return answer