# test() 함수 선언
def test():
    print("test() 함수의 첫 줄입니다.");
    try:
        print("try 구문이 실행되었습니다.");
        return;
        print("try 구문의 return 키워드 뒤");
    except:
        print("except 구문 실행");
    else:
        print("else 구문 실행");
    finally:
        print("finally 구문이 실행");
    print("test() 함수의 마지막 줄입니다.");

# test 함수 호출
test();