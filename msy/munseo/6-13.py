#295

try:

    number_input_a = int(input("정수입력"))

    print("원의 반지름",number_input_a)
    print("원의 둘레",3.14*2*number_input_a)
    print("원의 넓이",3.14*number_input_a*number_input_a)
except Exception as exception:
    print("typr(exception)",type(exception))
    print("exception",exception)