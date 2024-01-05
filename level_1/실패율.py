'''
[날짜] 2024-01-04
[링크] https://school.programmers.co.kr/learn/courses/30/lessons/42889

[메모] 다시 풀어보기
'''

def solution(N, stages):
    '''
    실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    return : 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열
    만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
    스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
    '''
    answer = []
    
    total = [0 for _ in range(N+1)]
    
    # total[i] : i번째 스테이지를 클리어한 사람
    # rest[i] : i번째 스테이지에 머무른 사람
    
    for stage in stages:
        total[stage-1]+=1
        
    rest = list(total)
    for i in list(reversed(range(len(total)-1))):
        total[i] +=total[i+1]
        
    fails = dict()
    for i in range(0, N): # 1부터 500까지 돌면서 스테이지 계산
        fail_rate = rest[i] / total[i] if total[i]!=0 else 0.0
        fails[i+1] = fail_rate
    
    return [x[0] for x in sorted(fails.items(), key = lambda x : -x[1])]
    
    for num in range(1, number+1):
        result = divisor_cnt(num)
        
        if result > limit:
            result = power
        
        answer+=result
    
    
    return answer