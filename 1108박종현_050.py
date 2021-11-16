# 시간 속의 숫자 찾기
for i in range(int(input()) + 1):
	for j in range(60):
		for k in range(60):
			try:
				cnt += str(i).count('3') + str(j).count('3') + str(k).count('3')
			except NameError:
				cnt = str(i).count('3') + str(j).count('3') + str(k).count('3')
print(cnt)