def solution(friends, gifts):
    # 1. 친구 이름별 인덱스 생성 (이름 -> 숫자)
    f_idx = {name: i for i, name in enumerate(friends)}
    n = len(friends)
    
    # 2. 선물을 주고받은 내역을 저장할 2차원 행렬
    # gift_matrix[A][B] = A가 B에게 준 선물 개수
    gift_matrix = [[0] * n for _ in range(n)]
    
    # 3. 선물 지수를 계산하기 위한 준/받은 개수 저장
    given_cnt = [0] * n
    received_cnt = [0] * n
    
    for gift in gifts:
        giver, receiver = gift.split()
        g_i, r_i = f_idx[giver], f_idx[receiver]
        
        gift_matrix[g_i][r_i] += 1
        given_cnt[g_i] += 1
        received_cnt[r_i] += 1
        
    # 4. 선물 지수 계산 (준 거 - 받은 거)
    gift_indices = [given_cnt[i] - received_cnt[i] for i in range(n)]
    
    # 5. 다음 달에 받을 선물 계산
    next_month_gifts = [0] * n
    
    # 모든 친구 쌍(i, j)을 비교
    for i in range(n):
        for j in range(i + 1, n):
            # i가 j에게 준 것 vs j가 i에게 준 것
            if gift_matrix[i][j] > gift_matrix[j][i]:
                next_month_gifts[i] += 1
            elif gift_matrix[i][j] < gift_matrix[j][i]:
                next_month_gifts[j] += 1
            else:
                # 주고받은 기록이 없거나 같으면 선물 지수 비교
                if gift_indices[i] > gift_indices[j]:
                    next_month_gifts[i] += 1
                elif gift_indices[i] < gift_indices[j]:
                    next_month_gifts[j] += 1
                    
    # 6. 가장 많이 받는 사람의 선물 개수 반환
    return max(next_month_gifts)