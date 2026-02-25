# N x N 크기의 정사각형 모양의 방에 사람들이 앉아 있음.
# P : 방 안의 사람들, S : 계단 입구
# 이동 완료 시간 : 모든 사람들이 계단을 내려가 아래 층으로 이동을 완료한 시간
# 계단 입구까지 이동 시간 = abs(PR - SR) + abs(PC - SC) / 현재 위치에서 계단 입구까지 이동하는 시간
# 계단을 내려가는 시간 : 계단 입구에 도착한 후부터 계단을 완전히 내려갈 때까지의 시간
# 계단 입구에 도착하면, 1분 후 아래칸으로 내려갈 수 있음.
# 계단 위에는 동시에 최대 3명까지만 올라가 있을 수 있음.
# 이미 계단을 3명이 내려가고 있는 경우, 그 중 한 명이 계단을 완전히 내려갈 때까지 계단 입구에서 대기해야 함.
# 계단마다 길이 K가 주어지며, 계단에 올라간 후 완전히 내려가는데 K분 걸림.
# 모든 사람들이 계단을 내려가 이동이 완료되는 시간이 최소가 되는 경우를 찾고, 그 때의 소요시간을 출력
# 계단은 반드시 2개
# 1 : 사람들, 2 이상 : 계단의 입구

# 이동 완료 시간 계산
# arrivals : 도착시간들, K : 계단길이
def simulate(arrivals, K):
    if not arrivals:
        return 0
    
    arrivals.sort()

    off = [] # 계단을 내려가는 사람들의 '끝나는 시간'들 (최대 3개)

    for a in arrivals:
        t = a + 1 # 도착 후 1분 뒤부터 계단 진입 가능

        if len(off) < 3:
            finish = t + K
            off.append(finish)
            off.sort()
        else:
            # 자리가 빌 때까지 기다려야 함 (가장 빨리 끝나는 시점)
            earliest = off.pop(0)
            start = max(t, earliest)
            finish = start + K
            off.append(finish)
            off.sort()

    return max(off) # 마지막 사람이 내려간 시간

# 사람들이 어느 계단으로 내려갈지 배정
def dfs(i):
    global answer

    if i == len(people):
        A, B = [], []
        for idx in range(len(people)):
            if choice[idx] == 0:
                A.append(stair0[idx])
            else:
                B.append(stair1[idx])

        t0 = simulate(A, k0)
        t1 = simulate(B, k1)
        answer = min(answer, max(t0, t1))
        return
    
    # i번 사람을 0번 계단으로
    choice[i] = 0
    dfs(i + 1)

    # i번 사람을 1번 계단으로
    choice[i] = 1
    dfs(i + 1)


T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    N = int(input()) # 방의 크기
    board = [list(map(int, input().split())) for _ in range(N)] # 지도의 정보

    answer = 10 ** 9 # 모든 사람들이 계단을 내려가 이동이 완료되는 최소 시간

    # 사람, 계단 좌표
    people = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                people.append([i, j])
            elif board[i][j] >= 2:
                stairs.append([i, j, board[i][j]])

    # 계단 도착시간(이동시간)
    stair0 = [0] * len(people)
    stair1 = [0] * len(people)

    sr0, sc0, k0 = stairs[0]
    sr1, sc1, k1 = stairs[1]

    for idx, (pr, pc) in enumerate(people):
        stair0[idx] = abs(pr - sr0) + abs(pc - sc0) # 0번 계단 도착시간(이동시간)
        stair1[idx] = abs(pr - sr1) + abs(pc - sc1) # 1번 계단 도착시간(이동시간)

    choice = [0] * len(people) # i번 사람이 어느 계단 선택했는지

    dfs(0)

    print(f'#{test_case} {answer}')