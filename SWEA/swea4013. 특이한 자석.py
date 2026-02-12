# 4개의 자석이 놓여져 있었고, 각 자선은 8개의 날을 가지고 있음.
# 자석의 각 날마다 N극 또는 S극의 자성을 가지고 있음.
# 하나의 자석이 1칸 회전될 때, 붙어 있는 자석은 서로 붙어 있는 날의 자성과 다를 경우에만 인력에 의해 반대 방향으로 1칸 회전
# 1번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 1점을 획득
# 2번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 2점을 획득
# 3번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 4점을 획득
# 4번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 8점을 획득
# 4개 자석의 자성 정보와 자석을 1칸씩 K번 회전시키려고 할 때,
# K번 자석을 회전시킨 후 획득하는 점수의 총합을 출력

# 자석을 회전시키는 방향은 시계방향이 1, 반시계 방향이 -1
# 날의 자성은 N극이 0, S극이 1
# 각 자석의 자성정보는 빨간색 화살표 위치의 날부터 시계방향 순서대로 주어짐.

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    K = int(input()) # 자석을 회전시키는 횟수
    magnetic = [list(map(int, input().split())) for _ in range(4)] # 1번부터 4번 자석까지 각각 8개 날의 자성정보
    rotate = [list(map(int, input().split())) for _ in range(K)] # K번의 회전 정보 : 회전시키려는 자석의 번호, 회전방향

    # k : 무슨 자석 번호 회전시키는지, d : 어느 방향으로 회전
    for k, d in rotate:
        k -= 1
        dir = [0, 0, 0, 0] # 이번 턴에 각 자석이 어떤 방향으로 회전할지
        dir[k] = d

        # 왼쪽 전파
        for i in range(k-1, -1, -1):
            # 현재 자석번호랑 한 칸 앞의 자석번호가 다르면 반대 방향으로 회전
            if magnetic[i][2] != magnetic[i+1][6]:
                dir[i] = -dir[i+1]
            # 같으면 전파 멈춤
            else:
                break

        # 오른쪽 전파
        for i in range(k, 3):
            # 현재 자석번호랑 한 칸 뒤의 자석번호가 다르면 반대 방향으로 회전
            if magnetic[i][2] != magnetic[i+1][6]:
                dir[i+1] = -dir[i]
            # 같으면 전파 멈춤
            else:
                break
        
        # 자석들 회전시키기
        for i in range(len(dir)):
            # 시계 방향으로 회전
            if dir[i] == -1:
                magnetic[i] = magnetic[i][1:] + [magnetic[i][0]]
            elif dir[i] == 1:
                magnetic[i] = [magnetic[i][-1]] + magnetic[i][:-1]

    answer = 0 # K번 자식을 회전시킨 후 획득하는 점수의 총합 출력

    for i in range(len(magnetic)):
        # 빨간색 화살표 위치에 있는 날의 자성이 S극일 경우
        if magnetic[i][0] == 1:
            answer += 2 ** i

    print(f'#{test_case} {answer}')