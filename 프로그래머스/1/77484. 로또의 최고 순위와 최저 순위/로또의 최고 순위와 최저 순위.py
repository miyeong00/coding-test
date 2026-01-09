def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    cur_lotto = 0 # 원래 내 번호에서 맞는 개수
    for lotto in lottos:
        if lotto in win_nums:
            cur_lotto += 1
    
    zero_count = lottos.count(0) # 0 개수
    
    best_rank = rank[cur_lotto + zero_count]
    worst_rank = rank[cur_lotto]
        
    return [best_rank, worst_rank]