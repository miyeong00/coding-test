def solution(n, m):
    # 최대공약수
    gcd = 0
    for i in range(1, n+1):
        if n % i == 0 and m % i == 0:
            gcd = i
            
    # 최소공배수
    lcm = gcd * (n // gcd) * (m // gcd)
    
    return [gcd, lcm]