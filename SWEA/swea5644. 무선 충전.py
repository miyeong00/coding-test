# 10 * 10 영역의 지도
# 같은 영역에 두 개의 배터리 충전기가 있다면 두 개 중 하나 선택해도 되고 하나를 나눠 써도 됨.
# BC의 정보와 사용자의 이동 궤적이 주어졌을 때, 모든 사용자가 충전한 양의 합의 최댓값 구하기
# 사용자 2명, 사용자 A는 지도의 (1, 1) 지점에서, 사용자 B는 지도의 (10, 10) 지점에서 출발

T = int(input()) # 테스트 케이스 개수
for test_case in range(1, T+1):
    M, A = map(int, input().split()) # M : 총 이동 시간, A : BC의 개수
    A_move = list(map(int, input().split())) # 사용자 A의 이동 정보
    B_move = list(map(int, input().split())) # 사용자 B의 이동 정보
    BC = [list(map(int, input().split())) for _ in range(A)] # X, Y 좌표, 충전 범위(C), 처리량(P)

    # 이동 방향: 0(정지), 1(상), 2(우), 3(하), 4(좌)
    dx = [0, 0, 1, 0, -1]
    dy = [0, -1, 0, 1, 0]

    # 사용자 초기 위치
    ax, ay = 1, 1
    bx, by = 10, 10

    total = 0  # 모든 시간의 최대 충전량 합

    # 0초(이동 전)도 충전 가능하므로,
    # 이동 배열 앞에 0(정지)을 붙여서 0초~M초를 동일하게 처리
    A_path = [0] + A_move
    B_path = [0] + B_move

    # 0초부터 M초까지 총 M+1번 시뮬레이션
    for t in range(M + 1):
        # 현재 시간의 이동을 적용
        a_dir = A_path[t]
        b_dir = B_path[t]

        ax += dx[a_dir]
        ay += dy[a_dir]
        bx += dx[b_dir]
        by += dy[b_dir]

        # 각 사용자가 접속 가능한 BC 목록(인덱스)을 구한다
        a_can = []  # A가 접속 가능한 BC 인덱스들
        b_can = []  # B가 접속 가능한 BC 인덱스들

        for i in range(A):
            x, y, c, p = BC[i]
            # 맨해튼 거리 <= c 이면 접속 가능
            if abs(ax - x) + abs(ay - y) <= c:
                a_can.append(i)
            if abs(bx - x) + abs(by - y) <= c:
                b_can.append(i)

        # A가 선택한 BC i, B가 선택한 BC j의 모든 조합을 비교해서 그 시간의 최대 충전량을 찾는다.
        best = 0

        # 아무 BC도 못 잡는 경우 대비: [-1]을 넣어 "선택 없음"도 조합에 포함
        a_choices = a_can if a_can else [-1]
        b_choices = b_can if b_can else [-1]

        for i in a_choices:
            for j in b_choices:
                # i 또는 j가 -1이면 해당 사용자는 충전 안 함(0)
                if i == -1 and j == -1:
                    charge = 0
                elif i == -1:
                    charge = BC[j][3]  # B만 충전
                elif j == -1:
                    charge = BC[i][3]  # A만 충전
                else:
                    # 둘 다 BC 선택
                    if i == j:
                        # 같은 BC를 공유하면 총합은 P 한 번만
                        charge = BC[i][3]
                    else:
                        # 서로 다른 BC면 각각 충전해서 합
                        charge = BC[i][3] + BC[j][3]

                if charge > best:
                    best = charge

        total += best

    print(f"#{test_case} {total}")