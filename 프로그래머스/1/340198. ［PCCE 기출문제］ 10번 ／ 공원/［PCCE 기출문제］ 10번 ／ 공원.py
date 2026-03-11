# 다양한 크기의 정사각형 모양 돗자리
# 지민이가 깔 수 있는 가장 큰 돗자리가 어떤 건지 확인하고자 함.
# mats : 지민이가 가진 돗자리들의 한 변의 길이들이 담긴 정수 리스트
# park : 현재 공원의 자리 배치도를 의미하는 2차원 문자열 리스트
# 지민이가 깔 수 있는 가장 큰 돗자리의 한 변 길이 반환
# park[i][j]의 원소는 문자열
# park[i][j]에 돗자리를 깐 사람이 없다면 -1

def solution(mats, park):
    answer = 0
    
    mats.sort(reverse=True)
    
    for mat in mats:
        for i in range(len(park) - mat + 1):
            for j in range(len(park[0]) - mat + 1):
                fail = False
                for x in range(i, i + mat):
                    for y in range(j, j + mat):
                        if park[x][y] != "-1":
                            fail = True
                            break
                    if fail:
                        break
                        
                if not fail:
                    return mat
    
    return -1