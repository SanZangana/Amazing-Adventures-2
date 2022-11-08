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