# Write a program to define a function with multiple return values

def returnMultipleValues (name, age, gender):
  return (name, age, gender)

name, age, gender = returnMultipleValues('sachith', 19, 'm')
print(name, age, gender)
