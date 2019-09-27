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

    print("Do you want to generate the seed too")
    a = input("Press Y for yes N for no\n").upper()
    now = datetime.datetime.now()
    seed = now.year*now.month*now.day*now.hour*now.minute*now.second*now.microsecond
    if a == "Y":
        print(seed)
    rand = random.seed(seed)
    randomint = random.randint(0,1000)
    print("random number is ", randomint)
    b = input("To generate another random number press Y else press any key\n").upper()
    if b != "Y":
        i = False
