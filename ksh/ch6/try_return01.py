# test() 함수 선언
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행됨")
    else:
        print("else 구문이 실행됨")
    finally:
        print("finally 구문이 실행됨")
    print("test() 함수 마지막줄임")

test()