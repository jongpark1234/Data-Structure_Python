# 이진수 1의 갯수와 큰 것 중에 작은 수 찾기
a = int(input())
count = bin(a)[2:].count('1')
while True:
    a += 1
    if bin(a)[2:].count('1') == count:
        print(a)
        break
