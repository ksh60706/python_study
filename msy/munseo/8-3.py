#374

def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean" : korean, 
        "math" : math,
        "english" : english,
        "science" : science
    }

def student_get_sum(student):
    return student["korean"] + student["math"] +\
        student["english"] + student["science"]

def student_get_average(student):
    return student["korean"] + student["math"] +\
        student["english"] + student["science"]

def student_to_string(student):
    return "{}\t{}\t{}\t".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student))

students = [
    create_student("문서영",100,100,100,100),
    create_student("김수환",100,100,100,100),
    create_student("장예진",100,100,100,100)
]
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))

