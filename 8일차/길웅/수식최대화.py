# 프로그래머스 '수식 최대화'
# https://programmers.co.kr/learn/courses/30/lessons/67257

def set_priority(p):
    if p == 0:
        return ['*', '+', '-']
    if p == 1:
        return ['*', '-', '+']
    if p == 2:
        return ['+', '*', '-']
    if p == 3:
        return ['+', '-', '*']
    if p == 4:
        return ['-', '*', '+']
    if p == 5:
        return ['-', '+', '*']
    
    return None

def calculate(num1, num2, ex):
    if ex == '*':
        return num1 * num2
    if ex == '+':
        return num1 + num2
    if ex == '-':
        return num1 - num2
    
    return None


def solution(expression):
    num_list = []
    ex_list = []
    
    tmp = ""
    for c in expression:
        if c.isdigit():
            tmp += c
        else:
            if len(tmp) > 0:
                num_list.append(int(tmp))
                tmp = ""
            
            ex_list.append(c)
            
    if len(tmp) > 0:
        num_list.append(int(tmp))
        tmp = ""
        
    answer = 0

    for p in range(6):
        priority = set_priority(p)

        new_num_list = num_list.copy()
        new_ex_list = ex_list.copy()

        for ex in priority:
            i = 0
            while i < len(new_ex_list):
                if new_ex_list[i] == ex:
                    new_num_list[i] = calculate(new_num_list[i], new_num_list[i + 1], ex)
                    new_num_list.pop(i + 1)
                    new_ex_list.pop(i)
                else:
                    i += 1
        
        answer = max(answer, abs(new_num_list[0]))
    
    return answer