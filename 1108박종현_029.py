# [문제] 주어진 알파벳을 오름차순으로 정렬하라
arr = ['b', 'c', 'a', 'f', 't', 'e']
# 리스트 요소 중 아스키 코드값이 가장 작은 / 큰 알파벳을 출력하시오.
arr.sort()
print(arr[0]) # 맨 앞 요소
print(arr[-1]) # 맨 뒤 요소

# 역순으로 출력, 내림차순으로 정렬하라.
arr.sort(reverse=1)
print(arr)

# [문제] 주어진 점수 리스트에서 최고점과 최저점을 출력하시오.
score = [55, 78, 99, 34, 87]
# score.sort()
# print(arr[0], arr[-1])
print(min(score), max(score))