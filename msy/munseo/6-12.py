#290

print("프로그램이 시작")

while True:
    try:
        print("try구문실행")
        break
        print("try구문의 break 뒤입니다.")
    except:
        print("except 구문실행")
    finally:
        print("finally 구문 실행")
    print("while 반복문의 마지막 줄입니다.")
print("프로그램이 종료되었습니다.")