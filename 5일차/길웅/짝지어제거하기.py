# 프로그래머스 '짝지어 제거하기'
# https://programmers.co.kr/learn/courses/30/lessons/12973

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