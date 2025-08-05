def solution(my_string):
    answer = ''
    my_set = list(set(my_string))
    for st in my_string :
        for s in my_set : 
            if s == st :
                answer += s
                my_set.remove(s)
                break
    return answer