def solution(s):
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx, num in enumerate(number):
        s = s.replace(num, str(idx))
    
    return int(s)