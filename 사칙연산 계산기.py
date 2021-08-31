# 사칙연산 계산기 만들기(함수)

# 함수 6개의 원형 정의
def plus(a, b) :
    result = a + b
    return result

def minus(a, b) :
    result = a - b
    return result

def mul(a, b) :
    result = a * b
    return result

def division_f(a, b) :
    result = a / b
    return result

def division_i(a, b) :
    result = a // b
    return result

def remain(a, b) :
    result = a % b
    return result

# 두 개의 숫자 입력 받기
a, b = input("두 개의 숫자를 입력하세요 : ").split()
a = int(a)
b = int(b)

# 연산기호 입력 받기
operator = input("연산자를 입력하세요 : ")

# 조건문을 활용하여 입력된 연산에 해당되는 함수를 호출하여 결과 값 출력
if operator == "+" :
    num = plus(a, b)
    print(f"덧셈 결과 : {num}")
elif operator == "-" :
    if a >= b :
        num = minus(a, b)
        print(f"뺄셈 결과 : {num}")
    else :
        print("뺄셈 결과 : 첫 번째 입력한 수가 두 번째 입력한 수보다 작습니다! 다시 입력해주세요!")
elif operator == "*" :
    num = mul(a, b)
    print(f"곱셈 결과 : {num}")
elif operator == "/" :
    if b != 0 :
        num = division_f(a, b)
        print("실수 나눗셈 결과 : {:.2f}".format(num))
    else :
        print("실수 나눗셈 결과 : 0으로 나눌 수 없습니다! 다시 입력해주세요!")
elif operator == "//" :
    if b != 0 :
        num = division_i(a, b)
        print(f"정수 나눗셈 결과 : {num}")
    else :
        print("정수 나눗셈 결과 : 0으로 나눌 수 없습니다! 다시 입력해주세요!")
elif operator == "%" :
    if b != 0 :
        num = remain(a, b)
        print(f"나머지 나눗셈 결과 : {num}")
    else :
        print(f"나머지 나눗셈 결과 : 0으로 나눌 수 없습니다! 다시 입력해주세요!")
else :
    print("올바른 연산자를 입력해주세요!")