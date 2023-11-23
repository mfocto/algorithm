"""
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
 -------------------------------------------------------------------------------
@ 두 수는 1이상 1000000이하의 자연수입니다.
"""

def solution(n, m):
    answer = []
    gres = gcd(n, m)
    answer.append(gres)
    answer.append(lcm(n, m, gres))
    return answer


# 최대공약수
def gcd(n, m):
    maxnum = max(n, m)
    result = 0

    for i in range(1, maxnum):
        if n % i == 0 and m % i == 0:
            result = i

    return result

# 최소공배수
def lcm(n, m, gcd):
    return n * m / gcd


print(solution(3, 12))
print(solution(1, 10))