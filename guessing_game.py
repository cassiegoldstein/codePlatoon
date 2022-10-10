import random

class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        self.result = ""
       

    def guess(self, user_guess):
        if user_guess > self.answer:
            self.result = "too high"
            return self.result
        elif user_guess < self.answer:
            self.result = "too low"
            return self.result
        else: 
            self.result = "correct"
            return self.result

    def solved(self):
        if self.result == "correct":
            return True
        else:
            return False



        
        
        
def main():

    game = GuessingGame(random.randint(1,100))
    last_guess  = None
    last_result = None
    
    while game.solved() == False:
        if last_guess != None:
            print("Oops! Your last guess, " + last_guess+ ", was " + last_result +"\n")
       
        last_guess  = input("Enter your guess: ")
        last_result = game.guess(int(last_guess))
    
    print(last_guess + " was correct!")

main()



