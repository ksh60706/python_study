# 리스트 선언
# 리스트 이름 = [표현식 for 반복자 in 반복할 수 있는 것 if 조건문]
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]

# 출력
print(output)