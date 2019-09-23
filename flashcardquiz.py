#Author Rahul Gahlot
#github.com/starinfinity
import os


tryag ='Y'

while tryag == 'Y':
    a = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    m = 0
    print("**************************************************************************")
    print("*************************Welcome to Flashcard Quiz************************")
    print("**************************************************************************")
    print("you will be given 10 questions. Each question carry same marks.")
    print("press a for option A, b for B, c for C and d for D. 0 marks for other keys")
    print("To start the quiz, press return key")
    input()
    os.system("clear")
    print("1. Which nut is used to make Dynamite?")
    a[0] = input("A. Walnut                 B. Peanut           \nC. Cashew                 D. Almonds\n").upper()
    os.system("clear")
    print("2. How many rings are on the Olympic flag?")
    a[1] = input("A. 3                      B. 4                \nC. 5                      D. 7\n").upper()
    os.system("clear")
    print("3. On a clear night about how many galaxies are visible to the naked eye?")
    a[2] = input("A. 2                      B. 2 mil.           \nC. 9000                   D. 5000\n").upper()
    os.system("clear")
    print("4. How many muscles do you have in total in all your fingers combined?")
    a[3] = input("A. 10                     B. 22               \nC. 20                     D. None\n").upper()
    os.system("clear")
    print("5. What part of the atom has a negative charge?")
    a[4] = input("A. proton                 B. neutron          \nC. nucleus                D. electron\n").upper()
    os.system("clear")
    print("6. Light travel fastest in what medium ?")
    a[5] = input("A. Vacuum                 B. salt-water       \nC. Air                    D. same in all medium\n").upper()
    os.system("clear")
    print("7. The mineral, diamond, is naturally what crystal shape ?")
    a[6] = input("A. Trigonal               B. Hexagonal        \nC. Cubic                  D. Dodecahedronal\n").upper()
    os.system("clear")
    print("8. At the end of 2012, which only city has hosted the modern Olympic Games three times?")
    a[7] = input("A. Athens                 B. London           \nC. Rome                   D. Tokyo\n").upper()
    os.system("clear")
    print("9. What beverage is traditionally drunk by the winner of the Indianapolis 500 car race? ")
    a[8] = input("A. Coca-cola              B. Milk             \nC. beer                   D. Red Wine\n").upper()
    os.system("clear")
    print("10. Near Field Communication technology is a set of standards for?")
    a[9] = input("A. Hot-air ballooning     B. Smartphones      \nC. Border control         D. Satellites\n").upper()
    os.system("clear")

    b = ["B", "C", "A", "D", "D", "A", "C", "B", "B", "B"]
    print("calculating marks")
    for i in range(10):
        c = i+1
        if a[i] == b[i]:
            print("Question %d is correct" % c)
            m = m + 1
        else:
            print("Question %d is incorrect" % c)

    print("*********************************Total marks are %d/10*********************************" % m)
    if m == 10:
        print("Congrats! you did great.")
    elif m < 10 and m > 3:
        print("You did good.")
    else:
        print("boy, you should open your book right now.")

    tryag = input("Want to try again? yes y for yes, n for No").upper()

print("Thank You for taking this quiz.")
