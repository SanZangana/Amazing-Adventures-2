# user enters name and game proceeds...
def get_username():
    while True:
        name = input("Before we start, type in your name: ")
        if name.isalpha():
            print(f"Get ready {name} the Amazing Adventure starts now!")
            break
        else:
            print(f"{name} is not valid, please try again.")


def validate_left_right():
    while True:
        question = input("Please enter 'R' or 'L'. ")
        if question.lower() == 'l' or question.lower() == 'r':
            return question.lower()
        else:
            print(f"{question} is not valid, please try again.")


def question_1():
    """
    so here the user has to make a choice between two different roads/paths-
    and each road lead to different paths and end goals/adventures.
    """
    print(
        "You open your eyes, and see two roads a head in a mystical wood.\n"
        "The road to the right leads to a big castle while the road to\n"
        "the left leads to a UFO. Now, which path will you choose?\n"
        "Press enter 'R' for the castle or 'L' for the UFO.\n")

    get_user_answer = validate_left_right()


 # R path
    if get_user_answer == 'r':
        wizard_appears()

    # L path
    if get_user_answer == 'l':
        alien_appears()


# R path
def wizard_appears():
    print(
        "On the way to the castle... a wizard appears. "
        "The wizard asks 'You can ask me to craft a weapon, "
        "what will you choose?' "
        "Press 'R' for a raygun or 'L' for a Lightsaber ")
    get_user_answer = validate_left_right()
    if get_user_answer == 'r':
        raygun()
    if get_user_answer == 'l':
        lightsaber()


# L path
def alien_appears():
    print(
        "While on your way to the UFO a foreign green creature with\n"
         "one eye appears! "
        "'Hello human, would you like to taste soda\n"
        "from Jupiter?' Press 'R' for yes and 'L' for no\n")
    get_user_answer = validate_left_right()
    if get_user_answer == 'r':
        lose_game()
    if get_user_answer == 'l':
        no_soda()


# R path
def lose_game():
    print("You drink the soda but your vision starts to get blurry...\n" 
        "you pass out. GAME OVER. Press 'R' to restart the game ")


# L path
def no_soda():
    print("You neglect the offer and keep walking on the path to the UFO.\n"
     "You come to a lake with a bridge and you wonder if\n" 
    "you should swim across or walk across the bridge.\n"
    "Press 'R' for swim or 'L' for walk")
    get_user_answer = validate_left_right()
    if get_user_answer == 'r':
        swim()
    if get_user_answer == 'l':
        walk()


# L path 
def swim():
    print("You jump in the water but there's a alligator in there and\n"
     "as soon as you do your first stroke the alligator eats you. YOU LOSE")

# R path 
def walk():
    print("You reached the UFO! Good job. You enter the UFO and the\n"
     "aliens give you a ride through the Galaxy. Thank you for playing! ")



# R path
def raygun():
    print("You acquired the desired weapon, keep walking\n"
    "forward or take a shortcut? Press 'R'\n" 
    "for forward or 'L' for shortcut")
    get_user_answer = validate_left_right()
    if get_user_answer == 'r':
        forward()
    if get_user_answer == 'l':
        shortcut()

def lightsaber():
    print("You acquired the desired weapon, keep walking\n"
    "forward or take a shortcut? Press 'R'\n" 
    "for forward or 'L' for shortcut")
    get_user_answer = validate_left_right()
    if get_user_answer == 'r':
        forward()
    if get_user_answer == 'l':
        shortcut()

# R path
def shortcut():
    print("The shortcut leads you to a pack of "
    "wolves that chase you down... and you LOSE! ")



# R path
def forward():
    print("You're finally at the gates to the castle...\n"
    "but before you enter you must defeat\n"
    "the demon that guards the castle.\n"
    "Press 'R' to use radiation beam or 'L' for laser beam ")
    get_user_answer = validate_left_right()
    if get_user_answer == 'r':
        radiation_beam()
    if get_user_answer == 'l':
        laser_beam()

# R path
def radiation_beam():
    print("Oh no, you lost! The demon is\n"
    "immune to radiation and eats you.")


# L path
def laser_beam():
    print("The laser instantly melts the demon!\n"
    "Congratulaions you won! ")


if __name__ == "__main__":
    input("Hello and welcome to Amazing Adventures. "
    "To start, please press enter key ")
    get_username()
    question_1()
    while True:
        restart = input("Would you like to play again? Press 'Y' or 'N'.\n")  
        if restart.lower() == 'n':
            print("Thanks for playing!\n")
            break
        elif restart.lower() != 'y':
            print(f"{restart} is not valid, please try again")
        else:
            question_1()
