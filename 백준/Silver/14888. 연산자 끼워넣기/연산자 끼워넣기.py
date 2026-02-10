# N개의 수로 이루어진 수열
# 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자 : +, -, x, /
# 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 만듦.
# 주어진 수의 순서를 바꾸면 안 됨.
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행
# 음수로 양수를 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꿈.
# 만들 수 있는 식의 결과가 최대인 것과 최소인 것 구하기

N = int(input()) # 수열의 개수
arr = list(map(int, input().split())) # N개의 수열
operators = list(map(int, input().split())) # 연산자 +, -, x, /

answer_max = -1000000000 # 나올 수 있는 최댓값
answer_min = 1000000000 # 나올 수 있는 최솟값

# idx : 이제 계산할 값의 인덱스, cur : 현재 계산된 값
def dfs(idx, cur):
    # 종료 조건
    if idx == N:
        global answer_max, answer_min
        answer_max = max(answer_max, cur)
        answer_min = min(answer_min, cur)
        return

    if operators[0] > 0:
        operators[0] -= 1
        dfs(idx + 1, cur + arr[idx])
        operators[0] += 1

    if operators[1] > 0:
        operators[1] -= 1
        dfs(idx + 1, cur - arr[idx])
        operators[1] += 1

    if operators[2] > 0:
        operators[2] -= 1
        dfs(idx + 1, cur * arr[idx])
        operators[2] += 1

    if operators[3] > 0:
        operators[3] -= 1
        if cur < 0:
            dfs(idx + 1, -(-cur // arr[idx]))
        else:
            dfs(idx + 1, cur // arr[idx])
        operators[3] += 1

dfs(1, arr[0])
print(answer_max)
print(answer_min)

