# 문제
# 인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 
# 승원이는 연구소의 특정 위치에 바이러스 M개를 놓을 것이고, 승원이의 신호와 동시에 바이러스는 퍼지게 된다.
# 연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 
# 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.
# 일부 빈 칸은 바이러스를 놓을 수 있는 칸이다. 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.

# Code
import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

def bfs(comb):
    visited = [[-1] * n for _ in range(n)]
    max_time = 0
    q = deque()
    
    for x, y in comb:
        q.append((x, y))
        visited[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < n:
                if lab[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    max_time = max(max_time, visited[nx][ny])
                    q.append((nx, ny))

    for i in range(n):
        for j in range(n):
            if lab[i][j] != 1:
                if visited[i][j] == -1:
                    return int(1e9)
        
    return max_time

# 0 : 빈 칸, 1 : 벽, 2 : 바이러스 놓을 수 있는 칸
n, m = map(int, input().split()) # n : 연구소 사이즈, m : 바이러스 총 개수
lab = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

virus_pos = []
# 바이러스 놓을 수 있는 칸 체크
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus_pos.append((i, j))

min_time = int(1e9)
for comb in combinations(virus_pos, m):
    time = bfs(comb)
    
    min_time = min(min_time, time)
        

print(min_time if min_time != int(1e9) else -1)