# a, b 배열 인덱스
print(*sorted(list(input().split()), key= lambda x: (int(x[1:]), x[0])))
