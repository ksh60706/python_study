#169

dictionary = {
"name": "건조 망고",
"type": "당절임",
"ingredient": ["망고", "설탕","망고","수박"],
"origin":"필리핀"
}

value = dictionary.get("서영")
print("값:",value)

if value == None:
    print("존재하지 않는 키에 접근 가능했었습니다")