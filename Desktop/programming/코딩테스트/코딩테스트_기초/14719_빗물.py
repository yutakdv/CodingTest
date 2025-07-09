# 문제 
# 2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.
# 비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?

# Code
import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

result = 0
for i in range(1, w - 1):
    left_max = max(heights[:i])
    right_max = max(heights[i+1:])
    min_height = min(left_max, right_max)
    
    if heights[i] < min_height:
        result += min_height - heights[i]

print(result)