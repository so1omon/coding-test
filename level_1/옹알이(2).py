'''
[날짜] 2024-01-04
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/133499#qna

[메모] 반례 생각하며 다시 풀어보기
'''
def rep(word):
    keywords = ["aya", "ye", "woo", "ma"]
    
    for key in keywords:
        extend = key*2
        if extend in word:
            # print("중복발견: ", word)
            return False
    for key in keywords:
        word = word.replace(key, "*")
    word = word.replace('*', "")
    if word!="":
        return False
    return True
    
def solution(babbling):
    answer = 0
    
    for b in babbling:
        result = rep(b)
        answer+=1 if result else 0
    
    
    return answer
    
    
    for num in range(1, number+1):
        result = divisor_cnt(num)
        
        if result > limit:
            result = power
        
        answer+=result
    
    
    return answer