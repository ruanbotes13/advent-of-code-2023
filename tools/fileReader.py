class FileReader:
    def __init__(self):
        pass

    def readFileLines(self, path):
        listOfStrings = []
        with open(path) as f:
            for line in f:
                    listOfStrings.append(line.strip())
        return listOfStrings