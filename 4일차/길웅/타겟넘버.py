# 프로그래머스 '타겟 넘버'
# https://programmers.co.kr/learn/courses/30/lessons/43165

def dfs(numbers:list, target:int, idx:int, number:int):
    if idx >= len(numbers):
        if number == target:
            return 1
        return 0
    
    return dfs(numbers, target, idx + 1, number + numbers[idx]) + dfs(numbers, target, idx + 1, number - numbers[idx])


def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer