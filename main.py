from days.dayOne import DayOne

def main(): 
      print("(1) Day One")
      dayOne = DayOne('data\\input\\dayOne\\actual1.txt', 'data\\input\\dayOne\\actual2.txt')
      choice = input("what day would you like to run?")
      if choice == "1":
            dayOne.puzzleOne()
            dayOne.puzzleTwo()
            
main()