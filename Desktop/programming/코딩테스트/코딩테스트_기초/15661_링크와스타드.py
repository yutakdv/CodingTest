# 문제
# 오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 
# 축구를 하기 위해 모인 사람은 총 N명이다. 이제 스타트 팀과 링크 팀으로 사람들을 나눠야 한다. 두 팀의 인원수는 같지 않아도 되지만, 한 명 이상이어야 한다.

# BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 
# 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. 
# Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

# Code
import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 조합 중 하나씩 확인
min_diff = int(1e9)
for i in range(1, n // 2 + 1):
    for team_a in combinations(range(n), i):
        team_b = list(set(range(n)) - set(team_a))
        
        a_power = 0
        b_power = 0
        
        for x in team_a:
            for y in team_a:
                if x != y:
                    a_power += graph[x][y]
        
        for x in team_b:
            for y in team_b:
                if x != y:
                    b_power += graph[x][y]

        min_diff = min(min_diff, abs(a_power - b_power))

print(min_diff)