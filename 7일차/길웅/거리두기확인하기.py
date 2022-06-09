# 프로그래머스 '거리두기 확인하기'
# https://programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    N = 5
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    answer = []

    def dfs(room, st_i, st_j, i, j, cnt):
        if cnt >= 2:
            return 1
        
        for d in range(4):
            n_i = i + di[d]
            n_j = j + dj[d]

            if not (0 <= n_i < N) or not (0 <= n_j < N):
                continue

            if n_i == st_i and n_j == st_j:
                continue
            
            if room[n_i][n_j] == 'X':
                continue
            elif room[n_i][n_j] == 'P':
                return 0
            else:
                save_answer = dfs(room, st_i, st_j, n_i, n_j, cnt + 1)
                if save_answer == 0:
                    return 0
                else:
                    continue
        
        return 1


    for k in range(N):
        save_answer = 1
        for i in range(N):
            if save_answer == 0:
                break
            for j in range(N):
                if save_answer == 0:
                    break
                if places[k][i][j] == 'P':
                    save_answer = dfs(places[k], i, j, i, j, 0)
        
        answer.append(save_answer)
    return answer