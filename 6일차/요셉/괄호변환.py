def isOk(p):
    st = []
    
    for p_ in p:
        if len(st) != 0:
            if st[-1] == '(' and p_ == ')':
                st.pop()
            else: st.append(p_)
        else: st.append(p_)
        
    return False if len(st) else True

def isBalanced(p):
    a, b = 0, 0
    
    for p_ in p:
        if p_ == '(': a += 1
        else: b += 1
            
    return True if a == b else False

def dfs(p):
    if isOk(p): return p;
    
    for i in range(2, len(p)+1, 2):
        u, v = p[:i], p[i:]
        
        if isBalanced(u):
            if isOk(u): 
                return u + dfs(v)
            else:
                temp = '(' + dfs(v) + ')'
                for i in u[1:-1]:
                    if i == '(':
                        temp += ')'
                    else:
                        temp += '('
                return temp

def solution(p):
    if not p: return ''

    answer = dfs(p)
    
    return answer