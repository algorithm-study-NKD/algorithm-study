# 프로그래머스 '기능개발'
# https://programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):
    n = len(progresses)
    days = [0] * n

    for i in range(n):
        days[i] = math.ceil((100 - progresses[i]) / speeds[i])

    i = 0
    day = 0
    answer = []

    while True:
        while i < n:
            if days[i] <= day:
                answer[-1] += 1
                i += 1
                continue
            else:
                break
        
        if i < n:
            day = days[i]
            answer.append(0)
        else:
            break

    return answer