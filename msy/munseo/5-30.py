#266

def test():
    print("함수가 호출되었습니다.")
    yield "Test"

print("a지점 통과")
test()

print("B지점 통과")
test()
print(test())