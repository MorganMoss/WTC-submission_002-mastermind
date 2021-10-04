import random


def run_game():
    "Starts Mastermind"
    # step 1 : creating 4 digit code
    code_length = 4 # so it can be generalized for different difficulty
    code = []
    while len(code) < (code_length):
        i = random.randint(1,8)
        if i not in code:
            code.append(i)
        
    print(  "{}-digit Code has been set.".format(code_length),
            "Digits in range 1 to 8. You have 12 turns to break it.")
    turn = 1
    number_of_turns = 12
    while turn <= number_of_turns: 

        # step 2 : getting input
        try:
            guess = input("Input {} digit code: ".format(code_length))
        except: 
            break
        # step 2 : error checking 
            # if theres exactly the right amt of digits and nothing more
        if len(guess) != code_length or not guess.isdigit():
            print("Please enter exactly {} digits.".format(code_length))
            continue
            # if digits in the correct range of 1 - 8
        check = True
        for char in guess:
            if not char in "12345678":
                print("Please enter digits in range 1 to 8")
                check = False
                break
        if not check:
            continue     

            # converts a string to list of ints
        guess = list(map(int,list(guess))) 

        # step 3 : comparing guess to original
        correct_not_in_place = 0
        correct_in_place = 0
        for index in range(code_length):
            # number of correct and in place digits
            if guess[index] == code[index]:
                correct_in_place += 1
            # number of correct and not in place digits
            elif guess[index] in code:
                correct_not_in_place += 1

        print("Number of correct digits in correct place:     {}".
                format(correct_in_place))
        print("Number of correct digits not in correct place: {}".
                format(correct_not_in_place))
                
            # guess correct
        if guess == code:
            print("Congratulations! You are a codebreaker!")
            break
        
        turn += 1

        print("Turns left: {}".format(number_of_turns+1-turn))

    print("The code was: {}".format("".join(list(map(str,code)))))




if __name__ == "__main__":
    run_game()
