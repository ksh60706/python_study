#263

try:

    number_input_a= int(input("정수입력"))
    print("원의반지름",number_input_a)
    print("원의 둘레",2*3.14*number_input_a)
    print("원의 넓이",3.14*number_input_a*number_input_a)
except:
    print("정수를 입력해달라고 했잖아요")
else:
    print("예외가 발생하였습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")