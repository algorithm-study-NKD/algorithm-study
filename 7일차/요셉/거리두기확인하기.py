# 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302

# 00000
# 00P12
# 0X4X0
# 00500

def check(y, x, place):
    
    # p 오른쪽이 p면 false
    if place[y][x+1] == 'P':
        return False
    
    # p 오른쪽이 o일 때, x축 p+1 하, p+2 확인
    elif place[y][x+1] == 'O':
        if place[y][x+2] == 'P' or place[y+1][x+1] == 'P':
            return False
    
    # p 하단이 p면 false
    if place[y+1][x] == 'P':
        return False
    
    # p 하단이 o일 때, y축 p+1 좌우, p+2 확인
    elif place[y+1][x] == 'O':
        if place[y+2][x] == 'P' or place[y+1][x+1] == 'P' or place[y+1][x-1] == 'P':
            return False
    
    # p 왼쪽이 o일 때, y축 p+1 좌 확인
    if place[y][x-1] == 'O' and place[y+1][x-1] == 'P':
        return False
        
    return True
        

def find(place):
    # 범위 안 벗어나도록 패딩 추가
    place = ['0{0}00'.format(p) for p in place]
    place.extend(['00000000', '00000000'])
    
    for i in range(7):
        for j in range(8):
            if place[i][j] == 'P':
                if not check(i, j, place): # 맨해튼 거리 체크
                    return False
    return True

def solution(places):
    answer = []
    
    # 순서대로
    for place in places:
        if not find(place): # 거리두기 판별
            answer.append(0)
        else:
            answer.append(1)
        
    return answer