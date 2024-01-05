'''
[날짜] 2024-01-05
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/150370

[메모] 
날짜 함수 

문자를 지정한 형식에 맞게 파싱하여 날짜로 datetime.datetime.strptime(str, format)
날짜를 지정한 형식에 맞게 파싱하여 문자로 datetime.datetime.strftime(date, format)

날짜 format 공부

timedelta vs from dateutil.relativedelta import relativedelta

cf) 파이썬에서 외부 라이브러리 얼마나 쓸 수 있는지 알아보기
'''
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
from datetime import datetime
from dateutil.relativedelta import relativedelta


def solution(today, terms, privacies):
    answer = []

    table = {key: relativedelta(months = int(value)) for key, value in [term.split() for term in terms]}

    dateformat = "%Y.%m.%d"
    currentDate= datetime.strptime(today, dateformat)

    for i, privacy in enumerate(privacies):
        targetDate, term = privacy.split()
        targetDate = datetime.strptime(targetDate, dateformat)
        term = table[term]

        if targetDate + term <= currentDate:
            answer.append(i+1)

    return answer
