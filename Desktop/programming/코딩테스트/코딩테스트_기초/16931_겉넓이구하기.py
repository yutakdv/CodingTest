# 문제
# 크기가 N×M인 종이가 있고, 종이는 1×1크기의 칸으로 나누어져 있다. 이 종이의 각 칸 위에 1×1×1 크기의 정육면체를 놓아 3차원 도형을 만들었다.
# 종이의 각 칸에 놓인 정육면체의 개수가 주어졌을 때, 이 도형의 겉넓이를 구하는 프로그램을 작성하시오.

# Code
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
total = 0

for i in range(n):
    for j in range(m):
        h = grid[i][j]
        
        if h > 0:
            total += 2
            
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                
                if 0 <= nx < n and 0 <= ny < m:
                    neighbor = grid[nx][ny]
                else:
                    neighbor = 0 
            
                exposed = max(h - neighbor, 0)
                total += exposed

print(total)