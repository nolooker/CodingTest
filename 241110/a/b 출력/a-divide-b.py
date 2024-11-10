from decimal import Decimal, getcontext

# 소수점 자릿수 설정 (충분히 큰 값으로 설정)
getcontext().prec = 25

# a와 b를 입력 받음
a, b = map(int, input().split())

# 실수 계산
result = Decimal(a) / Decimal(b)

# 소수점 21번째 자리까지 내림
formatted_result = result.quantize(Decimal('1.00000000000000000000'), rounding='ROUND_DOWN')

# 출력
print(formatted_result)