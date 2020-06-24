# 3장 조건문
# 불 만들기 비교 연산자
import datetime;

print(10 == 100);
print(10 != 100);
print(10 < 100);
print(10 > 100);
print(10 <= 100);
print(10 >= 100);

print("가방" == "가방");
print("가방" != "가방");
print("가방" < "하마");
print("가방" > "하마");

x = 25;
print(10 < x < 30);
print(40 < x < 60);

# 불 연산하기: 논리연산자
# not연산자
print(not True);
print(not False);

x = 10;
under_20 = x < 20;
print("under_20", under_20);
print("not under_20", not under_20);

# and, or 연산자
print(True and True);
print(True and False);
print(False and True);
print(False and False);
print(True or True);
print(True or False);
print(False or True);
print(False or False);

# if 조건문

if True:
    print("True입니다.");
    print("정말 True 입니다.");

if False:
    print("False입니다.");

number = input("정수입력:");
number = int(number);

if number > 0:
    print("양수입니다.");

if number < 0:
    print("음수입니다.");

if number == 0:
    print("0입니다.");

now = datetime.datetime.now();

print(now.year, "년");
print(now.month, "월");
print(now.day, "일");
print(now.hour, "시");
print(now.minute, "분");
print(now.second, "초");

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.".format(
        now.hour
    ));

if now.hour >=12:
    print("현재 시각은 {}시로 오후입니다.".format(
        now.hour
    ));


if 3 <= now.month <= 5:
    print("이번 달은 {}로 봄입니다.".format(
        now.month
    ));

if 6 <= now.month <= 8:
    print("이번 달은 {}로 여름입니다.".format(
        now.month
    ));

if 9 <= now.month <= 11:
    print("이번 달은 {}로 가을입니다.".format(
        now.month
    ));

if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}로 겨울입니다.".format(
       now.month
    ));

number = input("정수 입력:");

last_character = number[-1];
last_number = int(last_character);

if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8 :
    print("짝수입니다.");

if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9 :
    print("홀수입니다.");

number = input("정수 입력:");
last_cha = number[-1];

if last_cha in "02468":
    print("짝수입니다.");

if last_cha in "13579":
    print("홀수입니다.");

number = input("정수 입력:");
number = int(number);

if number % 2 == 0:
    print("짝수입니다.");

if number % 2 == 1:
    print("홀수 입니다.");

#if else

number = input("정수입력:");
number = int(number);

if number % 2 == 0:
    print("짝수입니다!");
else:
    print("홀수이지렁");

#elif

now = datetime.datetime.now();
month = now.month;

if 3 <= month <=5:
    print("현재는 봄입니다.");
elif 6 <= month <= 8:
    print("현재는 여름입니다.");
elif 9 <= month <= 11:
    print("현재는 가을입니다.");
else:
    print("현재는 겨울입니다.");


score = float(input("학점 입력: "));

if score == 4.5:
    print("신");
elif 4.2 <= score < 4.5:
    print("교수님의 사랑");
elif 3.5 <= score < 4.2:
    print("현 체재의 수호자");
elif 2.8 <= score < 3.5:
    print("일반인");
elif 2.3 <= score < 2.8:
    print("일탈을 꿈꾸는 소시민");
elif 1.75 <= score < 2.3:
    print("오락문화의 선구자");
elif 1.0 <= score < 1.75:
    print("불가촉천민");
elif 0.5 <= score < 1.0:
    print("자벌레");
elif 0 <= score < 0.5:
    print("플랑크톤");
elif score == 0:
    print("시대를 앞서가는 혁명의 씨앗");

score = float(input("학점 입력: "));

if score == 4.5:
    print("신");
elif 4.2 <= score:
    print("교수님의 사랑");
elif 3.5 <= score:
    print("현 체재의 수호자");
elif 2.8 <= score:
    print("일반인");
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민");
elif 1.75 <= score:
    print("오락문화의 선구자");
elif 1.0 <= score:
    print("불가촉천민");
elif 0.5 <= score:
    print("자벌레");
elif 0 <= score:
    print("플랑크톤");
elif score == 0:
    print("시대를 앞서가는 혁명의 씨앗");

#false로 변환되는 값
print("# if 조건문에 0 넣기");
if 0:
    print("0은 True로 변환됩니다.");
else:
    print("0은 False로 변환됩니다.");
print();

print("# if 조건문에 빈 문자열 넣기");
if "":
    print("빈 문자열은 True로 변환됩니다.");
else:
    print("빈 문자열은 False로 변환됩니다.");

# pass 키워드
number = input("정수 입력: ");
number = int(number);

if number > 0:
    #양수일 때: 아직 미구현 상태입니다.(IdentationError발생)
    pass
else:
    #음수일 때: 아직 미구현 상태입니다.
    pass

# pass 키워드
number = input("정수 입력: ");
number = int(number);

if number > 0:
    #양수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError
else:
    #음수일 때: 아직 미구현 상태입니다.
    raise NotImplementedError