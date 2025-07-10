# 문제
# 세로 두 줄, 가로로 N개의 칸으로 이루어진 표가 있다. 첫째 줄의 각 칸에는 정수 1, 2, …, N이 차례대로 들어 있고 둘째 줄의 각 칸에는 1이상 N이하인 정수가 들어 있다. 
# 첫째 줄에서 숫자를 적절히 뽑으면, 그 뽑힌 정수들이 이루는 집합과, 뽑힌 정수들의 바로 밑의 둘째 줄에 들어있는 정수들이 이루는 집합이 일치한다. 
# 이러한 조건을 만족시키도록 정수들을 뽑되, 최대로 많이 뽑는 방법을 찾는 프로그램을 작성하시오. 

# Code
import sys
input = sys.stdin.readline

def dfs(x, path):
    visited[x] = True
    path.append(x)
    next_node = graph[x]
    
    if not visited[next_node]:
        dfs(next_node, path)
    elif not finished[next_node]:
        idx = path.index(next_node)
        result.extend(path[idx:])
    
    finished[x] = True

n = int(input())
graph = [0] * (n + 1)
for i in range(1, n + 1):
    graph[i] = int(input())
    
visited = [False] * (n + 1)
finished = [False] * (n + 1)

result = []
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, [])    

result.sort()
print(len(result))
for num in result:
    print(num)