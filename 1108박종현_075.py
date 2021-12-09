a = input()
num = a
while True:
    temp = 0
    for i in num:
        temp += int(i) ** 2
    if str(temp) == a:
        print('Unhappy Number')
        break
    if temp == 1:
        print('Happy Number')
        break
    num = str(temp)
