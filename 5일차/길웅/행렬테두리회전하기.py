# 프로그래머스 '행렬 테두리 회전하기'
# https://programmers.co.kr/learn/courses/30/lessons/77485

def rotate(map, query, MAX_NUM):
    i1, j1, i2, j2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1

    tmp = map[i1][j1]
    min_num = MAX_NUM

    for i in range(i1 + 1, i2 + 1):
        map[i - 1][j1] = map[i][j1]
        min_num = min(min_num, map[i - 1][j1])

    for j in range(j1 + 1, j2 + 1):
        map[i2][j - 1] = map[i2][j]
        min_num = min(min_num,  map[i2][j - 1])
    
    for i in range(i2 - 1, i1 - 1, -1):
        map[i + 1][j2] = map[i][j2]
        min_num = min(min_num, map[i + 1][j2])
    
    for j in range(j2 - 1, j1, -1):
        map[i1][j + 1] = map[i1][j]
        min_num = min(min_num, map[i1][j + 1])
    
    map[i1][j1 + 1] = tmp
    min_num = min(min_num, map[i1][j1 + 1])

    return min_num


def solution(rows, columns, queries):
    map = [[j for j in range(columns * i + 1, columns * (i + 1) + 1)] for i in range(rows)]
    MAX_NUM = len(map) * len(map[0])

    answer = []
    for query in queries:
        answer.append(rotate(map, query, MAX_NUM))
        
    return answer