def solution(record):
    name = {}
    answer = []
    
    for log in record:
        log = log.split()
        if log[0] == 'Enter' or log[0] == 'Change':
            name[log[1]] = log[2]
    
    for log in record:
        log = log.split()
        if log[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(name[log[1]]))
        elif log[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(name[log[1]]))
    
    return answer