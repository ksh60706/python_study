# try except 구문으로 예외 처리
try:
    # 숫자로 변환
    number_input_a = int(input("정수 입력: "));
    # 출력
    print("원의 반지름: ", number_input_a);
    print("원의 둘레: ", 2 * 3.14 * number_input_a);
    print("원의 넓이: ", 3.14 * number_input_a * number_input_a);
except:
    print("정수를 입력해야지!");
else:
    print("정수를 입력했구나!");
finally:
    print("일단 실행은 했어!");