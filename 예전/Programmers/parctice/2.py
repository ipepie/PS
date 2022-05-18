# 두 개 뽑아서 더하기 - level1
# 22/2/4

def solution(numbers):
    sum_nums = [x+y for x in numbers for y in numbers if numbers.index(x) != numbers.index(y)] + [x+x for x in numbers if numbers.count(x) != 1] # 같은 숫자가 두개이상 있을 때 인덱스 조건때문에 리스트에 추가가 안돼서 따로 더해줌
    sum_nums.sort()
    result = []
    for x in sum_nums:
        if x not in result:
            result.append(x)
    return result

# 이중포문 사용하면 되겠다고 생각했지만 list comprehension 사용 연습해보려고 이렇게 풀어봄!
# 이중포문 이용하면
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         result.append(numbers[i] + numbers[j])
# 처럼 사용할 수 있겠네. 다른 인덱스의 요소끼리 더해야하는 조건이니 이게 더 쉬워 보인다.


# 다른 사람의 풀이를 보니까 중복을 제거할 때 완전 편한 방법이 있다
# retrun sorted(list(set(result)))
# 리스트를 셋으로 바꿔 중복을 없애주고 다시 리스트로!