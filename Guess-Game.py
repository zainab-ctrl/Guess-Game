from random import randint
def main():
             print("\t\t--------Guess Game Started---------")
             print("Description: Computer have selected one number between 1 to 100 integer "+
             "if you guess the right number you will win.")
             print()
             trys = game()
             if(trys <= 5):  
                 Status = 'Excellent'
             elif(trys <= 10):  
                 Status = 'Well done'
             elif(trys <= 15):  
                 Status = 'Good'
             elif(trys <= 20):  
                 Status = 'Not Bad'
             else:
                  Status = 'Focus and think before typing'
             print(f"\tCongragulations! You win the game in {trys} trys\n\t\t--------{Status}---------")
             
def game():
       b = randint(1,100)
       trys = 1
       while True:
        try:
            if(trys%5 == 0):
                 print("Focus you can do it.")
            a = int(input("Enter a number btw 1-100:"))
            if(a>b):
             print("It's higher than number")
            elif(a<b):
             print("It's lower than number")
            else:
             return trys
            print("Try again!")
            trys+=1
        except ValueError:
            print("Enter right value.")

if __name__ == "__main__":
       main()
