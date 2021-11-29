# 이상한 정렬
numlist = list(map(int, input().split()))
print(*[i for i in numlist if i < 0], *[j for j in numlist if j > 0])
