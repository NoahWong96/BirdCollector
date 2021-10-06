import os.path
from properties import Properties


def FindBadDataBirdTest():
    BadData = []

    for i in range(0,3999):
        indexString = str(i)
        filePath = "../../../Data/birds_test/"  + indexString + ".jpg"
        if not os.path.exists(filePath):
            BadData.append(int(indexString))

    return BadData

def FindBadDataBirdTrain():
    BadData = []
    birdProperties = Properties()
    fileNames = birdProperties.getBirdFileNames()


    for i in range(0,199):
        birdFileName = birdProperties.getBirdFileNames()[i]

        for j in range(0,39):
            filePath = "../../../Data/birds_train/" + birdFileName + "/" + str(j) + ".jpg"
            if not os.path.exists(filePath):
                BadData[i].append(j)

    return BadData



if __name__ == '__main__':
    print(FindBadDataBirdTrain())


