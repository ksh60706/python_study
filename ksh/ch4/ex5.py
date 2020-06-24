# 리스트 연결 연산자와 요소 추가의 차이
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# 연결 연산자 + 를 이용하면 기존 데이터에는 변화 x (비파괴적 처리)
print(list_a+list_b)

# extend()를 이용해서 연결하면 기존 데이터에 변화가 있음 (파괴적 처리)
list_a.extend(list_b)
print(list_a)