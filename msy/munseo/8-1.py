students = [
    { "name" : "김수환", "korean" : 87, "math" : 98, "english": 50, "sceience" : "40"},
    { "name" : "문서영", "korean" : 87, "math" : 98, "english": 50, "sceience" : "40"},
    { "name" : "장예진", "korean" : 87, "math" : 98, "english": 50, "sceience" : "40"}
]

print("이름", "총점", "평균", sep="\t")

for student in students:
    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["sceience"]
    score_average = score_sum / 4
    
    print(student["name"], score_sum, score_average, sep="\t")