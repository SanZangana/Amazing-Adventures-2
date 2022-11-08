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