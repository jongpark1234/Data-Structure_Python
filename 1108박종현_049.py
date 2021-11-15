# 4 5
# 00110
# 00011
# 11111
# 00000
# 출력
# 3
# 첫 번째 줄에 땅 크기 N, M 1 <= N, M <= 1000
# 두 번째 줄에 N + 1 번째 줄까지 땅에 대한 표시이다.
# 0은 물 구덩이, 1은 밟아도 무너지지 않는 땅이다.
# 전체 땅 속에서 물 구덩이 개수를 출력한다.

n, m = map(int, input().split()) # n 과 m 을 입력받음

graph = [] # graph 라는 리스트 선언

for i in range(n): # n 번 반복
    graph.append(list(map(int, input()))) # graph 라는 리스트에 맵을 공백 없이 입력받음

def puddle(x, y): # puddle 함수 선언
    if x <= -1 or x >= n or y <= -1 or y >= m: # 만약 맵 인덱스를 벗어난다면
        return False # False 반환
    if graph[x][y] == 0: # 만약 찾은 인덱스가 0 (구덩이) 라면
        graph[x][y] = 1 # 1로 변환시킴
        puddle(x - 1, y) # 상, 하, 좌, 우 탐색
        puddle(x, y - 1)
        puddle(x + 1, y)
        puddle(x, y + 1)  
        return True # True 를 반환
    else: # 인덱스가 1 (벽) 이라면
        return False # False 반환
count = 0 # 물 웅덩이의 개수 count 변수 선언
for i in range(n): # n 번 반복
    for j in range(m): # m 번 반복
        if puddle(i, j) == True: # 만약 이 인덱스가 0 ( 물웅덩이 ) 라면
            count += 1 # 물웅덩이의 개수를 1 증가시키고 해당 인덱스와 연결된 모든 0 (웅덩이) 를 1 로 변환시킴.
print(count) # 물 웅덩이의 개수 (count) 출력.
