# 변수 선언
list_number = [52, 273, 32, 72, 100];

# try except 구문으로 예외 처리
try:
    # 숫자 입력
    number_input = int(input("정수 입력: "));
    # 리스트 요소를 출력
    print("{}번째 요소: {}".format(number_input, list_number[number_input]));
    예외.발생       # 잡지 않은 예외 발생
except ValueError as exception:
    #ValueError가 발생하는 경우
    print("정수를 입력해주세요!");
    print("exception: ", exception);
except IndexError as exception:
    #IndexError가 발생하는 경우
    print("리스트의 인덱스를 벗어났어요!");
    print("exception: ", exception);