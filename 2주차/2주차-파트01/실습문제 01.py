def solution(q, r, code):
    answer = ''
    tmp=[0]*len(code)

    for i in range (len(code)) :
        tmp[i]=i%q
        
        if tmp[i] ==r:
            answer+= code[i]
    
    return answer