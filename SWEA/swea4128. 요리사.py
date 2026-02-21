# N개의 식재료
# 식재료들을 각각 N/2개씩 나누어 두 개의 요리를 하려고 함. (N은 짝수)
# 비슷한 맛의 음식을 만들기 위해서는 A음식과 B음식의 맛의 차이가 최소가 되도록 재료를 배분해야 함.
# 식재료 i는 식재료 j와 같이 요리하게 되면 궁합이 잘 맞아 시너지 Sij가 발생
# 각 음식의 맛은 음식을 구성하는 식재료들로부터 발생하는 시너지 Sij들의 합
# 식재료 i를 식재료 j와 같이 요리하게 되면 발생하는 시너지 Sij의 정보가 주어짐.
# 가지고 있는 식재료를 이용해 A음식과 B음식을 만들 때, 두 음식 간의 맛의 차이가 최소가 되는 경우의 최솟값 출력

def dfs(start, depth):
    global answer
    
    if depth == N // 2:
        sumA = 0
        sumB = 0

        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    sumA += ingredients[i][j] + ingredients[j][i]
                elif (not visited[i]) and (not visited[j]):
                    sumB += ingredients[i][j] + ingredients[j][i]

        answer = min(answer, abs(sumA - sumB))
        return
    
    for i in range(start, N):
        visited[i] = True
        dfs(i + 1, depth + 1)
        visited[i] = False

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N = int(input()) # 식재료의 수
    ingredients = [list(map(int, input().split())) for _ in range(N)] # 시너지 Sij

    visited = [False] * N
    answer = 10**9

    dfs(0, 0)

    print(f'#{test_case} {answer}')