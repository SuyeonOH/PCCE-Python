def solution(n):
    answer = 0
    
    while n!=0 :
        list.append(n%10)
        n//10
    
    for i in range(len(list)) :
        if (list[i]<list[i+1]) :
            tmp = list[i]
            list[i]=list[i+1]
            list[i+1]=tmp
    return answer