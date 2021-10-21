from random import *
arr = []

# 로또 번호 생성기
for i in range(6):
    arr.append(randint(1, 46))
print(arr)