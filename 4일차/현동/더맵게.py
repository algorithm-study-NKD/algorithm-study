# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    answer = 0
    while True:
        first = heapq.heappop(scoville)
        if first > K:
            return answer
        
        if not len(scoville):
            return -1
        
        answer += 1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
        
    return answer