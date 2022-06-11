# 프로그래머스 기능개발
# 22/5/20
# 스택/큐


def solution(progresses, speeds):
    # 수정한 답. 그냥 각 작업 끝나는 기간 리스트 구하지 않고 
    # 처음부터 100 넘는 작업 생기면 나머지 요소 스캔
    answer = []
    state = 0
    count = 1
    for i in range(100):
        for j in range(len(progresses)):
            progresses[j] += speeds[j]

        if progresses[state] >= 100:
            for k in range(state+1, len(progresses)):
                if progresses[k] >= 100:
                    state += 1
                    count += 1
                else:
                    break
            state += 1
            answer.append(count)
            
            count = 1
        
        if state == len(progresses):
            break
    return answer
    
    
    
    
"""     내가 풀었던 답. 앞의 작업 데이터를 지우면서 진행하다보니 
    맨앞 작업 진행 기간 고려하지 않고 따로 비교해서 놓치는 게 생김
    좀더 고민하면 수정할 수 있을거 같은데

    answer = []
    finish = []
    for i in range(len(progresses)):
        for n in range(100):
            if progresses[i] + speeds[i] * n >= 100:
                finish.append(n)
                break
    a = 1

    while len(finish) > 0:
        if len(finish) == 1:
            answer.append(a)
            break
        elif finish[0] >= finish[1]:
            a += 1
        else: 
            answer.append(a)
            a = 1
        finish.pop(0)     """


""" 내코드랑 제일 비슷한 코드. 수정완료

def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    n = 0
    count = 0

    while len(progresses) > 0:
        if progresses[0] + speeds[0] * n >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count >0:
                answer.append(count)
                count = 0
            n += 1
    answer.append(count)
    return answer """