def checker(a , b):
    c = 0
    gcd = 1
    if a == 0 or b == 0:
        print("The GCD is zero")
    elif a < 0 or b < 0:
        print("can not find GCD for value less than zero")
    elif a < b:
        c = a
        while gcd == 1:
            if c == 0:
                gcd = 0
            elif a % c == 0 and b % c == 0:
                print("The GCD for %d and %d is %d" %(a, b, c))
                gcd = 0
            else:
                gcd = 1
                c -= 1
    elif b < a:
        c = b
        while gcd == 1:
            if c == 0:
                gcd = 0
            elif a % c == 0 and b % c == 0:
                print("The GCD for %d and %d is %d" %(a, b, c))
                gcd = 0
            else:
                gcd = 1
                c -= 1
    elif a == b:
        print("The GCD for %d and %d is %d" %(a, b, a))

    return c


print(" Enter the number to find their GCD")
a = int(input(""))
b = int(input(""))
checker(a,b)
