def solution(n):
    #원래 append를 사용해서 list로 만들어서 하려고 했음... -> 복잡
    
    # 정수를 문자열로 변환하여 각 자릿수를 리스트에 저장
    digit_list = list(str(n))
    
    # 각 자릿수를 큰 순서로 정렬
    sorted_digits = sorted(digit_list, reverse=True)
    
    # 정렬된 자릿수를 문자열로 결합하고 정수로 변환
    result = int(''.join(sorted_digits))
    
    return result