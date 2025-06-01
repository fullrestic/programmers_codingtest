def solution(n):
    root = n ** 0.5
    if root - int(root) == 0 :
        answer = 1
    else : 
        answer = 2
    return answer