# 프로그래머스 주식가격
# 22/5/25
# 스택/큐

# 효율성은 별로이지만 그냥 간단하게 품
# answer = [0] * len(prices)로 잡아두고, cur안쓰고 바로 answer[i] += 1하는게 더 편할듯
def solution(prices):
    answer = []
    cur = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                cur += 1
                if j == len(prices)-1:
                    answer.append(cur)
                    cur = 0
            else:
                cur += 1
                answer.append(cur)
                cur = 0
                break
    answer.append(0)
    return answer





print(solution([1, 2, 3, 2, 3]))