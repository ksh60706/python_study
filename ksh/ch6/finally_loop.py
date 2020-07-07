print("프로그램이 시작됨")

while True:
    try:
        print("try 구문이 실행됨")
        break
        print("try 구문의 break 키워드 뒤임")
    except:
        print("except 구문이 실행됨")
    finally:
        print("finally 구문 실행")
    print("while 반복문 마지막줄임")
print("프로그램 종료")