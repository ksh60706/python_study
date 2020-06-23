# 불이 아닌 다른 값이 올때 자동으로 불로 변환
# False로 변환되는 값은 None, 숫자 0과 0.0, 빈 컨테이너 (빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리 등)
# 이 외에는 True로 변환
print("# if 조건문에 0 넣기")
if 0:
    print("0은 True로 변환됩니다.")
else:
    print("0은 False로 변환됩니다.")
print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다.")
else:
    print("빈 문자열은 False로 변환됩니다.")