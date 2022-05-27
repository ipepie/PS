# 프로그래머스 오픈채팅방
# 22/5/26

def solution(record):
    answer = []
    dic = {}
    # 닉네임 변경의 경우 출력 문자열 없음
    # record 탐색하면서 유저 ID에 해당하는 닉네임을 딕셔너리에 저장
    # 나가는 경우 닉네임 없어서 if문 두개에만 추가
    # 덮어쓰면서 가장 마지막에 변경된 닉네임 저장됨
    for x in record:
        if x.startswith("Enter"):
            answer.append(x.split()[1]+"님이 들어왔습니다.")
            dic[x.split()[1]] = x.split()[2]
        elif x.startswith("Leave"):
            answer.append(x.split()[1]+"님이 나갔습니다.")
        else:
            dic[x.split()[1]] = x.split()[2]    
    # 딕셔너리로 부터 id에 해당하는 닉네임 조회해서 변경
    # 처음 저장할 때부터 '님이' 안쓰고 나중에 출력할 때만 추가해도 될듯
    ans = []
    for x in answer:
        ans.append(x.replace(x.split()[0],dic[x.split('님이')[0]]+'님이'))
    
    return ans