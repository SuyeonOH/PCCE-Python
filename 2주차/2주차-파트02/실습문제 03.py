def solution(my_string, overwrite_string, s):
    answer = '' 
    #append를 사용했었는데 append는 list에 추가할 때 쓰는
        
    #s값 전까지는 result에 그대로 넣기
    for i in range (s) :
        answer+=my_string[i]
    #s값이 되는 순간 overwrite넣기
    for j in range (len(overwrite_string)) :
        answer+=overwrite_string[j]
    #s값 이후에는 그대로 my_string 사용
    for q in range (s+len(overwrite_string),len(my_string) ) :
        answer+=my_string[q]
    
    return answer