def Hello():
    print('Hello')
    print('KIM')
# 파이썬에서는 들여쓰기가 중요하다. 보통 4칸 들여쓰기 사용


# 함수 출력하기, 함수 실행하기
Hello()

if __name__ == '__main__':
    Hello()

# [문제] 'KIM'이라는 매개변수 값을 넘겨줄 때
# 'Hi, KIM'이 출력되도록 하시오.
# Hello('KIM')

def Hello(name):
    print(f'Hi, {name}')

Hello('Kim')

def info(name, address, phone):
    print(f'제 이름은 {name}이고, 주소는 {address}입니다.'\
        f'제 전화번호는 {phone}에요.')
info('JongPark', '대구시 동구', '010-0000-0000')

# [문제] 자신이 좋아하는 가수 이름을 3개 입력받고 출력하는 함수 만들기
# 함수이름 : singer(a, b, c)

def singer(a, b, c):
    print(a, b, c)
a, b, c = map(str, input('좋아하는 가수 3명 입력 : ').split())
singer(a, b, c)