import random

#define the function draw() which returns the result in the form of string
def draw(usr_choice,com_choice) :
        
        #if,else statement to check if user wins or loses or draws, and returns r
        if usr_choice == com_choice :
              r = "Draw"
        elif usr_choice == "rock" and com_choice == "scissors" :
              r = "Win!"
        elif usr_choice == "paper" and com_choice == "scissors" :
              r = "Lose!"
        elif usr_choice == "scissors" and com_choice == "paper" :
              r = "Win!"
        elif usr_choice == "rock" and com_choice == "paper" :
              r = "Lose!"
        elif usr_choice == "paper" and com_choice == "rock" :
              r = "Win!"
        elif usr_choice == "scissors" and com_choice == "rock" :
              r = "Lose!"
        else :
              print("Invalid")
              r = None

        return r

#indefinite loop so the game never ends unless...
while True :

        #prompts for the user's input and converts it to lowercase
        usr_ans = str(input("Enter your choice (enter 'quit' to exit) : "))
        usr_ans = usr_ans.lower()
        
        #code to break the indefinite loop so user can quit game
        if usr_ans == "quit":
                print("Thank you for playing!")
                break

        #using randrange to generate random number from 1 to 3 inclusive
        x = random.randrange(1,4)
        
        

        #from the results of randrange, assiciate each number to each result        
        if x == 1 :
            y = "scissors"
        elif x == 2 :
            y = "paper"
        elif x == 3 :
            y = "rock"

        #prints computer's guess
        print("Computer chose " + y)
        
        #calls the draw() function and assigns the returned answer to result
        result = draw(usr_ans,y)

        #if user did not enter garbage, their result will be printed
        if not result == None :
                print("You " + result)

        

      
        
    
