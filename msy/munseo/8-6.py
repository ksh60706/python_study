#388

class student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science
        
    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

students = [
    student("김수환", 100,100,100,100),
    student("문서영", 100,100,100,100),
    student("장예진", 100,100,100,100)
]

print("이름", "총점", "평균", sep = "\t")
for student in students:
    print(str(student))