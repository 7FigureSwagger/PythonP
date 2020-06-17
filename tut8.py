#Functions
#Usually start with a lowercase letter for name

def say_hi(user, age):
  print("Hello " + user + " you are " + age)

#Order of code execution
print("First")
say_hi(input("What is your name? "), input("What is your age? "))
print("Second")