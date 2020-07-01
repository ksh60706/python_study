# 변수 선언
list_input_a = ["52", "273", "32", "스파이", "103"];

# 반복 적용
list_number = [];
for item in list_input_a:
    # 숫자로 변환하여 리스트에 추가
    try:
        float(item);        #예외가 발생하면 알아서 다음으로 진행되지 않음
        list_number.append(item);       # 예외 없이 통과되면 Append
    except:
        pass;

# 출력
print("{} 내부에 있는 숫자는".format(list_input_a));
print("{} 입니다.".format(list_number));