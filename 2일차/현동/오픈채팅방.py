def solution(record):
    name = {}
    answer = []
    
    for log in record:
        log = log.split()
        if log[0] == 'Leave':
            answer.append(log)
        elif log[0] == 'Enter':
            name[log[1]] = log[2]
            answer.append(log)
        elif log[0] == 'Change':
            name[log[1]] = log[2]
        
    for i, log in enumerate(answer):
        if log[0] == 'Enter':
            answer[i] = '{}님이 들어왔습니다.'.format(name[log[1]])
        else:
            answer[i] = '{}님이 나갔습니다.'.format(name[log[1]])
    
    return answer