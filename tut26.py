from student import Student

student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Jim", "Business", 3.8, False)

#call class function

print("Student 1: " + str(student1.on_honor_roll()))
print("\nStudent 2: " + str(student2.on_honor_roll()))
