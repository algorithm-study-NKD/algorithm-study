def solution(s):
    answer = 9876543210 # max값 설정
    leng = len(s) # s의 길이, aabbaccc
    
    if leng == 1: # 길이가 1일 때 처리
        return 1
    
    for i in range(1, (leng//2)+1): # 1부터 len(s) // 2까지
        cur, cnt, result = s[0:i], 1, "" # s 쪼개기, a, aa, aab, aabb
        
        for j in range(i, leng+1, i): # i부터 len(s)까지
            # print(cur)
            if cur == s[j:j+i]: # cur 다음 문자열에서 cur 길이만큼 쪼갠 결과
                cnt += 1
            else:
                if cnt != 1: # 1 생략
                    result += str(cnt)
                result += cur
                
                cur = s[j:j+i] # cur 재정의
                cnt = 1 # 1로 초기화
        
        # 남은 문자열 처리
        if cnt != 1:
            result += str(cnt)
        result += cur
        
        # print(result)
        answer = min(len(result), answer) # 최소값
            
    return answer