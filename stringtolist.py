
def strtolist(str):
  string = []
  count = 0
  for i in str:
    string.append(i)
  return string


str = input("please enter a string\n")
print(strtolist(str))
