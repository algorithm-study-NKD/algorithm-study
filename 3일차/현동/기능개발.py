# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    n = len(progresses)
    answer = []
    days = []
    stack = []
    
    for i in range(n):
        value, rest = divmod(100-progresses[i], speeds[i])
        if rest:
            value += 1
        days.append(value)
        
    j = 0
    while j < n:
        cnt = 1
        for k in range(j+1, n):
            if days[j] >= days[k]:
                cnt += 1
            else:
                break
        answer.append(cnt)
        j += cnt
    
    return answer