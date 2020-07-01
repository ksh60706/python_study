#204

number = int(input("정수입력>"))

if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}은 짝수입니다."
    ]).format(number, number))
else:    
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}은 홀수입니다."
    ]).format(number, number))