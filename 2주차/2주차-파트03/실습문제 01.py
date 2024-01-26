def solution(before, after):
    
    #가지고 있는 알파벳이 같으면 삭제하는 코드를 짜려고 했음 -> 복잡...

    # before 문자열을 정렬하여 순서를 변경한 결과와 after가 같은지 확인
    sorted_before = ''.join(sorted(before))
    sorted_after=''.join(sorted(after))

    if sorted_before == sorted_after:
        return 1
    else:
        return 0
    