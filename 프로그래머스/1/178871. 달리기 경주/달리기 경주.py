def solution(players, callings):
    
    player_dict = {player: i for i, player in enumerate(players)}
    
    for calling in callings:
        # 2. 불린 사람의 현재 등수와 앞사람 이름 찾기
        cur_idx = player_dict[calling] # 딕셔너리라 바로 찾음!
        pre_idx = cur_idx - 1
        front_player = players[pre_idx]
        
        # 3. 리스트에서 두 사람의 위치 교체 (Swap)
        players[pre_idx], players[cur_idx] = players[cur_idx], players[pre_idx]
        
        # 4. 딕셔너리 정보도 같이 업데이트 (중요!)
        player_dict[calling] = pre_idx
        player_dict[front_player] = cur_idx
        
    return players