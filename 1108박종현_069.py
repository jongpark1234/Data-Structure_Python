# 코딩테스트 2
numlist = list(map(int, input().split()))
print(*[i for i in numlist if i < 0], *[i for i in numlist if i > 0])
