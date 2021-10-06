import random 
import time
from PIL import Image
from properties import Properties


class BirdVisualizer:

    def __init__(self, specificBird = False, specificBirdNumber = 1 ):
        self.specificBird = specificBird
        self.specificBirdNumber = specificBirdNumber
        self.birdProperties = Properties()


    def showSpecificBird(self, birdSpecies=1, numberPics =5, timeInterval = 0.5):
        birdFileName = self.birdProperties.getBirdFileNames()[birdSpecies]
        
        for i in range(0, numberPics):
            randomNumberString = str(random.randint(0,39))
            birdFolder = self.birdProperties.getBirdFileNames()[birdSpecies]
            randomBirdFileName = "../../../Data/birds_train/" + birdFolder + "/" + randomNumberString +".jpg"
            print(randomBirdFileName)
            Image.open(randomBirdFileName).show()
            time.sleep(timeInterval)
  

    def showRandomBirds(self, numberPics=5, timeInterval=0.5): 
    
        for i in range(0,numberPics):
            randomNumber = random.choice([i for i in range(0,3999) if i not in self.birdProperties.getMissingDataBirdTest()])
            randomNumberString = str(randomNumber)

            #Use a parameter for the file path
            randomBirdFileName = "../../../Data/birds_test/" + randomNumberString + ".jpg"
            print(randomBirdFileName)
            Image.open(randomBirdFileName).show()
            time.sleep(timeInterval)

if __name__ == '__main__':
    example = BirdVisualizer()
    example.showSpecificBird(5)
    #example.showRandomBirds(5)
    

