# N개의 숫자가 적혀 있는 게임 판
# +, -, x, /의 연산자 카드를 숫자 사이에 끼워 넣어 다양한 결과 값을 구해보기
# 왼쪽에서 오른쪽으로 차례대로 계산
# 주어진 연산자 카드를 사용하여 수식을 계산했을 때 그 결과가 최대가 되는 수식과 최소가 되는 수식의 차이 출력

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N = int(input()) # 게임 판에 적힌 숫자 개수
    operators = list(map(int, input().split())) # +, -, *, / 연산자 개수
    numbers = list(map(int, input().split())) # 게임 판에 적힌 숫자들

    answer_max = -100000000 # 나올 수 있는 결과의 최댓값
    answer_min = 100000000 # 나올 수 있는 결과의 최솟값

    # idx : 현재 계산할 값의 인덱스, cur : 현재 계산된 값
    def dfs(idx, cur):
        # 종료 조건
        # 게임 판에 적힌 숫자들을 다 계산했을 때
        if idx == N:
            global answer_max, answer_min
            answer_max = max(answer_max, cur)
            answer_min = min(answer_min, cur)
            return
        
        # + 계산
        if operators[0] > 0:
            operators[0] -= 1
            dfs(idx + 1, cur + numbers[idx])
            operators[0] += 1

        # - 계산
        if operators[1] > 0:
            operators[1] -= 1
            dfs(idx + 1, cur - numbers[idx])
            operators[1] += 1

        # x 계산
        if operators[2] > 0:
            operators[2] -= 1
            dfs(idx + 1, cur * numbers[idx])
            operators[2] += 1

        # / 계산
        if operators[3] > 0:
            operators[3] -= 1
            if cur < 0:
                dfs(idx + 1, -(-cur // numbers[idx]))
            else:
                dfs(idx + 1, cur // numbers[idx])
            operators[3] += 1

    dfs(1, numbers[0])

    print(f'#{test_case} {answer_max - answer_min}')

        

    