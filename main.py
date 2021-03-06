################################################################################
# Program Filename:
# Author: Palmer Campbell-Kaswell
# Date: 4/7/2022
# Description: This script calculates how many gallons of gas a specific car
#              will use in one year, given the amount that the average Oregonian
#              drives in one year. It also calculates the cost to that person
#              given their car type and fuel cost.
# Inputs:  1. Type of car (gas or electric)
#          2. Gas mileage in MPG or MPGe
# Outputs: 1. Gallons/gallons equivalent used in one year on average
#          2. Cost of gas per year at $4.72 per gallon (current price in OR)
#          3. Cost of gas per year at $5.92 per gallon (current price in CA)
#          4. Cost of power over year at $0.1116 per kWh (price at home in
#               Corvallis)
#          5. Cost of power over year at $0.30 per kWh (price at charging
#               station)
################################################################################

carType = 0

###############################################################################
# Function: getcartype
# Description: Sets global carType to 1 or 0 depending on the user's input.
#              This function is necessary in order to loop until a valid input
#              is given.
# Parameters: integer input of 1 or 0
# Return values: "Gas or hybrid", "Electric only", "Please enter either a 1 or a 0."
# Pre-Conditions: Car type not known
# Post-Conditions: Car type known
###############################################################################


def getcartype():
    global carType
    carType = input("Car type = ")
    if carType.isnumeric():
        carType = int(carType)
    else:
        print("Please enter either a 1 or a 0.")
        getcartype()

    if carType == 1:
        return "Gas or hybrid"
    elif carType == 0:
        return "Electric only"
    else:
        print("Please enter either a 1 or a 0.")
        getcartype()


while True:
    print("This script calculates the gallons used per year and cost of gas per year for a typical Oregon driver.")
    print("Please input your car type (1 for gas or hybrid, 0 for electric only):")
    print("You entered: ", str(getcartype()))
    print("")

    if int(carType) == 1:
        print("Please enter your car's gas mileage in MPG (do not include units):")
        mileage = float(input("Gas mileage = "))
        mpgEq = " "
        fuelType = "gas"
    elif int(carType) == 0:
        print("Please enter your car's gas mileage equivalent in MPGe (do not include units):")
        mileage = float(input("Gas mileage equivalent = "))
        mpgEq = " equivalent "
        fuelType = "electricity"
    else:
        # This section unnecessary for proper functioning of code, but removes "variable may be undefined" error
        mileage = ""
        mpgEq = ""
        fuelType = ""

    yearPerGal = mileage / 14032
    galPerYear = 1 / yearPerGal
    costPerYear1 = galPerYear * 4.72
    costPerYear2 = galPerYear * 5.92

    print("")
    print("Gallons" + mpgEq + "used per year: " + str(galPerYear))
    print("Cost of " + fuelType + " per year in Oregon: $" + str(costPerYear1))
    print("Cost of " + fuelType + " per year in California: $" + str(costPerYear2))
    print("")

    if input("Run again? y for yes, any key for no: ") != "y":
        print("")
        break
