from os import system, name
import random
import turtle


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def test(a, b, c):
    x = False
    if a == b and b == c and c == a:
        if a != ' ':
            x = True
    return x


def result(a):
    x = False
    if test(a[0], a[1], a[2]):
        x = True
    if test(a[3], a[4], a[5]):
        x = True
    if test(a[6], a[7], a[8]):
        x = True
    if test(a[0], a[3], a[6]):
        x = True
    if test(a[1], a[4], a[7]):
        x = True
    if test(a[2], a[5], a[8]):
        x = True
    if test(a[0], a[4], a[8]):
        x = True
    if test(a[2], a[4], a[6]):
        x = True

    return x


def board(a):
    print("\n")
    print(" %s | %s | %s " % (a[0], a[1], a[2]))
    print("-----------")
    print(" %s | %s | %s " % (a[3], a[4], a[5]))
    print("-----------")
    print(" %s | %s | %s " % (a[6], a[7], a[8]))


def rules(p1, p2):
    print("press the number which represent the block to put your X or O")
    print("O is %s \t X is %s" % (p1, p2))
    rul = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    board(rul)


def start(p1, p2):
    a = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    i = 1
    w = "draw"
    try:
        while i < 10:

            if i % 2 == 0:
                inp = int(input("%s's turn\t" % p2))
                if a[inp - 1] == " ":
                    a[inp - 1] = "X"
                    clear()
                    rules(p1, p2)
                    board(a)
                    i += 1
                else:
                    print("block already marked")

            else:
                inp = int(input("%s's turn\t" % p1))
                if a[inp - 1] == " ":
                    a[inp - 1] = "O"
                    clear()
                    rules(p1, p2)
                    board(a)
                    i += 1
                else:
                    print("block already marked")

            result(a)
            if result(a) == True:
                if i % 2 == 0:
                    w = p1
                    print("%s Won" % p1)
                else:
                    w = p2
                    print("%s Won" % p2)
                i = 10

    except Exception as e:
        print(e)
    return w


def game():
    print("Welcome to the Tic Tac Toe Game")
    print("To play press Enter")
    input("\n")
    clear()
    p1 = input("Enter the name of player 1 \n")
    p2 = input("Enter the name of player 2 \n")
    clear()
    rules(p1, p2)
    input("press enter to continue \n")
    a = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    board(a)
    w = start(p1, p2)
    return w


d = game()


def celebrate():
    tina = turtle.Turtle()
    tina.speed(0)

    # firework color
    def pen(colour):
        tina.color(colour)

    pen('red')

    # move to a new place on screen
    def move():
        tina.pu()
        x = random.randint(-165, 165)
        y = random.randint(-165, 165)
        tina.goto(x, y)
        tina.pd()

    # set the sky black
    def sky(colour):
        wn = turtle.Screen()
        wn.bgcolor(colour)

    sky('black')

    # draw a firework
    def firework(size):
        for num in range(20):
            tina.fd(size)
            tina.rt(180 - (360 / 20))

    for i in range(2):
        a = random.randrange(10, 150)
        pen("white")
        firework(a)
        move()
        a = random.randrange(10, 150)
        pen('yellow')
        firework(a)
        move()
        a = random.randrange(10, 150)
        pen('blue')
        firework(a)
        move()
        a = random.randrange(10, 150)
        pen('green')
        firework(a)
        move()
        a = random.randrange(10, 150)
        pen('red')
        firework(a)
        move()
        a = random.randrange(10, 150)
        pen('orange')
        firework(a)
        move()


if d == "draw":
    print("Game Draw")
else:
    print("The winner is %s" % d)
    celebrate()
