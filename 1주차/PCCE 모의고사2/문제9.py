def solution(serial):
    answer = ''
    gender=serial[0:2]
    dep = serial[2:4]
    teamNum = serial[4:6]
    num=serial[6:8]
    total = 0

    # dictionary 사용 가능
    info = {
        "01":"male",
        "02":"female"
        #...사용할 때는 answer += 'info["02"]'
    }
    #성별
    if gender == "01" :
        answer += "male"
    else :
        answer += "female"
    answer +="/"

    #소속부서
    if dep == "10" :
        answer += "operation"
    elif dep == "11" :
        answer += "sales"
    elif dep =="12" :
        answer += "develop"
    elif dep=="13" :
        answer += "finance"
    elif dep =="14" :
        answer += "law"
    else :
        answer +="research"
    answer +="/"


    #소속 팀 (문자열 -> int -> 문자열로 해서 다시 넣어주기)
    answer += str(int(teamNum))+"team"
    answer +="/"

    #유효성 번호 
    for i in serial[:6] :
        total += int(i)
    
    if total %13 == int(num) :
        answer += "valid"
    else :
        answer += "invalid"
        
    return answer