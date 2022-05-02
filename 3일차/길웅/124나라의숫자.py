# 프로그래머스 '124 나라의 숫자'
# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''

    while n:
        n -= 1

        mod = n % 3
        if mod == 0:
            answer += '1'
        elif mod == 1:
            answer += '2'
        else:
            answer += '4'
        
        n //= 3
    
    answer = answer[::-1]
    return answer