"""
문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
각 단어는 하나 이상의 공백문자로 구분되어 있습니다.
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
---------------------------------------------------------------------------------------------------------
@ 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
@ 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
"""

def solution(s):
    answer = ''
    idx = 0
    for val in s:
        # 공백일 경우 인덱스 초기화
        if val == ' ':
            idx = 0
            answer += ' '
            continue
        # 0일 경우 나누면 에러 발생하므로 따로 조건 분리
        elif idx == 0:
            answer += val.upper()
            idx += 1
        # 짝수면 대문자
        elif idx % 2 == 0:
            answer += val.upper()
            idx += 1
        # 홀수면 소문자
        else:
            answer += val.lower()
            idx += 1

    return answer


print(solution("try hello world"))