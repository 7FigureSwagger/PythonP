
#class is a data type ie. what a student is (student data type)
#an object is an actual student, not the template anymore but a representation of a specific student

#import "Student" class from the "Student" file
from student import Student

student1 = Student("Ali", "CS", 3.0, False)
student2 = Student("Jim", "Geo-Engineering", 3.0, False)


print(student1.name)
print(student2.name)