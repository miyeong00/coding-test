def solution(data, ext, val_ext, sort_by):
    answer = []
    standard = ['code', 'date', 'maximum', 'remain']
    idx = standard.index(ext)
    sorting = standard.index(sort_by)
    
    for d in data:
        if d[idx] < val_ext:
            answer.append(d)
    
    return sorted(answer, key=lambda x: x[sorting])