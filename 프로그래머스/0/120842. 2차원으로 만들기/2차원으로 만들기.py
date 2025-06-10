def solution(num_list, n):
    answer = []
    
    for i in range(0, len(num_list), n) :
        answer.append(num_list[i : i + n])
    # if len(num_list) % n :
    #     answer.append(num_list[-(len(num_list) % n) :])
        
    return answer