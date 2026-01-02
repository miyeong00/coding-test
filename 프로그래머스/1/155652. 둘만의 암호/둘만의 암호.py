def solution(s, skip, index):
    answer = ''
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    
    for ch in skip:
        alphabets = alphabets.replace(ch, "")
    
    for char in s:
        curr_idx = alphabets.index(char)
        
        new_idx = (curr_idx + index) % len(alphabets)
        
        answer += alphabets[new_idx]
        
    return answer