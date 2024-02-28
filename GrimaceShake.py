
# Import Libraries Here
import time
import sys

timeToSleep = 1

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

# Code to have the elilipsis add a dot every /5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center System Loading" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first
    time.sleep(.5)
    if  ellipsis == 4:
        ellipsis =0
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")

print("*****************************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random
from time import sleep

# Function that lists Gas levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return  currentGasLevel

# Function that lists Gas Stations, m randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell","Speedway","Marathon","Circle K","Moble","Costco","Meijer","7Eleven"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby

# Function will call the gasLevelGauge to determine our gas level and then find a close gas station
# by calling the listOfGasStations function if we are on Low or Quarter Tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform (1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform (25.1, 50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2.5)
        print("     ***Calling Triple AAA***")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank, checking Google Maps for the closest gas station...")
        sleep(2.5)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationsQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half tank full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank.":
        print("Your gas tank is at three quarter tank.")
    else:
        print("Your gas tank is full - YEAH!!!! - Congratulations! - Vroom Vrooms!")
              
            
gasLevelAlert()
