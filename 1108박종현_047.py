# dfs
# 방문한 노드는 1로 세팅하고 노드 번호출력
# 인접리스트에서 방문하지 않은 노드를 가지고 dfs 재귀 호출

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],         # 인접행렬
    [2, 3, 8],  # 01100001
    [1, 7],     # 10000010
    [1, 4, 5],  # 10011000
    [3, 5],     # 00101000
    [3, 4],     # 00110000
    [7],        # 00000010
    [2, 6, 8],  # 01000101
    [1, 7]      # 10000010
]
visited = [0] * 9
dfs(graph, 1, visited) # 1번 노드부터 출발