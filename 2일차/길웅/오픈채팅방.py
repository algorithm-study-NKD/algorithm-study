# 프로그래머스 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    nickname_dict = dict()

    split_cmds = []

    for rec in record:
        cmds = rec.split()
        split_cmds.append(cmds)

        if len(cmds) == 3:
            cmd, id, nickname = cmds
            nickname_dict[id] = nickname
    
    for cmds in split_cmds:
        cmd, id = cmds[0], cmds[1]
        nickname = nickname_dict[id]

        if cmd == "Enter":
            res = nickname + "님이 들어왔습니다."
        elif cmd == "Leave":
            res = nickname + "님이 나갔습니다."
        else:
            continue

        answer.append(res)
        
    return answer