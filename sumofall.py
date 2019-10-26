
number = input("please enter the number \n")

len = len(number)
sum = 0
n = int(number)
for i in range(len):
    sum += n % 10
    n //= 10

print(sum)
