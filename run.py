# user enters name and game proceeds...
def get_username():
    while True:
        name = input("Before we start, type in your name: ")
        if name.isalpha():
            print(f"Get ready {name} the Amazing Adventure starts now!")
            break
        else:
            print(f"{name} is not valid, please try again.")