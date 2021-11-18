# 바운드 볼
stack = []
for _ in range(int(input())):
    stack.extend(input().split())
    stack = stack[:-int(input())]
print(' '.join(stack))