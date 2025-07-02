# 문제
# 배열 돌리는 총 6가지 방법
# 1. 상하 반전 | 2. 좌우 반전 | 3. 오른쪽으로 90도 회전 | 4. 왼쪽으로 90도 회전 | 5. 4등분하여 시계 방향 회전 | 6. 1 -> 4, 4 -> 3, 3 -> 2, 2 -> 1

# Code
import sys
input = sys.stdin.readline

def op1(board): # 상하 반전
    return board[::-1]

def op2(board): # 좌우 반전
    return [line[::-1] for line in board]

def op3(board): # 오른쪽으로 90도 회전
    return [list(x)[::-1] for x in zip(*board)]

def op4(board): # 왼쪽으로 90도 회전
    return [list(x)[::-1] for x in zip(*board[::-1])][::-1]

def op5(board): # 4등분하여 시계방향 회전
    row, col = len(board), len(board[0])
    res = [[0] * col for _ in range(row)]
    half_row, half_col = row // 2, col // 2
    
    for i in range(half_row):
        for j in range(half_col):
            res[i][j + half_col] = board[i][j] # 1 -> 2
            res[i + half_row][j + half_col] = board[i][j + half_col] # 2 -> 3
            res[i + half_row][j] = board[i + half_row][j + half_col] # 3 -> 4 
            res[i][j] = board[i + half_row][j] # 4 -> 1

    return res

def op6(board): # 1 -> 4, 4 -> 3, 3 -> 2, 2 -> 1
    row, col = len(board), len(board[0])
    res = [[0] * col for _ in range(row)]
    half_row, half_col = row // 2, col // 2
    
    for i in range(half_row):
        for j in range(half_col):
            res[i + half_row][j] = board[i][j] # 1 -> 4
            res[i + half_row][j + half_col] = board[i + half_row][j] # 4 -> 3
            res[i][j + half_col] = board[i + half_row][j + half_col] # 3 -> 2
            res[i][j] = board[i][j + half_col] # 2 -> 1
    
    return res

n, m, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
op_num = list(map(int, input().split()))

for op in op_num:
    if op == 1:
        board = op1(board)
    elif op == 2:
        board = op2(board)
    elif op == 3:
        board = op3(board)
    elif op == 4:
        board = op4(board)
    elif op == 5:
        board = op5(board)
    elif op == 6:
        board = op6(board)

for row in board:
    print(*row)