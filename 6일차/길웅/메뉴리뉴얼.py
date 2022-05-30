# 프로그래머스 '메뉴 리뉴얼'
# https://programmers.co.kr/learn/courses/30/lessons/72411

def solution(orders, course):
    max_len = 0
    for i in range(len(orders)):
        max_len = max(max_len, len(orders[i]))
        orders[i] = "".join(sorted(orders[i]))
        
    cnt_lst = [dict() for _ in range(max_len + 1)]

    def dfs(order, idx, cnt, string):

        if string in cnt_lst[cnt]:
            cnt_lst[cnt][string] += 1
        else:
            cnt_lst[cnt][string] = 1
        
        for i in range(idx + 1, len(order)):
            dfs(order, i, cnt + 1, string + order[i])
        
    for order in orders:
        dfs(order, -1, 0, "")
    
    answer = []
    for c in course:
        if c > max_len:
            continue

        max_cnt = 0
        max_course = []

        for k, v in cnt_lst[c].items():
            if v > max_cnt:
                max_cnt = v
                max_course = [k]
            elif v == max_cnt:
                max_course.append(k)
            else:
                continue
        
        if max_cnt < 2:
            continue
        
        for mc in max_course:
            answer.append(mc)
    
    answer.sort();
        
    return answer