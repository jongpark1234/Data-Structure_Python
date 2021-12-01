result = ''
for i in input():
    if i.isdecimal():
        result += i
print(int(result) + 5)