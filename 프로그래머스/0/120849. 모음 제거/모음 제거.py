def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    answer = my_string
    
    for i in vowel :
        answer = answer.replace(i, '')
    return answer