#255

power = lambda x: x * x
under_3 = lambda x: x <3

list_input_a = [1,2,3,4,5]

output_a = map(power, list_input_a)
print("함수의 실행결과")
print("map(power,list_input_a",output_a)
print("map(power,list_input_a",list(output_a))
print()

output_b = filter(under_3,list_input_a)
print("filter함수의 실행결과")
print("filter",output_b)
print("list_input_a",list(output_b))
