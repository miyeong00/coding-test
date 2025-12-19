def power(n, m):
    if m == 0:
        return 1
    
    half = power(n, m // 2)
    
    if m % 2 == 0:
        return half * half
    else:
        return half * half * n

for _ in range(10):
    tc = int(input())
    N, M = map(int, input().split())
    
    answer = power(N, M)
    
    print(f'#{tc} {answer}')