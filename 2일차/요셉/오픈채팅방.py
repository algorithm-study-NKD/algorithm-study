def solution(record):
    answer = []
    user = {} # 딕셔너리
    
    for rec in record:
        splt = rec.split() # 공백으로 분리
        
        if splt[0] == "Enter":
            user[splt[1]] = splt[2] # 아이디 : 닉네임
        elif splt[0] == "Change":
            user[splt[1]] = splt[2] # 변경
            
    for rec in record:
        splt = rec.split()
        
        if splt[0] == "Enter":
            answer.append(user[splt[1]] + "님이 들어왔습니다.") # 문자열로 저장
        elif splt[0] == "Leave":
            answer.append(user[splt[1]] + "님이 나갔습니다.")
    
    return answer