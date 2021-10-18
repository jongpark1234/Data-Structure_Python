#제어문 : if문

a = 5

if a > 3:
    print('3보다 큼')
elif a > 1:
    print('3보다 작고 1보다 큼') 
else:
    print('1보다 작음')

# 두 숫자를 한줄에 ㅇ비력 받아 더 큰 수를 출력하는 프로그램을 만드시오.
# [입력] 8 3
# [출력] 8
# print(max(list(map(int, input().split()))))
a, b = map(int, input().split())
if a > b:
    print(a)
else:
    print(b)


# [문제] 숫자를 하나 입력 받아 70 이상이면 '최우수'
# 그 외 50이상이면 '우수'
# 그 외 20이상이면 '보통'
# 그 외는 '노력 필요'를 출력하는 프로그램을 만드시오.

a = int(input())
if a >= 70:
    print('최우수')
elif a >= 50:
    print('우수')
elif a >= 20:
    print('보통')
else:
    print('노력 필요')