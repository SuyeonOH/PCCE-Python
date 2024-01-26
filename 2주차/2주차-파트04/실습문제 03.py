def solution(numbers):    
    #문자열로 취급 [...]: 리스트 컴프리헨션의 표현식 각 반복된 값에 대해 새로운 리스트를 생성
    numbers = [str(x) for x in numbers]
    
    # for i in range(len(numbers)):
    #     numbers[i]=str(numbers[i])
    
    numbers.sort(key=lambda x : (x*4)[:4], reverse= True)

    if numbers[0]=='0' :
        answer = '0'
        
    else :
        answer=''.join(numbers)

    return answer