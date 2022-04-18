# 프로그래머스 '[1차] 추석 트래픽'
# https://programmers.co.kr/learn/courses/30/lessons/17676

def calc_time(time, s2):
    d, h, m, s = time

    if s2 >= 0:
        s += s2
        if s >= 60:
            s -= 60
            m += 1
        
        if m >= 60:
            m -= 60
            h += 1
        
        if h >= 24:
            h -= 24
            d = "2016-09-16"
    else:
        s += s2
        if s < 0:
            s += 60
            m -= 1
        
        if m < 0:
            m += 60
            h -= 1
        
        if h < 0:
            h += 24
            d = "2016-09-14"
    
    s = round(s, 3)
    return (d, h, m, s)


def solution(lines):
    st_logs = list()
    fn_logs = list()
    for log in lines:
        fn_day, fn_time, length = log.split()

        fn_h, fn_m, fn_s = fn_time.split(":")

        fn_h = int(fn_h)
        fn_m = int(fn_m)
        fn_s = float(fn_s)
        
        length = float(length[:-1])

        st_day, st_h, st_m, st_s = calc_time((fn_day, fn_h, fn_m, fn_s), -length + 0.001)
        
        st_logs.append((st_day, st_h, st_m, st_s))
        fn_logs.append((fn_day, fn_h, fn_m, fn_s))
    
    answer = 0

    for i in range(len(lines)):
        st = fn_logs[i]
        fn = calc_time(st, 0.999)
        
        cnt = 1
        
        for j in range(i + 1, len(lines)):
            if fn_logs[j] > calc_time(fn, 3):
                break
            if st_logs[j] <= fn:
                cnt += 1

        answer = max(answer, cnt)
    return answer