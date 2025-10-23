#A very classic stater code of assigning grades according to the marks

#define class Student
class Student:
  # initialising attributes grade and name
    def __init__(self, name, score):
        self.name = name
        self.score = score

  # grade according to marks
    def grade(self):
        if self.score >= 85:
            return "HD"
        elif self.score >= 75:
            return "D"
        elif self.score >= 65:
            return "C"
        elif self.score >= 50:
            return "P"
        else:
            return "F"


# get the number of student
num_students = int(input("Enter number of students: "))

# for ith student in range of total student
for i in range(num_students):
    name = input("Enter name: ")
    score = int(input("Enter score: "))

    student = Student(name, score)
    # display
    print(f"{student.name} - {student.score} - ({student.grade()})")
