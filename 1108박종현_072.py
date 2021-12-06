# 코딩테스트 5
for i in range(1, int(input())):
    mineral = []
    for j in range(1, i):
        if not i % j:
            mineral.append(j)
    if sum(mineral) == i:
        print(i)
