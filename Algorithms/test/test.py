# 테스트용
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	
computers = [[]] + computers
for i in computers:
    for a,b in enumerate(i):
        if b == 1:
            i[a] = a+1
print(computers)