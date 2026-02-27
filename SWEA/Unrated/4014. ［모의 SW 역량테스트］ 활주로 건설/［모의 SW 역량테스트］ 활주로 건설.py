# N x N 크기의 절벽지대에 활주로를 건설하고자 함.
# 각 셀의 숫자는 그 지형의 높이
# 활주로는 높이가 동일한 구간에서 건설이 가능
# 높이가 다른 구간의 경우 활주로가 끊어지기 때문에 경사로 설치
# 경사로 : 길이 X, 높이 1
# 경사로는 높이 차이가 1이고 낮은 지형의 높이가 동일하게 경사로의 길이만큼 연속되는 곳에 설치할 수 있음.
# 경사로의 길이 X와 절벽지대의 높이 정보가 주어질 때, 활주로를 건설할 수 있는 경우의 수 계산

# 한 줄 검사하는 함수
def check(line):
    used = [False] * N # 경사로 설치 여부

    for i in range(N-1):
        if line[i] - line[i+1] == 0:
            continue
        elif line[i] - line[i+1] == 1: # 내리막
            start = line[i+1]
            for j in range(i+1, i+1+X):
                if j >= N or line[j] != start or used[j]:
                    return False
                used[j] = True
        elif line[i] - line[i+1] == -1: # 오르막
            start = line[i]
            for j in range(i, i-X, -1):
                if j < 0 or line[j] != start or used[j]:
                    return False
                used[j] = True
        else:
            return False
    return True

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N, X = map(int, input().split()) # N : 지도 한변의 크기, X : 경사로의 길이
    board = [list(map(int, input().split())) for _ in range(N)] # 지형 정보
    answer = 0 # 활주로를 건설할 수 있는 경우의 수

    # 가로 행 확인
    for i in range(N):
        if check(board[i]):
            answer += 1

    # 세로 열 확인
    for j in range(N):
        col = [board[i][j] for i in range(N)]
        if check(col):
            answer += 1

    print(f'#{test_case} {answer}')