# 2001. 파리 퇴치
T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N : 파리 배열, M : 파리채 크기
    flies = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0

    for i in range(N):
        for j in range(N):
            fly = 0
            for x in range(M):
                for y in range(M):
                    ni = i + x
                    nj = j + y
                    if 0 <= ni < N and 0 <= nj < N:
                        fly += flies[ni][nj]
            if max_fly < fly:
                max_fly = fly

    print(f'#{test_case} {max_fly}')