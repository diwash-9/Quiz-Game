def main():
    print("\t \t \tWELCOME TO THE QUIZ")
    select = input("\t\t   Do you want to play?(Yes/No) ")
    if select.lower()!="yes":
        print("See you next time.")
        exit()

    print("Great! Let's play quiz")

    print("Available genres: \n 1. Sports \n 2. Geography \n 3. Full Forms")
    print("Select as 1, 2 or 3")
    select = int(input("Which genre of questions do you want to face? "))

    match select:
        case 1:
            sports()
        case 2:
            geography()
        case 3:
            full_form()
        case _:
            print("Chosen genre is not available :(")

def sports():
    print("\n  \t \t Welcome to Sports quiz")
    score = 0
    print ("Total number of questions = 5")
    print("60% or more to win the game")
    print("Your score will be displayed at the end of the quiz.")

    input("Hit enter for the first question ")
    answer = input("Who is know as the 'God of Cricket'? ")
    if (answer.lower()) == "sachin tendulkar":
        score +=1
    
    input("Hit enter for the next question")
    answer = input("Which country won the first ever ICC Cricket World Cup? ")
    if (answer.lower()) == "west indies":
        score +=1
    
    input("Hit enter for the next question")
    answer = input("Which country won the first ever FIFA World Cup? ")
    if (answer.lower()) == "uruguay":
        score +=1

    input("Hit enter for the next question")
    answer = str (input("Which football club has won most number of UEFA Champions League? "))
    if (answer.lower())== "real madrid":
        score +=1

    input("Hit enter for the next question")
    answer = input("In cricket, who is know as the 'Master Blaster'? ")
    if (answer.lower()) == "sachin tendulkar":
        score +=1
    
    print("\n\n\n")
    input("Hit enter to see your result :)")
    
    print("Your score is "+ str(score) + " out of 5")
    percent = ((score/5)*100)
    print("Your percentage is : "+ str(percent) + "%")

    if percent<60:
        print("Sorry you failed the quiz. Try again next time. :)")
    else:
        print("Congratulations! You won the sports quiz.")

    exit()

def geography():
    print("\n  \t \t Welcome to Geography quiz")
    score = 0
    print ("Total number of questions = 5")
    print("60% or more to win the game")
    print("Your score will be displayed at the end of the quiz.")



def full_form():
    print("\n  \t \t Welcome to Full Form quiz")


main()