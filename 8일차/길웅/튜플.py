# 프로그래머스 '튜플'
# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer_dict = dict()

    s = s[1:-1]
    tmp_list = []
    tmp_s = ""
    flag = False

    for c in s:
        if c == '{':
            flag = True
        elif c == '}':
            tmp_list.append(int(tmp_s))
            tmp_s = ""

            for num in tmp_list:
                if num in answer_dict:
                    answer_dict[num] = min(answer_dict[num], len(tmp_list))
                else:
                    answer_dict[num] = len(tmp_list)
            tmp_list.clear()

            flag = False
        elif c == ',':
            if flag:
                tmp_list.append(int(tmp_s))
                tmp_s = ""
        else:
            tmp_s += c

    answer = sorted(answer_dict, key=lambda k: answer_dict[k])
    return answer