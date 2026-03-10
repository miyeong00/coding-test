def solution(park, routes):
    H = len(park)
    W = len(park[0])
    
    # 1. 시작 지점(S) 찾기
    cur_x, cur_y = 0, 0
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                cur_x, cur_y = i, j
                break

    # 이동 방향 매핑 (북, 남, 서, 동)
    direction = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    
    for route in routes:
        # 2. 명령 분리 (예: "E 5" -> "E", 5)
        d_char, count = route.split()
        count = int(count)
        dx, dy = direction[d_char]
        
        # 이동 전 현재 위치 저장
        temp_x, temp_y = cur_x, cur_y
        is_ok = True
        
        # 3. 'count'만큼 한 칸씩 이동하며 검사
        for _ in range(count):
            nx = temp_x + dx
            ny = temp_y + dy
            
            # 공원을 벗어나는지 확인
            if not (0 <= nx < H and 0 <= ny < W):
                is_ok = False
                break
            
            # 장애물(X)을 만나는지 확인
            if park[nx][ny] == 'X':
                is_ok = False
                break
            
            # 한 칸 이동 성공! 임시 위치 업데이트
            temp_x, temp_y = nx, ny
        
        # 4. 모든 칸을 무사히 통과했다면 실제 위치 업데이트
        if is_ok:
            cur_x, cur_y = temp_x, temp_y
            
    return [cur_x, cur_y]