# 숫자로만 구성되어있을 때
try:
    # 숫자로 변환
    number_input_a = int(input("정수 입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("정수를 입력하지 않았음3")
else:
    print("예외 발생 안함")
finally:
    print("끝남")