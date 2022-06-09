# 프로그래머스 '[1차] 뉴스 클러스터링'
# https://programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    def get_char_list(my_str):
        ptr = 0
        lst = []
        while ptr + 1 < len(my_str):
            my_char = my_str[ptr:ptr + 2]
            if my_char.isalpha():
                lst.append(my_char)

            ptr += 1
        
        return lst

    lst1 = get_char_list(str1)
    lst2 = get_char_list(str2)

    if len(lst1) + len(lst2) == 0:
        return 65536

    inter_cnt = 0

    for char1 in lst1:
        for j in range(len(lst2)):
            char2 = lst2[j]

            if char1 == char2:
                inter_cnt += 1
                lst2.pop(j)
                break
    
    answer = (inter_cnt * 65536) // (len(lst1) + len(lst2))
    return answer