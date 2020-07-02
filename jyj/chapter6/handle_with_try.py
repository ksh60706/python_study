# try except 구문으로 예외 처리
try:
    # 숫자로 변환
    number_input_a = int(input("정수 입력: "));      # 예외가 발생할 가능이 있는 구문
    # 출력
    print("원의 반지름: ", number_input_a);
    print("원의 둘레: ", 2 * 3.14 * number_input_a);
    print("원의 넓이: ", 3.14 * number_input_a * number_input_a);
except:
    print("이상해!");       # 예외가 발생했을 때 실행할 구문
