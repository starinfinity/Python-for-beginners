
def reverse(str):
  string = ""
  for i in str:
    string = i + string
  return string


str = input("please enter a string\n")
print(reverse(str))
