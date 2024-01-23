# def solution(text, anagram, sw):
#     answer = ''
#     if sw==True:
#         for i in range (len(anagram)) :
#             n=anagram[i]
#             answer[n]=text[i] 처음에 이런 식으로 접근함 -> TypeError: 'str' object does not support item assignment 가 뜸, 문자열은 "불변 타입"
#           즉 문자열은 할당, 이동이 불가능함
def solution(text, anagram, sw):
    arr=[0]*len(text)
    
    if sw==True:
        for i in range (len(anagram)):
            arr[anagram[i]]=text[i]
            
    else:
        for i in range (len(anagram)):
            arr[i]=text[anagram[i]]
            
    answer = ''.join(arr)
    
    return answer