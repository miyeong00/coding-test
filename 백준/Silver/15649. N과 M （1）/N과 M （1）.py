# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

N, M = map(int, input().split()) # N : 1부터 N까지 자연수, M : 수열의 길이

visited = [False] * (N + 1)
answer = []

def dfs():
    if len(answer) == M:
        print(*answer)
        return
    
    for i in range(1, N + 1):

        if not visited[i]:
            visited[i] = True
            answer.append(i)

            dfs()

            answer.pop()
            visited[i] = False

dfs()