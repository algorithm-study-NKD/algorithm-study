def start_time(log, t):
    hh, mm , ss = log
    ss = round(float(ss) - float(t) + 0.001, 3)
    if ss < 0:
        mm = int(mm)-1
        ss += 60
        if mm < 0:
            hh = int(hh)-1
            mm = mm + 60
            if hh < 0:
                return [0, 0, 0]
    return [int(hh),int(mm),ss]


def after_1min(log):
    hh, mm , ss = log
    ss = round(float(ss) + 0.999, 3)
    if ss >= 60:
        ss = round(ss - 60, 3)
        mm = int(mm) + 1
        if mm >= 60:
            mm -= 60
            hh = int(hh) + 1
            if hh >= 60:
                return [23, 59, 59.999]
    return [int(hh),int(mm),ss]

def is_contain(end, start):
    if end[0] < start[0]: return False
    if end[1] < start[1]: return False
    if end[2] < start[2]: return False
    return True
    
def solution(lines):
    answer = 1
    lines = list(map(lambda x: [x.split()[1].split(':'), x.split()[2][:-1]], lines))
    for i in range(len(lines)-1):
        cnt = 1
        for j in range(i+1, len(lines)):
            if is_contain(after_1min(lines[i][0]), start_time(lines[j][0], lines[j][1])):
                cnt += 1
        answer = max(answer, cnt)
    return answer