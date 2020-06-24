# 리스트에 요소 추가
# append(요소) : 리스트 뒤에 추가
# insert(위치, 요소) : 지정한 위치에 요소 추가

# 리스트를 선언합니다
list_a = [1, 2, 3]

# 리스트 뒤에 요소 추가하기
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가하기
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)

# 한 번에 여러 요소 추가
# extend()
list_a.extend([4, 5, 6])
print(list_a)