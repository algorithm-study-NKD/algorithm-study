def solution(s):
    stk = []
    stk.append(s[0])
    ptr = 1

    while ptr < len(s):
        if stk and stk[-1] == s[ptr]:
            ptr += 1
            stk.pop()
        else:
            stk.append(s[ptr])
            ptr += 1
            
    if stk:
        answer = 0
    else:
        answer = 1
        
    return answer