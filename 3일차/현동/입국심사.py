# https://programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    left, right = min(times), max(times)*n
    
    while left < right:
        mid = (left+right) // 2
        
        total = 0
        for time in times:
            total += mid // time
        
        if n <= total:
            right = mid
        else:
            left = mid+1
            
    return left