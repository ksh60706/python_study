# 함수 선언
power = lambda item: item * item
under_3 = lambda item : item < 3
test = lambda : print('hi')

# 변수 선언
list_input_a = [1, 2, 3, 4, 5]

# map() 함수 사용
output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

# filter 함수 사용
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, output_b):", output_b)
print("filter(under_3, output_b):", list(output_b))

test()


print(enumerate())