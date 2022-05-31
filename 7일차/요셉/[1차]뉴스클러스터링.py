# [1차] 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter

def solution(str1, str2):
    answer = 0
    
    # 대문자 변환
    str1 = str1.upper()
    str2 = str2.upper()
    
    # 두 글짜씩 끊기
    lst1, lst2 = [], []
    for i in range(2, len(str1)+1):
        word = str1[i-2:i]
        if word.isalpha():
            lst1.append(word)
        
    for i in range(2, len(str2)+1):
        word = str2[i-2:i]
        if word.isalpha():
            lst2.append(word)
            
    # 교집합, 합집합
    counter1, counter2 = Counter(lst1), Counter(lst2)
    
    inter = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    
    len_inter = len(inter)
    len_union = len(union)
    
    # 65536 곱한 후 버림
    if not len_inter and not len_union:
        return 65536
    else:
        return int((len_inter / len_union)*65536)
        