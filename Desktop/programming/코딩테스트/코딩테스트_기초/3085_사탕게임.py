# 문제
# 상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.
# 가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 
# 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
# 사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

# Code
import sys
input = sys.stdin.readline

# N 입력
N = int(input())
board = [list(input().strip()) for _ in range(N)]

# 현재 보드에서 가장 긴 연속 사탕 길이 계산
def check(board):
    max_count = 1
    
    # 행 체크
    for i in range(N):
        count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    # 열 체크
    for j in range(N):
        count = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
    
    return max_count

# 인접한 사탕 하나씩 교환해보며 최대값 찾기
answer = 0
for i in range(N):
    for j in range(N):
        # 오른쪽과 교환
        if j + 1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer, check(board))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]  # 원복

        # 아래쪽과 교환
        if i + 1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer, check(board))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]  # 원복

# 결과 출력
print(answer)