def solution(n, numlist):
    answer = list(filter(lambda x : x % n == 0, numlist))
    return answer