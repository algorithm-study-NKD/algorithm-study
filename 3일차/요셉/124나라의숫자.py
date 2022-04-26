def solution(n):
    answer = ''
    
    while n:
        n, rest = divmod(n, 3)
        if not rest:
            n -= 1
        answer = '412'[rest] + answer
        
    return answer