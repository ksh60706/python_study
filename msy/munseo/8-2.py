#372

def create_student(name, korean, math, english, science):

    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

students = [
    create_student("서영", 87, 98, 72, 92),
    create_student("수환", 93, 199,188,233),
    create_student("예진",100, 100,100, 100)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    
    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    score_average = score_sum / 4

    print(student["name"], score_sum, score_average, sep = "\t")