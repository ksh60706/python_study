# 변수를 선언
counter = 0


# global 키워드
# 함수 내부에서 외부에 있는 변수를 참조하려고할 때 사용함.
# 함수를 선언
def fibonacci(n):
    # 어떤 피보나치 수를 구하는지 출력
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter += 1
    #피보나치 수를 구합니다.
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(35)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))
