#298

list_number  = [52,343,52,52,100]

try:
    number_input = int(input("정수입력"))
    print("{}번쩨 요소, {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해 주세요")
except IndexError:
    print("리스트의 인덱스를 벗어났어요")