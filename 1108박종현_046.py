# 숫자를 입력받아 총합을 구하는 프로그램을 만드시오.
# 1 2 3 4
# 10
print(sum(list(map(int, input().split()))))

# 만약 아래로 입력을 받는다면
# 단, 5개를 입력받는다.

for _ in range(5):
    n = int(input())
    try:
        temp += n
    except:
        temp = n
print(temp)