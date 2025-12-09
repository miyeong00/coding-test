def solution(sizes):
    for i in range(len(sizes)):
        first = sizes[i][0]
        if sizes[i][1] > sizes[i][0]:
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = first
            
    size_width = 0 # 가로 : 인덱스 0
    size_length = 0 # 세로 : 인덱스 1
    for j in range(len(sizes)):
        if sizes[j][0] > size_width:
            size_width = sizes[j][0]
        if sizes[j][1] > size_length:
            size_length = sizes[j][1]
            
    return size_width * size_length