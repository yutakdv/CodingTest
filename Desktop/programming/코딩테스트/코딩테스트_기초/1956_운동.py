# 문제
# V개의 마을와 E개의 도로로 구성되어 있는 도시가 있다. 도로는 마을과 마을 사이에 놓여 있으며, 일방 통행 도로이다. 
# 마을에는 편의상 1번부터 V번까지 번호가 매겨져 있다고 하자.
# 당신은 도로를 따라 운동을 하기 위한 경로를 찾으려고 한다. 운동을 한 후에는 다시 시작점으로 돌아오는 것이 좋기 때문에, 우리는 사이클을 찾기를 원한다. 
# 단, 당신은 운동을 매우 귀찮아하므로, 사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.
# 도로의 정보가 주어졌을 때, 도로의 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오. 두 마을을 왕복하는 경우도 사이클에 포함됨에 주의한다.

# Code
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
dist = [[INF] * (V + 1) for _ in range((V + 1))]

for _ in range(E):
    u, v, w = map(int, input().split())
    dist[u][v] = min(dist[u][v], w)
    
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = min(dist[i][i] for i in range(1, V + 1))
print(ans if ans < INF else -1)