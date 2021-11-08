from collections import deque
def bfs(start):
    queue = deque([start]) # 덱 선언
    visited[start] = True # 정복 여부 True 설정
    while queue: # 덱이 빌 때 까지 반복함
        v = queue.popleft() # 덱에서 하나를 빼냄
        print(v, end=' ') # 출력
        for i in graph[v]: 
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]
visited = [False] * 9
bfs(1)