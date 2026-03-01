# 원자의 최초 위치는 2차원 평면상의 [x, y]
# 원자는 각자 고유의 움직이는 방향을 가지고 있음.
# 상 : y 증가 / 하 : y 감소 / 좌 : x 감소 / 우 : x 증가
# 모든 원자들의 이동속도는 동일 / 1초에 1만큼 이동
# 모든 원자들은 최초 위치에서 동시에 이동을 시작
# 두 개 이상의 원자가 동시에 충돌할 경우 충돌한 원자들은 모두 보유한 에너지를 방출하고 소멸됨.
# N개의 원자들의 [x, y] 위치, 이동 방향, 보유 에너지가 주어질 때 원자들이 소멸되면서 방출하는 에너지의 총합
# 상 0, 하 1, 좌 2, 우 3

# 방향: 상(0), 하(1), 좌(2), 우(3)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

LIMIT = 4000  # 좌표를 2배로 늘렸으니 원래 [-2000,2000] -> [-4000,4000]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atoms = []
    for _ in range(N):
        x, y, d, k = map(int, input().split())
        atoms.append((x * 2, y * 2, d, k))  # 좌표 2배 스케일링

    ans = 0

    while atoms:
        pos_map = {}  # (x,y) -> [sum_energy, count, dir_if_unique]

        # 1) 모두 1칸(=0.5초) 이동
        for x, y, d, k in atoms:
            nx = x + dx[d]
            ny = y + dy[d]

            # 범위를 벗어나면 소멸(에너지 방출 없음)
            if nx < -LIMIT or nx > LIMIT or ny < -LIMIT or ny > LIMIT:
                continue

            key = (nx, ny)
            if key not in pos_map:
                pos_map[key] = [k, 1, d]  # 에너지합, 개수, (유일할 때 방향)
            else:
                pos_map[key][0] += k
                pos_map[key][1] += 1

        # 2) 충돌 처리 (같은 칸에 2개 이상이면 전부 소멸 + 에너지 합산)
        new_atoms = []
        for (x, y), (sum_k, cnt, d_if_unique) in pos_map.items():
            if cnt >= 2:
                ans += sum_k
            else:
                new_atoms.append((x, y, d_if_unique, sum_k))

        atoms = new_atoms

    print(f"#{tc} {ans}")
