def solution(rows, columns, queries):
    answer = []
    arr = [[i * columns + j for j in range(1, columns+1)] for i in range(rows)]
    
    for x1, y1, x2, y2 in queries:
        # 맨 위 맨 왼쪽 값
        temp = arr[x1-1][y1-1]
        min_val = temp
        
        # 왼쪽
        for i in range(x1, x2):
            arr[i-1][y1-1] = arr[i][y1-1]
            min_val = min(min_val, arr[i][y1-1])
        
        # 아래
        for i in range(y1, y2):
            arr[x2-1][i-1] = arr[x2-1][i]
            min_val = min(min_val, arr[x2-1][i])
        
        # 오른쪽
        for i in range(x2-1, x1-1, -1):
            arr[i][y2-1] = arr[i-1][y2-1]
            min_val = min(min_val, arr[i-1][y2-1])
        
        # 위
        for i in range(y2-1, y1-1, -1):
            arr[x1-1][i] = arr[x1-1][i-1]
            min_val = min(min_val, arr[x1-1][i-1])
            
        arr[x1-1][y1] = temp
        
        answer.append(min_val)
    
    return answer