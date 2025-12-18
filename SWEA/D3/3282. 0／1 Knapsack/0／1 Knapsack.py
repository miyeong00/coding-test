T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N, K = map(int, input().split()) # N : 물건의 개수, K : 가방의 부피
    dp = [0] * (K + 1) # 인덱스가 곧 가방의 부피

    for _ in range(N):
        volume, value = map(int, input().split())

        for j in range(K, volume - 1, -1):
            dp[j] = max(dp[j], dp[j - volume] + value)

    print(f'#{test_case} {dp[K]}')