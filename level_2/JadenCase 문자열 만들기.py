'''
[날짜] 2024-01-05
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/12951#

[메모] 
공백 여러 개 있는 문자 안에서 split()을 대신할 방법 찾기
capitalize() 함수
'''

import re

def solution(s):
    answer = []
    new_s=s.split(" ")
    #공백이 들어갈 경우 대비(ex. 3people     Unfollwed Me)
    #split()말고, split(" ")이라고 공백 하나만 들어가게 할 것
    
    for x in new_s:
        answer.append(x.lower().capitalize())
    return ' '.join(answer)
    
    return s
