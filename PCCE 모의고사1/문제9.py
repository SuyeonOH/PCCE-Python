def solution(num_list):
    answer = []
       
    for num in num_list :
        is_demical=True
        
        for i in range(2,num): 
            if num%i == 0:
                answer.append(False)
                is_demical=False
                break 
        if is_demical==True:
            answer.append(True)
            
    return answer