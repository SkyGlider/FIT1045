import random

#define the function draw() which returns the computer's guess in the form of string
def draw() :

        #using randrange to generate random number from 1 to 3 inclusive
        x = random.randrange(1,4)
        #y is empty string
        y = ""

        #from the results of randrange, assiciate each number to each result        
        if x == 1 :
            y = "scissors"
        elif x == 2 :
            y = "paper"
        elif x == 3 :
            y = "rock"

        #prints computer's guess
        print("Computer chose " + y)

        return y

#indefinite loop so the game never ends unless...
while True :

        #prompts for the user's input and converts it to lowercase
        usr_ans = str(input("Enter your choice : "))
        usr_ans = usr_ans.lower()
        
        #code to break the indefinite loop so user can quit game
        if usr_ans == "quit":
                break
        
        #calls the draw() function and assigns the returned answer to com_ans
        com_ans = draw()

        #if,else statement to check if user wins or loses or draws, and prints the results
        if usr_ans == com_ans :
              print("It's a draw")
        elif usr_ans == "rock" and com_ans == "scissors" :
              print("You win!")
        elif usr_ans == "paper" and com_ans == "scissors" :
              print("You lose!")
        elif usr_ans == "scissors" and com_ans == "paper" :
              print("You win!")
        elif usr_ans == "rock" and com_ans == "paper" :
              print("You lose!")
        elif usr_ans == "paper" and com_ans == "scissors" :
              print("You win!")
        elif usr_ans == "scissors" and com_ans == "rock" :
              print("You lose!")
        else :
              print("Your answer is invalid, so you lose!")

      
        
    
