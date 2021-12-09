# 올바르게 입력된 괄호 문장을 찾아라
stack = []
Open, Close = 0, 0
for i in input():
    if i == '(':
        Open += 1
    elif i == ')':
        Close += 1
    if Open > 0 and Close > 0:
        Open -= 1
        Close -= 1
    if Open < Close:
        print('False')
        exit(0)
if Open or Close:
    print('False')
else:
    print('True')
