# 프로그래머스 카펫
# 22/5/26
# 완전탐색

# 첫번째 포문에서 바로 약수 하나 가지고 대입해서 풀었어도 될듯
def solution(brown, yellow):
    answer = []
    a = brown + yellow

    # 직사각형의 가로 * 세로 == brown + yellow 이므로 a의 약수 구하기
    for i in range(1,a):
        if a % i == 0:
            answer.append(i)
    # brown = 2w + 2h - 4
    # 위의 식에서 answer의 두 요소의 합을 w+h에 대입
    for x in answer:
        for y in answer:
            if x + y + .0 == (brown+4)/2 and x>=y:
                return [x,y]