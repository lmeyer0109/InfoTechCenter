print("*****************************************")
print("Gasoline Branch\n\n")

# Import Libraries Here
import random

# Function that lists Gas levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank", "Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return  currentGasLevel

#Function that lists Gas Stations, m randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell","Speedway","Marathon","Circle K","Moble","Costco","Meijer","7Eleven"]
    gasStationNearby = random.choice(gasStations)
    return gasStationNearby


print(gasLevelGauge())
print(listOfGasStations())
