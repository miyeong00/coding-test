def solution(today, terms, privacies):
    answer = []
    ty, tm, td = today.split(".")
    today_days = (int(ty) * 12 * 28) + (int(tm) * 28) + int(td)
    
    term = {}
    for t in terms:
        t_type, month = t.split(" ")
        term[t_type] = int(month)
    
    for i in range(len(privacies)):
        date, p_type = privacies[i].split(" ")
        py, pm, pd = date.split(".")
        privacy_days = (int(py) * 12 * 28) + (int(pm) * 28) + int(pd)
        
        if today_days >= privacy_days + (28 * term[p_type]):
                answer.append(i + 1)
    
    return answer