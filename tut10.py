is_male = True
is_human = False

if is_male and is_human:
  print("You are a human male")
#Add parens for not()
elif is_male and not(is_human):
  print("I can tell you are male, but not human")
else:
  print("You are not a human or male")
