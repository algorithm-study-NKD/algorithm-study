def solution(lines):
    answer = 0
    
    for line in lines:
        data = line.split()
        s = list(map(float, data[1].split(':')))
        t = float(data[2][:-1])
        
        end_time = (s[0]*3600 + s[1]*60 + s[2]) * 1000
        start_time = end_time - t * 1000 + 1
        
        cnt = 0
        if start_time <= end_time:
            cnt += 1
            
    
    return answer
