# 숫자를 입력받음
user_input_a = input("정수 입력> ")

# 숫자로만 구성되어있을 때
try:
    # 숫자로 변환
    number_input_a = int(user_input_a)
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("정수를 입력하지 않았음3")