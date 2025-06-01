def gcd(num1, num2) : 
    while num2 :
        num1, num2 = num2, num1 % num2 
    return num1

def lcm(num1, num2) :
    return num1 * num2 // gcd(num1, num2)
    
def solution(numer1, denom1, numer2, denom2):
    denom_lcm = lcm(denom1, denom2)
    numer_sum = numer1 * denom_lcm // denom1 + numer2 * denom_lcm // denom2
    
    result_gcd = gcd(numer_sum, denom_lcm)
    answer = [numer_sum // result_gcd , denom_lcm // result_gcd]
    return answer