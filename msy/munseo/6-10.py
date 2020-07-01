#288

def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다/")
        return 
        print("try 구문의 return 키워드 뒤입니다")
    except:
        print("excpt 구문이 실행되었습니다.")
    else:
        print("else구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행")
    print("test()함수의 마지막")

test()