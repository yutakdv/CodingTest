# 문제
# 대략 위의 그림과 같이 생긴 성곽이 있다. 굵은 선은 벽을 나타내고, 점선은 벽이 없어서 지나다닐 수 있는 통로를 나타낸다. 
# 이러한 형태의 성의 지도를 입력받아서 다음을 계산하는 프로그램을 작성하시오.

# 1. 이 성에 있는 방의 개수
# 2. 가장 넓은 방의 넓이
# 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기

# 1 : 서쪽, 2 : 북쪽, 4 : 동쪽, 8 : 남쪽 // 2진수 비트

# Code
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, room_id):
    q = deque([(x, y)])
    visited[x][y] = room_id
    size = 1
    
    while q:
        x, y = q.popleft()
        
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            
            if 0 <= nx < m and 0 <= ny < n:
                if not (castle[x][y] & bitmask[dir]) and visited[nx][ny] == -1:
                    visited[nx][ny] = room_id
                    size += 1
                    q.append([nx, ny])
    
    return size

n, m = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(m)]

# [서, 북, 동, 남]
bitmask = [1, 2, 4, 8]

# 0: 서, 1: 북, 2: 동, 3: 남
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

visited = [[-1] * n for _ in range(m)]
room_size = []
room_id = 0

# 1. 이 성에 있는 방의 개수 & 2. 가장 넓은 방의 크기
for i in range(m):
    for j in range(n):
        if visited[i][j] == -1:
            size = bfs(i, j, room_id)
            room_size.append(size)
            room_id += 1

print(room_id)
print(max(room_size))

# 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
max_merge = 0
for i in range(m):
    for j in range(n):
        for d in range(4):
            ni, nj = i + dx[d], j + dy[d]
            
            if 0 <= ni < m and 0 <= nj < n:
                if (castle[i][j] & bitmask[d]) and (visited[i][j] != visited[ni][nj]):
                    combined = room_size[visited[i][j]] + room_size[visited[ni][nj]]
                    max_merge = max(max_merge, combined)

print(max_merge)