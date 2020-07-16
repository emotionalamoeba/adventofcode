# https://adventofcode.com/2019/day/1

import math

def fuelForMassStep(mass):
    return math.floor(mass / 3) - 2

def fuelForMass(fuel):
    additionalFuel = fuelForMassStep(fuel)

    if (additionalFuel <= 0):
        return 0

    return additionalFuel + fuelForMass(additionalFuel)

totalFuelRequired = 0
f = open("masses.txt", "r")
for moduleMass in f:
    massInt = int(moduleMass)
    fuelInt = fuelForMass(massInt)
    totalFuelRequired += fuelInt
    print("Mass : {}, Fuel Required : {}".format(massInt, fuelInt))

print("Total fuel required for modules : {}".format(totalFuelRequired))

