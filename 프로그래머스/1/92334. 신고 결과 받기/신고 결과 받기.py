# 각 유저는 한 번에 한 명의 유저를 신고할 수 있음.
# 신고 회수 제한 X. 서로 다른 유저를 계속 신고 가능
# 한 유저를 여러 번 신고할 수 있음. 하지만 1회로 처리
# k번 이상 신고된 유저는 게시판 이용이 정지됨.
# 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송함.
# id_list : 이용자의 ID가 담긴 문자열 배열
# report : 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열
# k : 정지 기준이 되는 신고 횟수 
# 각 유저별로 처리 결과 메일을 받은 횟수

def solution(id_list, report, k):
    reporting = {user: [] for user in id_list}
    reported = {user: 0 for user in id_list}
    
    for r in set(report):
        ing, ed = r.split(" ") # ing: 신고하는 유저, ed: 신고 당하는 유저
        
        if ing not in reporting:
            reporting[ing] = []
        reporting[ing].append(ed)
        
        if ed not in reported:
            reported[ed] = 0
        reported[ed] += 1
    
    stop = [] # 정지되는 ID
    
    for id in reported:
        if reported[id] >= k:
            stop.append(id)
        
    answer = [0] * len(id_list) # 각 유저별로 처리 결과 메일을 받은 횟수
    for i in range(len(id_list)):
        for s in stop:
            if s in reporting[id_list[i]]:
                answer[i] += 1
        
    return answer