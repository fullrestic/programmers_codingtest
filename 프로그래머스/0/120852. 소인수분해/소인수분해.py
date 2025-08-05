def prime(n) :
    prime_num = []
    for i in range(2, n + 1) :
        check = 1
        for j in range(2, i) :
            if i % j == 0 :
                check = 0
                break
        if check :
            prime_num.append(i)
    return prime_num
        

def solution(n):
    answer = []
    for i in prime(n) :
        if n % i != 0 :
            continue
        else :
            answer.append(i) 
    
    return answer