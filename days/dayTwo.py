from tools.fileReader import FileReader

class DayTwo:

    def __init__(self, partOneFile, partTwoFile):
        self.partOneFile = partOneFile
        self.partTwoFile = partTwoFile
        self.maxRed = 12
        self.maxGreen = 13
        self.maxBlue = 14

    def puzzleOne(self):
        print("Day Two Puzzle One")
        fileReader = FileReader()
        listOfStrings = fileReader.readFileLines(self.partOneFile)
        listOfGames = []

        for game in listOfStrings:
            gamePossible = True

            gameParts = game.split(': ')
            gameParts[0] = gameParts[0].replace('Game ', '')
            gameRounds = gameParts[1].split('; ')
            
            for gameRound in gameRounds:
                gameRed = 0
                gameGreen = 0
                gameBlue = 0

                gamePlays = gameRound.split(", ")

                for gamePlay in gamePlays:
                    play = gamePlay.split(' ')
                    
                    if play[1] == "red":
                        gameRed = gameRed + int(play[0])
                    elif play[1] == "green":
                        gameGreen = gameGreen + int(play[0])
                    elif play[1] == "blue":
                        gameBlue = gameBlue + int(play[0])

                if (gameRed > self.maxRed or gameGreen > self.maxGreen or gameBlue > self.maxBlue):
                    gamePossible = False

            if (gamePossible == True):
                listOfGames.append(int(gameParts[0]))

        sum = 0

        for game in listOfGames:
            sum = sum + game

        print("1. " + str(sum))

    def puzzleTwo(self):
        fileReader = FileReader()
        listOfStrings = fileReader.readFileLines(self.partTwoFile)
        listOfGames = []

        for game in listOfStrings:
            gameRed = 0
            gameGreen = 0
            gameBlue = 0

            gameParts = game.split(': ')
            gameParts[0] = gameParts[0].replace('Game ', '')
            gameRounds = gameParts[1].split('; ')
            
            for gameRound in gameRounds:
                

                gamePlays = gameRound.split(", ")

                for gamePlay in gamePlays:
                    play = gamePlay.split(' ')
                    
                    if play[1] == "red" and int(play[0]) > gameRed:
                        gameRed = int(play[0])
                    elif play[1] == "green" and int(play[0]) > gameGreen:
                        gameGreen = int(play[0])
                    elif play[1] == "blue" and int(play[0]) > gameBlue:
                        gameBlue = int(play[0])

            listOfGames.append(gameRed * gameGreen * gameBlue)

        sum = 0

        for game in listOfGames:
            sum = sum + game

        print("2. " + str(sum))