def solution(s):
    answer = len(s)
    if len(s) == 1: return 1

    for i in range(1, len(s)//2+1):
        result = ''
        prev = s[0:i]
        cnt = 1
        
        for j in range(i, len(s), i):
            if prev != s[j:j+i]:
                result += prev if cnt == 1 else str(cnt) + prev
                prev = s[j:j+i]
                cnt = 1
            else:
                cnt += 1
        result += prev if cnt == 1 else str(cnt) + prev
        answer = min(len(result), answer)
            
    return answer