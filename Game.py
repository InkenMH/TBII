USERNAME = ""

FIRSTROUNDDICTIONARY = {"question" : "Wat do you want to drink?",
                        1: "Beer",
                        2: "Coke",
                        3: "Wine",
                        4: "Water"}

SECONDROUNDC1 = {"question" : "Which person do you want to meet?",
                        1: "P1",
                        2: "P2",
                        3: "P3",
                        4: "P4"}

SECONDROUNDC2 = {"question" : "Do you take the same drink again?",
                        1: "YES",
                        2: "NO"}

FIRSTROUNDTRANSITION = {1: SECONDROUNDC1, 2: SECONDROUNDC1, 3: SECONDROUNDC2, 4: SECONDROUNDC2}

def start_game():
    username = input("Before we start the game please enter your name:\n")

    while not valid_name(username):
        username = input("That was a non valid username, please tell me your real name:\n")

    # needs to acces the global not the local var
    global USERNAME
    USERNAME = username

    greet_user()
    start_playing()


def valid_name(name):
    # a valid username has to have at least 2 characters and max 30
    # feel free to code a more sensible check ;)
    return 2 <= len(name) <= 30

def greet_user():
    special_greeting = False
    if special_greeting:
        print("A special hello", USERNAME, "I like to play with you!")
    else:
        print("Hello", USERNAME, "I like to play with you!")

def start_playing():
    print("\n")
    print(USERNAME, ", your first choice should be easy...")

    choice = play_round_with_dict(FIRSTROUNDDICTIONARY)
    nextDict = FIRSTROUNDTRANSITION[choice]
    choice = play_round_with_dict(nextDict)

    quit_game()

def play_round_with_dict(dict):
    max_choice = len(dict)

    print(dict["question"])
    # go over all possible answeres
    for i in range(1,max_choice):
        print("[", str(i) ,"]", dict[i])

    choice = get_users_choice(max_choice)

    print("Your choice was", dict[choice], "...")

    return choice

def get_users_choice(max_choice):
    c = input("Make your decision by typing a number:\n")
    while not int(c) in range(1,max_choice):
        c = input("That was an invalid input, please type a valid number:\n")
    return int(c)

def quit_game():
    print("It was nice to play with you" , USERNAME)

if __name__ == "__main__":
    start_game()
