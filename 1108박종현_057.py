# 최대공약수, 최소공배수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
a, b = map(int, input().split())
print(gcd(a, b), a * b // gcd(a, b))
