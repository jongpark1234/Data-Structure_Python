# 소수 판별하기
def isprime(num):
    if num == 1:
    	return False
    for i in range(2, int(num ** 0.5) + 1):
    	if not num % i:
    		return False
    return True
print(isprime(int(input())))
