import datetime
import random
import os

i = True
while i == True:
    a = None
    os.system('clear')
    print("    ____                  __     Welcome       _   __                __      to         ______                           __            ")
    print("   / __ \____ _____  ____/ /___  ____ ___     / | / /_  ______ ___  / /_  ___  _____   / ____/__  ____  ___  _________ _/ /_____  _____")
    print("  / /_/ / __ `/ __ \/ __  / __ \/ __ `__ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/  / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/")
    print(" / _, _/ /_/ / / / / /_/ / /_/ / / / / / /  / /|  / /_/ / / / / / / /_/ /  __/ /     / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    ")
    print("/_/ |_|\__,_/_/ /_/\__,_/\____/_/ /_/ /_/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/      \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     ")
    print("To generate a binary number please press B")
    bin = input("To generate natural number press any other key\n").upper()
    if bin != "B":
        print("Do you want to generate the seed too")
        a = input("Press Y for yes N for no\n").upper()
        min = int(input("Please enter the minimum range of Number \t\t"))
        max = int(input("Please enter the Maximum range of Number \t\t"))
        now = datetime.datetime.now()
        seed = now.year*now.month*now.day*now.hour*now.minute*now.second*now.microsecond
        if a == "Y":
            print("Seed is \t\t\t\t\t", seed)
        rand = random.seed(seed)
        randomint = random.randint(min, max)
        print("Random Number is \t\t\t\t\t", randomint)
    else:
        leng = int(input("Please enter the length of Random binary number to be generated\t"))
        res = " "
        for j in range(leng):
            now = datetime.datetime.now()
            seed = now.year*now.month*now.day*now.hour*now.minute*now.second*now.microsecond
            rand = random.seed(seed)
            randint = random.randint(0,1)
            res = str(res)+str(randint)
        print("Random Binary number of length %d is %s" %(leng,res))
    b = input("To generate another random number press Y else press any key\n").upper()
    if b != "Y":
        i = False
