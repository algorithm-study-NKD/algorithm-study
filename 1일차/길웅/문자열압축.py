# 프로그래머스 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s:str):
    answer = len(s)
    for num in range(1, len(s)//2 + 1):
        length = len(s)

        i = 0

        cnt = 1

        while i <= len(s) - 2*num:
            if s[i:(i + num)] == s[(i + num):(i + 2*num)]:
                length -= num
                if cnt == 1 or cnt == 9 or cnt == 99 or cnt == 999:
                    length += 1
                cnt += 1
            else:
                cnt = 1
            i += num
        
        answer = min(answer, length)
    return answer