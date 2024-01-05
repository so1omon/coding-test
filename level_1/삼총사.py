'''
[날짜] 2024-01-03
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/131705

[메모]
combinations, permutations 사용법 익히기

[Memo]
'''

from itertools import combinations

def solution(number):
    
    return [sum(t) for t in combinations(number, 3)].count(0)
    