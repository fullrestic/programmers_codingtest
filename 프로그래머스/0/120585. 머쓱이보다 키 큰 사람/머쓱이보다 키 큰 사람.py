def solution(array, height):
    cnt = 0
    for i in reversed(sorted(array)) :
        if i <= height : 
            break
        cnt += 1
    return cnt