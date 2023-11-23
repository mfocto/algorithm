"""
문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
예를 들어 s가 "a234"이면 False를 리턴하고
"1234"라면 True를 리턴하면 됩니다.
--------------------------------------------------------------------------------------
@ s는 길이 1 이상, 길이 8 이하인 문자열입니다.
@ s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.
"""

# ---------------------------------------
# def solution(s):
#     answer = True
#
#     for i in s:
#         if not 48 <= ord(i) <= 57:
#             answer = False
#
#     return answer
#   test 5. 6. 28. 89 실패(문자열 길이 검사 안함)
# ------------------------------------------

def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False

    for i in s:
        if not 48 <= ord(i) <= 57:
            answer = False

    return answer


# -------------
# 입출력 예
# -------------
solution('a234')
solution('1234')



