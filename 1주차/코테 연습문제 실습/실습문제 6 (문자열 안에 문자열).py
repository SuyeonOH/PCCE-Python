def solution(str1, str2):    
    #find 함수 사용 없으면 -1을 반납
    #처음 발생한 위치만 알려줌

# string = "Hello, Hello, World!"

# "Hello"의 첫 번째 발생 위치 찾기
# index = string.find("Hello")
# print(index)  출력: 0

# 두 번째 "Hello"의 시작 위치 찾기
# index = string.find("Hello", 1)
# print(index)  # 출력: 7


    if str1.find(str2) != -1:
        return 1
    else :
        return 2