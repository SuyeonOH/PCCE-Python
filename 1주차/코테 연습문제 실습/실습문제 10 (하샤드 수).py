def solution(x):
    num=0
    #temp를 통해 x를 저장해두어야함
    temp=x
    
    while temp>0 :
        num += temp%10
        temp//=10
        
    if x % num == 0 :
        answer= True
    else :
        answer=False
    
    return answer