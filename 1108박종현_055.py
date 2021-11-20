# 1이 될때까지
n, k = map(int, input().split())
while n != 1:
    try: cnt += 1
    except NameError: cnt = 1
    n = n - 1 if n % k or n < k else n // k
print(cnt + 1)