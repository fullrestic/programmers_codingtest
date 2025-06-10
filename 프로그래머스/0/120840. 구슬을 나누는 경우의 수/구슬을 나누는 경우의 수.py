def solution(balls, share):
    answer = 1
    for i in range(1, share + 1) : 
        answer *= balls
        answer /= i
        balls -= 1
        
    return answer