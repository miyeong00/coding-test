def solution(id_list, report, k):
    # 1. 중복 신고 제거
    report = list(set(report))
    
    # 2. 유저별 신고당한 횟수를 저장할 딕셔너리
    report_count = {id: 0 for id in id_list}
    # 3. 각 유저가 신고한 대상 목록을 저장할 딕셔너리
    user_reports = {id: [] for id in id_list}
    
    # 신고 정보 기록
    for r in report:
        reporter, target = r.split()
        report_count[target] += 1
        user_reports[reporter].append(target)
    
    # 4. 정지된 유저를 신고한 횟수 계산
    answer = []
    for user in id_list:
        mail_count = 0
        for target in user_reports[user]:
            if report_count[target] >= k:
                mail_count += 1
        answer.append(mail_count)
        
    return answer