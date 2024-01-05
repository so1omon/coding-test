'''
[날짜] 2024-01-04
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/72410

[메모] 
정규 표현식 복습
strip

'.'이 연속으로 나오는 경우 제거하기 -> st = re.sub('\.+', '.', st)
'''


import re

def solution(new_id):
    new_id = re.sub(r'[^a-z0-9\-\_\.]',"", new_id.lower())
    new_id = new_id.replace("..", ".").replace("..", ".").replace("..", ".").replace("..", ".").strip(".")
    
    if len(new_id)==0:
        new_id = "a"
    
    if len(new_id)>=16:
        new_id = new_id[:15].strip(".")
    
    while len(new_id)<3:
        new_id+=new_id[-1]
    
    return new_id


print(solution("3................3"))
