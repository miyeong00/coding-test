def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        # 1. 각 숫자를 이진수 문자열로 변환 (따로따로!)
        row1 = bin(arr1[i])[2:]
        row2 = bin(arr2[i])[2:]
        
        # 2. 자릿수(n)에 맞춰서 앞에 0 채우기
        row1 = row1.zfill(n)
        row2 = row2.zfill(n)
        
        # 3. 한 글자씩 비교해서 지도 만들기
        decoded_line = ""
        for j in range(n):
            # "둘 중 하나라도 '1'(벽)이면 벽(#)이다"
            if row1[j] == '1' or row2[j] == '1':
                decoded_line += "#"
            else:
                decoded_line += " "
        
        answer.append(decoded_line)
        
    return answer