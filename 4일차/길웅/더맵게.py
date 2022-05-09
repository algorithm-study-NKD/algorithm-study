# 프로그래머스 '더 맵게'
# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0

    while True:
        k1 = heapq.heappop(scoville)

        if k1 >= K:
            break
        
        if len(scoville) == 0:
            answer = -1
            break

        k2 = heapq.heappop(scoville)

        heapq.heappush(scoville, k1 + 2 * k2)
        answer += 1
    
    return answer