"""
자연수 n이 매개변수로 주어집니다.
 n을 3진법 상에서 앞뒤로 뒤집은 후,
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
"""

def solution(n):
    a = ''
    re = 0
    while n > 0:
        a += str(n%3)
        n = int(n/3)
    a = a[::-1]
    for de in range(len(a), 0 , -1):
        re += int(a[de-1]) * (3 ** (de-1))
    print(re)
    return 0


solution(125)