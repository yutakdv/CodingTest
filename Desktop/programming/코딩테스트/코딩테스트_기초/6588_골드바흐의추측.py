# 문제
# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
#    4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 
# 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.
# 이 추측은 아직도 해결되지 않은 문제이다.
# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

# Code
import sys
input = sys.stdin.readline

MAX = 1000000

# 모든 홀수 소수를 미리 구해놓는다
sieve = [True] * (MAX + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(MAX ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * i, MAX + 1, i):
            sieve[j] = False

odd_primes = [i for i in range(3, MAX + 1, 2) if sieve[i]]
odd_set = set(odd_primes) # set을 통해 해쉬 검색으로 O(1)로 처리
            
while True:
    n = int(input())
    
    if n == 0:
        break
    
    for a in odd_primes:
        if a > n // 2:
            break
        
        if n - a in odd_set:
            b = n - a
            print(f"{n} = {a} + {b}") 
            break
    else:
        print("Goldbach's conjecture is wrong.")
        