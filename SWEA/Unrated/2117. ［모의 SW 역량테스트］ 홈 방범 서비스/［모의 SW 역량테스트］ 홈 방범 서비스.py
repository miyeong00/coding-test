# N x N 크기의 도시에 홈방범 서비스 제공 -> 마름모 모양의 영역에만 제공됨.
# 서비스 영역의 크기 K가 커질수록 운영 비용이 커짐.
# 운영 비용 = K * K + (K - 1) * (K - 1)
# 홈방범 서비스를 제공받는 집들은 각각 M의 비용을 지불할 수 있어 최대한 많은 집에 제공하려고 함.
# 손해를 보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾고,
# 그 때의 홈방범 서비스를 제공 받는 집들의 수 출력
# 집이 있는 위치는 1이고, 나머지는 0

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N : 도시의 크기, M : 하나의 집이 지불할 수 있는 비용
    cities = [list(map(int, input().split())) for _ in range(N)] # N x N 크기의 도시 정보

    answer = 0 # 홈방범 서비스를 제공 받는 집들의 수

    for sr in range(N):
        for sc in range(N):
            for K in range(1, 2*N):
                cost = K * K + (K - 1) * (K - 1) # 비용
                home = 0
                for r in range(N):
                    for c in range(N):
                        if abs(r - sr) + abs(c - sc) < K:
                            if cities[r][c] == 1:
                                home += 1
                if home * M >= cost:
                    answer = max(answer, home)


    print(f'#{test_case} {answer}')