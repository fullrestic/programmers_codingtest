def solution(numbers, k):
    num = -2
    for i in range(k) :
        num += 2
    return numbers[num % len(numbers)]