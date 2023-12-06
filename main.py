from days.dayOne import DayOne
from days.dayTwo import DayTwo

def main(): 
      print("(1) Day One")
      print("(2) Day Two")
      dayOne = DayOne('data\\input\\dayOne\\actual1.txt', 'data\\input\\dayOne\\actual2.txt')
      dayTwo = DayTwo('data\\input\\dayTwo\\actual1.txt', 'data\\input\\dayTwo\\actual2.txt')

      choice = input("what day would you like to run?")
      if choice == "1":
            dayOne.puzzleOne()
            dayOne.puzzleTwo()
      elif choice == "2":
            dayTwo.puzzleOne()
            dayTwo.puzzleTwo()
            
main()