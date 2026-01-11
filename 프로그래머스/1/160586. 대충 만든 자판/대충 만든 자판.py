def solution(keymap, targets):
    min_press = {}
    
    for key in keymap:
        for i, char in enumerate(key):
            if char not in min_press or i + 1 < min_press[char]:
                min_press[char] = i + 1
    
    answer = []
    
    for target in targets:
        total = 0
        for char in target:
            if char in min_press:
                total += min_press[char]
            else:
                total = -1
                break
        answer.append(total)
        
    return answer