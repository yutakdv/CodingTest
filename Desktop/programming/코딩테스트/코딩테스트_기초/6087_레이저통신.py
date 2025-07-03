# 문제
# 크기가 1×1인 정사각형으로 나누어진 W×H 크기의 지도가 있다. 지도의 각 칸은 빈 칸이거나 벽이며, 두 칸은 'C'로 표시되어 있는 칸이다.
# 'C'로 표시되어 있는 두 칸을 레이저로 통신하기 위해서 설치해야 하는 거울 개수의 최솟값을 구하는 프로그램을 작성하시오. 
# 레이저로 통신한다는 것은 두 칸을 레이저로 연결할 수 있음을 의미한다.
# 레이저는 C에서만 발사할 수 있고, 빈 칸에 거울('/', '\')을 설치해서 방향을 90도 회전시킬 수 있다.
# 아래 그림은 H = 8, W = 7인 경우이고, 빈 칸은 '.', 벽은 '*'로 나타냈다. 
# 왼쪽은 초기 상태, 오른쪽은 최소 개수의 거울을 사용해서 두 'C'를 연결한 것이다.

# Code
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_x, start_y, end_x, end_y):
    q = deque()
    for d in range(4):
        visited[start_x][start_y][d] = 0
        q.append((start_x, start_y, d))
    
    while q:
        x, y, dir = q.popleft()
        
        nx, ny = x + dx[dir], y + dy[dir]
        
        while 0 <= nx < h and 0 <= ny < w and maps[nx][ny] != "*":
            for new_dir in range(4):
                cost = 0 if new_dir == dir else 1
                
                if visited[nx][ny][new_dir] > visited[x][y][dir] + cost:
                    visited[nx][ny][new_dir] = visited[x][y][dir] + cost
                    
                    if cost == 0:
                        q.appendleft((nx, ny, new_dir))
                    else:
                        q.append((nx, ny, new_dir))
            
            nx += dx[dir]
            ny += dy[dir]
    
    return min(visited[end_x][end_y])

w, h = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(h)]
visited = [[[int(1e9)] * 4 for _ in range(w)] for _ in range(h)]
dx, dy = [-1, 1, 0 ,0], [0, 0, -1, 1]

pos = []
for i in range(h):
    for j in range(w):
        if maps[i][j] == "C":
            pos.append([i, j])

(start_x, start_y), (end_x, end_y) = pos
print(bfs(start_x, start_y, end_x, end_y))

