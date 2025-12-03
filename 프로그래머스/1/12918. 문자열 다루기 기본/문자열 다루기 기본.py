def solution(s):
    if len(str(s)) == 4 or len(str(s)) == 6:
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False