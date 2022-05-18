# 해시 > 완주하지 못한 선수 - level1
# 22/2/6

def solution(participant, completion):
    participant.sort()   
    completion.sort()
    if participant[-1] != completion[-1]:
            return(participant.pop())
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return(participant[i])


# 그냥 count메소드 써서 두리스트 원소 비교해서 다른거 출력하면 효율성에서 다실패. 비효율떴음.
# 정렬하고 인덱스 i에 해당하는 원소가 다를 때로 비교해도 만약 participant의 맨 마지막 인덱스에 있으면 outofindex 가 발생하니까 반복문 시작전에 마지막 원소인지 [-1]이용해서 상수시간 체크하고 반복문실행.
