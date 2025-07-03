# 배열을 각 테두리마다 반시계 방향으로 회전하는 문제

# Code
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

layers = min(n, m) // 2

for layer in range(layers):
    top, left = layer, layer
    bottom, right = n - layer - 1, m - layer - 1
    
    elements = []
    # 각 레이어마다 Top, right, bottom, left의 값을 저장해둠

    # 1. Top
    for i in range(left, right):
        elements.append(board[top][i])
    
    # 2. Right
    for i in range(top, bottom):
        elements.append(board[i][right])
    
    # 3. Bottom
    for i in range(right, left, -1):
        elements.append(board[bottom][i])
    
    # 4. Left
    for i in range(bottom, top, -1):
        elements.append(board[i][left])
        
    # Rotate
    rotate = r % len(elements)
    rotated = elements[rotate:] + elements[:rotate]
    
    idx = 0
    # Top
    for i in range(left, right):
        board[top][i] = rotated[idx]
        idx += 1
    
    # Right
    for i in range(top, bottom):
        board[i][right] = rotated[idx]
        idx += 1
    
    # Bottom
    for i in range(right, left, -1):
        board[bottom][i] = rotated[idx]
        idx += 1
    
    # Left
    for i in range(bottom, top, -1):
        board[i][left] = rotated[idx]
        idx += 1
        
for row in board:
    print(*row)