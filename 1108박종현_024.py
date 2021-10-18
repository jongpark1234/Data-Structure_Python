# 문자열 입력하기
name = input('이름을 입력하세요 : ') # 문자열 입력 받기 printf(), scanf()
print('My name is', name) # ,로 문자열 연결
print('My name is ' +  name) # +로 문자열 연결

a = input('a = ') # 문자열 입력
b = input('b = ')
a = int(a) # 문자열을 정수로 변환
b = int(b)
# a = int(input('a = ')) # 이 형태로 보통 사용

print('-' * 10) # 기호 10회 반복
print(a + b)
print('-' * 10) # 기호 10회 반복

# [문제] 두 숫자를 입력받아 사칙연산하는 프로그램을 만드시오.
a, b = map(int, input('두 숫자 입력 : ').split())
print(a + b, a - b, a * b, a / b, sep = '\n')