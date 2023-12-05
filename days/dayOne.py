from tools.fileReader import FileReader

class DayOne:

    def __init__(self, partOneFile, partTwoFile):
        self.partOneFile = partOneFile
        self.partTwoFile = partTwoFile

    def puzzleOne(self):
        print("Day One Puzzle One")
        fileReader = FileReader()
        listOfStrings = fileReader.readFileLines(self.partOneFile)
        sum = self.sumValues(listOfStrings)
        print("1. " + str(sum))

    def puzzleTwo(self):
        print("Day One Puzzle Two")
        fileReader = FileReader()
        listOfStrings = fileReader.readFileLines(self.partTwoFile)
        listOfNumbers = [];

        for line in listOfStrings:
            oldWord = line
            newWord = ''
            while len(oldWord) > 0:
                if (oldWord.startswith("one")):
                    newWord = newWord + "1"
                    oldWord = oldWord[1:len(oldWord)]
                elif (oldWord.startswith("two")):
                    newWord = newWord + "2"
                    oldWord = oldWord[1:len(oldWord)]
                elif (oldWord.startswith("three")):
                    newWord = newWord + "3"
                    oldWord = oldWord[1:len(oldWord)]
                elif (oldWord.startswith("four")):
                    newWord = newWord + "4"
                    oldWord = oldWord[1:len(oldWord)]
                elif (oldWord.startswith("five")):
                    newWord = newWord + "5"
                    oldWord = oldWord[1:len(oldWord)]
                elif (oldWord.startswith("six")):
                    newWord = newWord + "6"
                    oldWord = oldWord[1:len(oldWord)]
                elif (oldWord.startswith("seven")):
                    newWord = newWord + "7"
                    oldWord = oldWord[1:len(oldWord)]
                elif (oldWord.startswith("eight")):
                    newWord = newWord + "8"
                    oldWord = oldWord[1:len(oldWord)]
                elif (oldWord.startswith("nine")):
                    newWord = newWord + "9"
                    oldWord = oldWord[1:len(oldWord)]
                else:
                    newWord = newWord + oldWord[0]
                    oldWord = oldWord[1:len(oldWord)]

            listOfNumbers.append(newWord)
        
        sum = self.sumValues(listOfNumbers);
        
        print("2. " + str(sum))

    def sumValues(self, listOfStrings):
        first = -1
        last = -1
        listOfNumbers = [];

        for line in listOfStrings:
                reverseLine = line
                for i, c in enumerate(line):
                    if c.isdigit():
                            first = i
                            break
                    
                for i, c in enumerate(reverseLine[::-1]):
                    if c.isdigit():
                            last = len(line) - i - 1
                            break

                listOfNumbers.append(line[first] + "" + line[last])
        
        sum = 0;

        for i in listOfNumbers:
                sum = sum + int(i)

        return sum
