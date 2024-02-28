# Import Libraries Here
import time
import sys
import random
from time import sleep

# Welcome Branch Starts Here
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

# Gasoline Branch Starts Here
print("*****************************************\n")
print("Gasoline Branch\n")

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

print("\n*****************************************\n")

print("Weather Branch\n")

# Create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["Snowy", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

# Variable to call the weather() once VRS(Vehicle Response System) is determined
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 50mph.")
    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 40mph.")
    elif weatherAlert == "Rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60mph.")
    elif weatherAlert == "Foggy":
        print("National Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60mph.")
    elif weatherAlert == "Windy":
        print("National Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
    elif weatherAlert == "Icy":
        print("National Weather Service has updated our alarm by 60 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 30mph.")
    else:
        print("\nNational Weather Service forecasts", weatherAlert, "weather conditions.")
        sleep(1.5)
        print("VRS has been disengaged! Drive at your own risk.")
      
vehicleResponseSystem()
