import heapq

def solution(scoville, K):
    answer = 0
    heap_tree = [] 
    
    for s in scoville: 
        heapq.heappush(heap_tree, s)

    while heap_tree[0] <= K:
        if len(heap_tree) <= 1:
            break
            
        min1 = heapq.heappop(heap_tree)
        min2 = heapq.heappop(heap_tree)

        heapq.heappush(heap_tree, min1 + (min2*2))
        
        answer += 1
        
    for s in heap_tree:
        if s < K:
            return -1
    
    return answer