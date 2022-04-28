# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    
    while n > 0:
        n, rest = divmod(n, 3)
        if rest == 1:
            answer += '1'
        elif rest == 2:
            answer += '2'
        else:
            answer += '4'
            n -= 1
    
    return answer[::-1]