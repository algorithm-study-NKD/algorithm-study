def solution(w,h):
    if w == 1 or h == 1:
        return 0
    if w == h: return (w*h)-w

    i = w if w < h else h
    while w%i != 0 or h%i != 0:
        if i == 1: 
            break
        i -= 1
    
    return h*w-(w+h-i)