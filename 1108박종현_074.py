# 진법변환 다시 10진수로
key = {'b': 2, 'o': 8, 'x': 16}
num = input()
print(int(num[2:], key[num[1]]))
