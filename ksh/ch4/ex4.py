# 대괄호 안에 음수를 넣어 뒤에서부터 요소 선택 가능
list_a = [273, 32, 103, "문자열", True, False]
print(list_a[-1])
print(list_a[-2])
print(list_a[-3])


# 이중으로 사용
print(list_a[3])
print(list_a[3][0])

# 리스트 안에 리스트 사용
list_b = [[1,2,3],[4,5,6],[7,8,9]]
print(list_b[1])
print(list_b[1][1])