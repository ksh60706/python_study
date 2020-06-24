# in 키워드
# 딕셔너리 내부에 키가 있는지 없는지 확인할 때 사용

# 딕셔너리 선언
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 사용자로부터 입력을 받습니다
key = input("> 접근하고자 하는 키: ")

# 출력합니다
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")