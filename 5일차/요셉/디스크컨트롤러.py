import heapq

def solution(jobs):
    time, cur, i = 0, 0, 0
    start = -1
    hq = []
    
    while i < len(jobs):
        for job in jobs:
            
            if start < job[0] <= cur:
                heapq.heappush(hq, (job[1], job[0]))
        
        if len(hq) > 0:
            end_time, start_time = heapq.heappop(hq)
            start = cur
            cur += end_time
            time += cur - start_time
            i += 1
        else:
            cur += 1
    
    return int(time/len(jobs))