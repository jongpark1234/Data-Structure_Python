# 문자 압축
strdic = {}
for i in input():
    try:
        strdic[i] += 1
    except KeyError:
        strdic[i] = 1
for i in strdic.keys():
    print(i, strdic[i], sep='', end='')
