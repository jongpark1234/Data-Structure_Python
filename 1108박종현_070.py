# 코딩테스트 3
alphabet = {}
for i in input():
    try:
        alphabet[i] += 1
    except KeyError:
        alphabet[i] = 1
for i in alphabet.keys():
    print(i + str(alphabet[i]), end='')
