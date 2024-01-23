#내가 풀려고 했던 방법.. -> 각 자리의 숫자 문자열을 각각 비교하며 맞는 것이 있으면 새로운 변수에 넣어서
#그 변수를 조합해서 최대의 수를 만드는 게 어떨까~ 생각을 했음 -> 근데 그거 어떻게 할건데?
#그래서 찾아본 다른 방법 
def solution (X, Y):
    count_X = [0]*10
    count_Y = [0]*10

    for digit in X:
        count_X[int(digit)] +=1
    
    for digit in Y:
        count_Y[int(digit)] +=1

    for digit in range(9,-1,-1):
        for _ in range (min(count_X[digit], count_Y[digit]) ):
            result +=str(digit)

    if result and all (char == '0' for char in result): #result가 비어있지 않고 모든 문자 '0' 이 true 
        return "0"
    
    if not result:
        return "-1"
    
    return result