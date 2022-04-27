def solution(progresses, speeds):
    answer = []
    count = 0
    
    while(progresses != []):
        progresses = [progresses + speeds for progresses, speeds in zip(progresses, speeds)]
        print(progresses)
        if(progresses[0] >= 100):
            for i in range(len(progresses)):
                if(progresses[i] < 100): break
                else: count += 1
            answer.append(count)
            for i in range(0, count):
                del progresses[0]
                del speeds[0]
            count = 0

    return answer