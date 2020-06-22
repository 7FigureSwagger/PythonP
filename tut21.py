

employees = open("employees.txt", "r")

# print(employees.read())
# print(employees.readline())
# print(employees.readline())
for employee in employees.readlines():
  print(employee)

employees.close()