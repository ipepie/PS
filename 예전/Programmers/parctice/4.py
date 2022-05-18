def solution(phone_book):
    phone_book.sort(key = lambda x:(x,len(x)))
    for x in range(len(phone_book)-1):
        if phone_book[x+1].startswith(phone_book[x]):
            return(False)
    return(True)


# 처음 제출코드 효율성테스트 3,4 통과못함.
# def solution(phone_book):
#     phone_book.sort()
#     for x in range(len(phone_book)):
#         for y in range(x+1,len(phone_book)):
#             if phone_book[y].startswith(phone_book[x]):
#                 return(False)
#     return(True)

# 정렬기준을 사전순, 길이 두가지로 잡으라는 힌트보고 수정해봤는데 이게 되는구나
# 이중포문 -> 포문으로 


# 다른분 해쉬 사용한 정석 풀이방법.. 생각못하겠다. 해쉬공부용 참고!
# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer