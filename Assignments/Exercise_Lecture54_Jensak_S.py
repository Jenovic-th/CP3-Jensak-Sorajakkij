def welcome():
    print("Welcome to Host Club")
    print("")
    print("Member login please")


def member():
    memberlogin = input("login :")
    memberpassword = input("Password :")
    if memberlogin == "jensak" and memberpassword == "1234":
        print("Welcome back mate :)")
        print("Can I Help you today?")
        print("")


def menu():
    print(" a.   I Need partner tonight ")
    print(" b.   I Need to rent porn dvd ")
    print("")
    userchoose = (input("Please Select :"))
    if userchoose == "a":
        print("Ok pal")
        print("We can delivery to you in 30 min or less")
        print("Prize is 100$ per Hour")
        useragree = input("Everyting ok?,yes or no :")
        print(useragree)
        if useragree == "yes":
            print("ok cool Thx and have a good time!!")
        elif useragree == "no":
            return menu()
    if userchoose == "b":
        print("4$ per dvd")
        print("We Delivery to you in 30 min or less")
        dvd = int(input("How many copy? :"))
        print("Total :", (dvd * 4) + (dvd * 7 / 100), "$")
        usercopy = input("Everyting ok?,yes or no :")
        print(usercopy)
        if usercopy == "yes":
            print("ok cool Thx and have a good time!!")
        elif usercopy == "no":
            return menu()


print(welcome())
print(member())
print(menu())
