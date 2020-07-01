# 변수 선언
list_number = [52, 273, 32, 72, 100];

# try except 구문으로 예외 처리
try:
    # 숫자 입력
    number_input = int(input("정수 입력: "));
    # 리스트 요소를 출력
    print("{}번째 요소: {}".format(number_input, list_number[number_input]));
except Exception as e:
    #예외 객체를 출력
    print("type(exception): ", type(e));
    print("exception:", e);