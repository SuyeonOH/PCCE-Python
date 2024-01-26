def solution(t, p):
    answer = 0
    list = [0]*(len(t)-len(p)+1)
    
    #t를 p의 길이만큼 자른 것을 배열에 넣어두기 
    for i in range (len(t)-len(p)+1) : #이 부분 생각 못했음..
        list[i]=int(t[i:i+len(p)]) #슬라이싱 사용
        if int(p)>= list[i] :    #배열 돌리면서 수 비교 후 answer++   
            answer+=1
    
    return answer