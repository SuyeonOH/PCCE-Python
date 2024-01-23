def solution(a, b):
    answer = ''
    day =0
    
    for i in range (1,a) :
        if i in [1,3,5,7,8,10,12] :
            day += 31
        elif i in [4, 6, 9, 11] :
            day += 30
        else :
            day += 29
    # or로 사용했었는데 in으로 사용해야한다
    day += b
    
    cal = {
        0:"THU",
        1:"FRI",
        2:"SAT",
        3:"SUN",
        4:"MON",
        5:"TUE",
        6:"WED"
    }
    
    answer = cal[day % 7] 
    
    return answer