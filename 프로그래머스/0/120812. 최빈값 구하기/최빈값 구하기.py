def solution(array):
    array_set = set(array)
    mode = -1
    max_cnt = 0
    
    for i in list(array_set) :
        cnt = array.count(i)
        if cnt > max_cnt :
            mode = i
            max_cnt = cnt
        elif cnt == max_cnt :
            mode = -1
    return mode