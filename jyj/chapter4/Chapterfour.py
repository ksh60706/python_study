## 리스트
import time


list_a = [1,2,3];
list_b = [4,5,6];

print("# 리스트");
print("list_a = ", list_a);
print("list_b = ", list_b);
print();

print("# 리스트 기본 연산자");
print("list_a + list_b = ", list_a + list_b);
print("list_a * 3 = ", list_a * 3);
print();

print("# 길이구하기");
print("len(list_a) = ", len(list_a));

# 리스트 요소 추가 append, insert
list_a = [1,2,3];

print("# 리스트 뒤에 요소 추가하기");
list_a.append(4);
list_a.append(5);
print(list_a);
print();

print("# 리스트 중간에 요소 추가하기");
list_a.insert(0, 10);
print(list_a);

# extend는 한번에 여러 요소를 추가하고 싶을 때
list_a.extend([6,7,8]);
print(list_a);

# 리스트 연결 연산자와 요소 추가의 차이
list_a = [1,2,3];
list_b = [4,5,6];

print(list_a + list_b);
print(list_a);
print(list_b);

print(list_a.extend(list_b));
print(list_a);
print(list_b);

# 요소 제거 del, pop
list_a = [0,1,2,3,4,5];
print("# 리스트의 요소 하나 제거하기");

del list_a[1];
print("del list_a[1] = ",list_a);

list_a.pop(2);
print("pop(2) = ", list_a);

list_b = [0,1,2,3,4,5,6];
del list_b[3:6];
print(list_b);

list_c = [0,1,2,3,4,5,6];
del list_c[:3];
print(list_c);

del list_c[3:];
print(list_c);

#값으로 제거하기, remove
list_c = [1,2,1,2];
list_c.remove(2);
print(list_c);

# 모두 제거하기, clear
list_d = [0,1,2,3,4,5,6];
list_d.clear();
print(list_d);

# 리스트 내부에 있는지 확인하기: in/not in 연산자
list_a = [273, 32, 103, 57, 52];
print(273 in list_a);
print(99 in list_a);
print(32 in list_a);
print(333 not in list_a);
print(103 not in list_a);
print(54 not in list_a);

# for 반복문: 리스트와 함께 사용하기
array = [273, 32, 103, 57, 52];

for element in array:
    print(element);

## 딕셔너리와 반복문
dict_a = {
    "name": "어벤져스 앤드게임",
    "type": "히어로 무비" 
}
print(dict_a);
print(dict_a["name"]);
print(dict_a["type"]);

dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중", "치자황색소"],
    "origin": "필리핀"
}

print("name: ", dictionary["name"]);
print("type: ", dictionary["type"]);
print("ingredient: ", dictionary["ingredient"]);
print("origin: ", dictionary["origin"]);
print();

dictionary["name"] = "8D 건조 망고";
print("name: ", dictionary["name"]);

# 딕셔너리에 값 추가하기/제거하기
dictionary["price"] = 5000;
print(dictionary);

dictionary["name"] = "8D 건조 파인애플";
print(dictionary);

del dictionary["ingredient"];
print(dictionary);

# 딕셔너리에 요소 추가하기
dictionary1 = {};

print("요소 추가 이전: ", dictionary1);

dictionary1["name"] = "새로운 이름";
dictionary1["head"] = "새로운 정신";
dictionary1["body"] = "새로운 몸";

print("요소 추가 이후: ",dictionary1);

# 딕셔너리에 요소 제거하기
dictionary2 = {
    "name": "7D 건조 망고",
    "type": "당절임"
}

print("요소 제거하기 전: ", dictionary2);

del dictionary2["name"];
del dictionary2["type"];

print("요소 제거 이후: ", dictionary2);

# 딕셔너리 내부에 키가 있는지 확인하기
dictionary3 = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중", "치자황색소"],
    "origin": "필리핀"
};

key = input("접근하고자 하는 키: ");

if key in dictionary3:
    print(dictionary3[key]);
else:
    print("존재하지 않는 키에 접근하고 있습니다.");

value = dictionary3.get("존재하지 않는 키");
print("값: ", value);

if value == None:
    print("존재하지 않는 키에 접근했었습니다.");

# for 반복문: 딕셔너리와 함께 사용하기
for key in dictionary3:
    print(key,":",dictionary3[key]);

# 반복문과 while 반복문
print(list(range(10)));

for i in range(5):
    print(str(i) + "= 반복 변수");
print();

for i in range(5,10): # 5부터 시작해서 10-1 까지
    print(str(i) + "= 반복 변수");
print();

for i in range(0, 10, 3):  # 0부터 시작해서 10-1까지 3씩 증가
    print(str(i) + "= 반복 변수");
print();

# for 반복문: 리스트와 범위 조합하기
array = [11, 33, 44, 55, 66];

for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]));

# for 반복문: 반대로 반복하기
for i in range(4, 0 - 1, -1):
    print("현재 반복 변수: {}".format(i));

for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i));

# while 반복문
#while True:

#    print(".", end=""); # 무한반복 ctrl+c

i = 0;
while i < 10:
    print("{}번째 반복 중".format(i))
    i += 1;

list_test = [1,2,1,2];
value = 2;

while value in list_test:
    list_test.remove(value);

print(list_test);

# while 반복문: 시간을 기반으로 반복하기
print(time.time());

number = 0;

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1;

print("5초 동안 {}번 반복했습니다.".format(number));\

# while 반복문: break 키워드/ continue 키워드
i = 0;

while True:
    print("{}번째 반복문입니다.".format(i))
    i += 1

    input_text = input("종료할래?:")
    if input_text in ["y", "Y"]:
        print("반복을 종료합니다.")
        break;

#continue 
numbers = [5,15,6,20,7,25];

for number in numbers:
    if number < 10:
        continue
    print(number);

# min max sum
numbers = [11,22,33,44,55];
print(min(numbers));
print(max(numbers));
print(sum(numbers));

list_a = [1,2,3,4,5];
list_reversed = reversed(list_a);

print("# reversed 함수: ");
print("reversed([1,2,3,4,5])", list_reversed);
print("list(reversed([1,2,3,4,5])):", list(list_reversed));
print();

print("# reversed() 함수와 반복문");
print("for i in reversed([1,2,3,4,5]):");
for i in reversed(list_a):
    print("-",i);

num = [1,2,3,4,5];
print(num[::-1]);

# enumerate()함수와 반복문 조합
example_list = ["요소A","요소B","요소C"];

print("단순출력");
print(example_list);
print();

print("# enumerate() 함수 적용 출력");
print(enumerate(example_list));
print();

print("# list() 함수로 강제 변환 출력");
print(list(enumerate(example_list)));
print();

print("# 반복문과 조합하기");
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value));


# 딕셔너리의 item() 힘수 반복문 조합하기
example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
};

print("#딕셔너리의 items() 함수");
print("items():", example_dictionary.items());

print("# 딕셔너리의 item() 함수와 반복문 조합하기");

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element));

#리스트 내포
array = [];

for i in range(0,20,2):
    array.append(i * i)

print(array);

array = [i * i for i in range(0, 20, 2)];
print(array);

array = ["사과","자두","초콜릿", "바나나","체리"];
output = [fruit for fruit in array if fruit != "초콜릿"];
print(output);

number = int(input("정수입력:"));

if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}은 짝수 입니다.""".format(number, number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}은 홀수 입니다.""".format(number, number));

number = int(input("정수입력:"));

if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.
        {}은 짝수 입니다.""".format(number, number))
else:
    print("""입력한 문자열은 {}입니다.
        {}은 홀수 입니다.""".format(number, number));

number = int(input("정수입력:"));

if number % 2 == 0:
    print("입력한 문자열은 {}입니다. \n{}은 짝수 입니다.".format(number, number))
else:
    print("입력한 문자열은 {}입니다.\n{}은 홀수 입니다.".format(number, number));

test = (
    "이렇게 입력해도"
    "하나의 문자열이"
    "생성되지렁"
);

print("test:", test);
print("type(test):", type(test));

number = int(input("정수 입력해주세욤:"));

if number % 2 ==0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}은 짝수입니다."
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}은 홀수입니다."
    ).format(number, number));

print("::".join(["1","2","3","4","5"]))

number = int(input("정수 입력해주세욤:"));

if number % 2 ==0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}은 짝수입니다."
    ]).format(number, number))
        
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}은 홀수입니다."
    ]).format(number, number));

numbers = [1,2,3,4,5,6];
r_num = reversed(numbers);

print("reversed_numbers: ", r_num);
print(next(r_num));
print(next(r_num));
print(next(r_num));
print(next(r_num));
print(next(r_num));
print(next(r_num));
