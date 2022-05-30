# 프로그래머스 '괄호 변환'
# https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):

    def parse(w):
        # check1
        if len(w) == 0:
            return w
        
        # check2
        u = ""
        v = ""
        l_cnt = 0
        r_cnt = 0
        i = 0
        while i < len(w):
            u += w[i]
            if w[i] == "(":
                l_cnt += 1
            else:
                r_cnt += 1
            
            i += 1

            if l_cnt == r_cnt:
                break
        
        while i < len(w):
            v += w[i]
            i += 1
        
        # check3
        stk = []
        flag = True
        if u[0] == ")":
            flag = False
        
        if flag:
            for i in range(len(u)):
                if u[i] == "(":
                    stk.append(u[i])
                else:
                    stk.pop()
        
        if len(stk) == 0 and flag:
            return u + parse(v)
        else:   # check4
            res = "("
            res += parse(v)
            res += ")"

            for i in range(1, len(u) - 1):
                if u[i] == "(":
                    res += ")"
                else:
                    res += "("

            return res
    
    return parse(p)