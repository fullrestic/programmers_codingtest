def solution(a, b):
    mul = 2 * a * b
    cross = int(str(a) + str(b))
    if mul > cross : return mul
    else : return cross