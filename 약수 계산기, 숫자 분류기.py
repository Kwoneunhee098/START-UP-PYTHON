# 숫자의 약수 구하기 & 숫자 분류하기

# 숫자 입력 받기(양수)
n = int(input("숫자를 입력하세요 : "))

# divisor 함수의 약수를 반환하는 함수
def divisor(n):
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return result

m = divisor(n)

# 출력
print(f"{n}의 약수 : *{m}")

if sum(m) - n == n:
    print(f"숫자 {n}은 완전수입니다")
elif len(m) == 2:
    print(f"숫자 {n}은 소수입니다")
else:
    print(f"숫자 {n}은 기본수입니다")