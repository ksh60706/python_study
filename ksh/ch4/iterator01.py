# 변수 선언
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

# reversed_numbers를 출력
# next() 함수 적용
# 하나하나 꺼낼 수 있는 요소를 이터레이터라고 함
print("reversed_numbers : ", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))