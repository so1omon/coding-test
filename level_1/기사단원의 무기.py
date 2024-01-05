'''
[날짜] 2024-01-04
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/136798

[메모] 약수의 개수 효율적으로 구하기
'''

def divisor_cnt(num):
    cnt = 0
    for i in range(1, int(num**(1/2))+1):
        if num%i==0:
            cnt+= 1 if i**2== num else 2
    return cnt

def solution(number, limit, power):
    answer = 0
    
    
    for num in range(1, number+1):
        result = divisor_cnt(num)
        
        if result > limit:
            result = power
        
        answer+=result
    
    
    return answer