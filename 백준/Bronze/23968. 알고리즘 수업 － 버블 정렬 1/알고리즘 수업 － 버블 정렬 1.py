N, K = map(int, input().split())
A = list(map(int, input().split()))

sort_cnt = 0
for i in range(N-1, 0, -1):
    for j in range(i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            sort_cnt += 1
            if sort_cnt == K:
                print(f'{A[j]} {A[j+1]}')
                exit()

if sort_cnt < K:
    print(-1)