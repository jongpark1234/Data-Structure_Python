from random import *
arr = []

# 로또 번호 생성기
for i in range(6):
    arr.append(randint(1, 46))
print(arr)

# [문제] arr에 있는 데이터 중 가장 큰 값을 반환하시오.
print(max(arr))

# [문제] 리스트에서 두번째 큰 값을 출력하시오.
arr.sort(reverse=True)
print(arr[1])
