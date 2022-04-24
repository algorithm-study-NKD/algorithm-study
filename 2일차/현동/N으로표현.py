def solution(N, number):
    if N == number:
        return 1
    
    step = {}
    step[1] = {N}
    
    for i in range(2, 9):
        step[i] = {int(str(N)*i)}
        for j in range(1, i):
            for x in step[j]:
                for y in step[i-j]:
                    step[i].add(x+y)
                    step[i].add(x-y)
                    step[i].add(x*y)
                    if y != 0:
                        step[i].add(x//y)
        if number in step[i]:
            return i
    return -1