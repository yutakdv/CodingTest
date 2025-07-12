# 문제
# N(2 ≤ N ≤ 10,000)개의 섬으로 이루어진 나라가 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.
# 영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다. 
# 물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다.
# 그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다. 만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.
# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.

# Code
import sys
input = sys.stdin.readline
INF = int(1e9)

import heapq
def dijkstra(n, graph, start_point, end_point):
    dist = [0] * (n + 1)
    dist[start_point] = INF
    heap = [(-dist[start_point], start_point)]
    
    while heap:
        weight, edge = heapq.heappop(heap)
        weight = -weight
        
        if edge == end_point:
            return weight
        
        if weight < dist[edge]:
            continue
        
        for vertex, vertex_weight in graph[edge]:
            tmp_weight = min(weight, vertex_weight)
            
            if dist[vertex] < tmp_weight:
                dist[vertex] = tmp_weight
                heapq.heappush(heap, (-dist[vertex], vertex))
    
    return 0

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start_point, end_point = map(int, input().split())

dist = dijkstra(n, graph, start_point, end_point)
print(dist)