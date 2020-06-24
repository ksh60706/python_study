list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

# 제거 방법[1] - del
# del 리스트명[인덱스]
del list_a[1]
print("del list_a[1]:", list_a)

# 제거 방법[2] - pop
# 리스트명.pop(인덱스)
# 인덱스를 작성하지 않으면 마지막 요소가 제거됨
list_a.pop(2)
print("pop(2):", list_a)