class allCars:
    licenseCode = ""
    serialCode = ""
    faceDet = ""

    def openAircondition(self):
        print("Turn Air On!!")

class Pickup(allCars):
    pass

class Sedan(allCars):
    pass

class Motorcycle(allCars):
    pass

mostcar = Pickup and Sedan and Motorcycle()
mostcar.openAircondition()