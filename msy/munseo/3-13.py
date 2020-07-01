#131
# 
score = float(input("학점입력>"))

if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("교수님의 사랑")
elif 3.5 <= score:
    print("수호자")
elif 2.8 <= score:
    print("일반인")
elif 2.3 <= score:
    print("소시민")
elif 1.75 <= score:
    print("선구자")
elif 1.0 <= score:
    print("화이팅")
elif 0.5 <= score:
    print("벌레")
elif 0 <= score:
    print("플랑크톤")
else:
    print("혁명")