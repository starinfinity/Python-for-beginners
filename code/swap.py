
def swap(a, b):
    c = a
    a = b
    b = c
    return a, b

print("please enter the numbers to swap")
a = input("\n")
b = input("\n")

print("Swapped variable are ")
print(swap(a, b))
