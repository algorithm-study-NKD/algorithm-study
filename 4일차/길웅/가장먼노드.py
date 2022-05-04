# 프로그래머스 '가장 먼 노드'
# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    node_dict = dict()

    for e1, e2 in edge:
        if e1 not in node_dict:
            node_dict[e1] = list()
        
        if e2 not in node_dict:
            node_dict[e2] = list()
            
        node_dict[e1].append(e2)
        node_dict[e2].append(e1)
    
    que = deque()
    visits = [False] * (n + 1)

    node = 1
    level = 0
    que.append((node, level))
    visits[1] = True
    
    max_level = 0
    answer = 0

    while que:
        node, level = que.popleft()
        
        if max_level < level:
            max_level = level
            answer = 1
        else:
            answer += 1

        next_nodes = node_dict.get(node, None)

        if next_nodes == None:
            continue

        for next_node in next_nodes:
            if visits[next_node]:
                continue

            que.append((next_node, level + 1))
            visits[next_node] = True

    return answer