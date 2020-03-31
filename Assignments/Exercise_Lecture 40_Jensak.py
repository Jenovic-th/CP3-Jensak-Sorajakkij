print("Welcome to Jeno GameShop")
print("Please login")
Customer = input("Customer Name :")
Customerpassword = input("Customer Password :")
if Customer == "Jensak" and Customerpassword == "1234":
    print("login Success!!")
    print("=========Process=========")
    print("Can I help you today?")
    print("=========Process=========")
    print("1.Choose Shop Item")
    print("2.EXIT")
    CustomerChoose = int(input("Choose :"))
    if CustomerChoose == 1:
        print("Summer Sale!!! all item just 650 THB")
        print("=========catalogue Item=========")
        print("GOD4 : God of War 4")
        print("DMC4 : Devil may Cry 4")
        print("RE2R : Resident Evil 2 Remake")
        print("RED2 : Reddead Redemption 2")
        print("OVER : Overcook 2")
        print("======Please Selected======")
        Selected = (input("Select GAME CODE>>>"))

        GOD4 = "You Select God of war 4"
        DMC4 = "You Select Devil may Cry 4"
        RE2R = "You Select Resident Evil 2 Remake"
        RED2 = "You Select Red dead Redemption 2"
        OVER = "You SelectOvercook 2"
        Prize = 650

        if Selected == "GOD4" or "DMC4" or "RE2R" or "RED2" or "OVER":
            Copy = int(input("How many Copy? :"))
            print("Total :", Prize * Copy, "THB")

    if CustomerChoose == 2:
        print("Exit")

else:
    print("Eror!! Please try again")