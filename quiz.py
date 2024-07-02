#-----------------------------------------------------------------------------------------------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num =1

    for key in questions:
        print('#------------------------')
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num+=1
    display_score(correct_guesses, guesses)
#-----------------------------------------------------------------------------------------------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("INCORRECT!")
        return 0
#-----------------------------------------------------------------------------------------------------------------------
def display_score(correct_guesses, guesses):
    print("#------------------------")
    print("RESULTS")
    print("#------------------------")
    
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("your score is: "+str(score)+"%")
#-----------------------------------------------------------------------------------------------------------------------

questions = {
    "What name i preffer while anonymous?: ": "C",
    "Which is my preffered linux os?: ": "A",
    "Am i fat?: ": "B",
    "My fav person?: ": "D"
}

options = [["A. serizen", "B. AVALANCH", "C. avalanch", "D. none"],
           ["A. kali", "B. ubuntu", "C. parrot os", "D. Blackarch"],
           ["A. Not That Much", "B. ALMOST EXPLODED", "C. No", "D. none"],
           ["A. Rinkiya ke papa", "B. Gandhi", "C. Elon Musk", "D. Adolf Hitler"]]

new_game()

