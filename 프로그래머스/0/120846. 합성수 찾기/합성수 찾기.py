def solution(n):
    cnt = 0
    for i in range(1, n + 1) :
        deno_cnt = 0
        for j in range(1, int(i**0.5) + 1) :
            if i % j == 0 : 
                if j * j == i : deno_cnt += 1
                else : deno_cnt += 2
            if deno_cnt >= 3 : 
                cnt += 1
                break
    return cnt