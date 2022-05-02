# 프로그래머스 '기능개발'
# https://programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):
    n = len(progresses)
    days = [0] * n

    for i in range(n):
        days[i] = math.ceil((100 - progresses[i]) / speeds[i])

    i = 0
    day = days[0]
    answer = []

    while i < n:
        answer.append(0)
        
        while i < n:
            if days[i] <= day:
                answer[-1] += 1
                i += 1
                continue
            else:
                day = days[i]
                break

    return answer