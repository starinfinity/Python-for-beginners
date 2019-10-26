
list = []
len = input("length of list\n")
for i in range(int(len)):
    list.append(input("\n"))

i = 0
j = 0

length = int(len)
while i < length:
    if j < length:
        if i != j and list[i] == list [j]:
                list.pop(j)
                length -= 1
        else:
            j += 1
    else:
        i += 1

print(list)
