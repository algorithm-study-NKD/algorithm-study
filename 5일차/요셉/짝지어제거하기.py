def solution(s):
    answer = -1

    st = []
    
    for i in s:
        if len(st) == 0:
            st.append(i)
        elif st[-1] == i:
            st.pop()
        else:
            st.append(i)
            
    if len(st) == 0: answer = 1
    else: answer = 0

    return answer