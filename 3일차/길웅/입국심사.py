# 프로그래머스 '입국심사'
# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n: int, times: list):
    max_time = max(times)

    l = 0
    r = max_time * n + 1

    while l < r:
        md = (l + r) // 2

        total = 0
        for time in times:
            total += (md // time)

        if total < n:
            l = md + 1
        else:
            r = md

    answer = l
    return answer