print("welcome to Vat Calulator")
print("Please Input Your Number :")


def vatCal(totalplz):
    result = totalplz + (totalplz * 7 / 100)
    return result


print("Total", vatCal(float(input())))
