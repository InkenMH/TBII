from Gui import *
from sql_save import *
import os


def start_game():
    dbFileName = 'game.db'

    # As file at filePath is deleted now, so we should check if file exists or not not before deleting them
    if os.path.exists(dbFileName):
        os.remove(dbFileName)
    else:
        print("Can not delete the file as it doesn't exists")

    username = input("Before we start the game please enter your name:\n")

    while not valid_name(username):
        username = input("That was a non valid username, please tell me your real name:\n")

    # needs to acces the global not the local var
    global USERNAME
    USERNAME = username
    question_table = "question"
    answer_table = "answers"
    user_answer_table = "user_answers"
    createQuestionTableWithData(dbFileName, question_table)

    createAnswerTableWithData(answer_table, dbFileName)

    createTable(dbFileName, user_answer_table,
                "(id INTEGER PRIMARY KEY, questionID INTEGER, answerID INTEGER, FOREIGN KEY(questionID) REFERENCES question(id), FOREIGN KEY(answerID) REFERENCES answers(id))")

    FIRSTROUNDDICTIONARY = startQuestionOne(answer_table, dbFileName, question_table)

    text = startQuestionTwo(answer_table, dbFileName, question_table, user_answer_table)

    text = startQuestionThree(answer_table, dbFileName, question_table, text, user_answer_table)

    startQuestionFour(answer_table, dbFileName, question_table, text, user_answer_table)

    text = startQuestionFive(answer_table, dbFileName, question_table, text, user_answer_table)

    startQuestionSix(answer_table, dbFileName, question_table, text)

    startQuestionSeven(answer_table, dbFileName, question_table, user_answer_table)

    startQuestionEight(answer_table, dbFileName, question_table)

    startQuestionNine(answer_table, dbFileName, question_table, user_answer_table)

    start_gui("", FIRSTROUNDDICTIONARY, 10, TRUE)


def createQuestionTableWithData(dbFileName, question_table):
    createTable(dbFileName, question_table, "(id INTEGER PRIMARY KEY, question TEXT)")
    insertData(dbFileName, question_table, "(1, 'What do you want to drink?')")
    insertData(dbFileName, question_table, "(2, 'What are you going to do?')")
    insertData(dbFileName, question_table, "(3, 'Do you try to help the nervous guy?')")
    insertData(dbFileName, question_table, "(4, 'Do you decide to call the police?')")
    insertData(dbFileName, question_table, "(5, 'Do you want to follow them?')")
    insertData(dbFileName, question_table, "(6, 'What do you do now?')")
    insertData(dbFileName, question_table, "(7, 'Do you want to go back to the front and wait for the police?')")
    insertData(dbFileName, question_table, "(8, 'When you see the police arriving, what are you going to do?')")
    insertData(dbFileName, question_table, "(9, 'What do you say?')")


def createAnswerTableWithData(answer_table, dbFileName):
    createTable(dbFileName, answer_table,
                "(id INTEGER PRIMARY KEY, questionID INTEGER, answer TEXT, FOREIGN KEY(questionID) REFERENCES question(id))")
    insertData(dbFileName, answer_table, "(1, 1, 'Beer')")
    insertData(dbFileName, answer_table, "(2, 1, 'Coke')")
    insertData(dbFileName, answer_table, "(3, 1, 'Wine')")
    insertData(dbFileName, answer_table, "(4, 1, 'Water')")
    insertData(dbFileName, answer_table, "(5, 2, 'try to listen closely to their conversation')")
    insertData(dbFileName, answer_table,
               "(6, 2, 'leave the bar, because you do not want to get involved in suspicious activities')")
    insertData(dbFileName, answer_table, "(7, 3, 'you try to make eye contact with the guy to give him a signal')")
    insertData(dbFileName, answer_table,
               "(8, 3, 'you take a piece of paper and write down: do you need help?, then you carefully place the piece of paper into his jacket while you are going over to the bar')")
    insertData(dbFileName, answer_table, "(9, 3, 'no, you are too scared to take action')")
    insertData(dbFileName, answer_table, "(10, 3, 'you have finished your drink and leave the bar to go home')")
    insertData(dbFileName, answer_table, "(11, 4, 'yes')")
    insertData(dbFileName, answer_table, "(12, 4, 'no')")
    insertData(dbFileName, answer_table, "(13, 5, 'yes, but you wait a little bit to not make it too obvious')")
    insertData(dbFileName, answer_table,
               "(14, 5, 'no, you are too scared to follow them and you rather wait for the police')")
    insertData(dbFileName, answer_table, "(15, 6, 'go to the door and open it a tiny bt to listen')")
    insertData(dbFileName, answer_table, "(16, 6, 'try to stand in front of the door and listen to the conversation')")
    insertData(dbFileName, answer_table, "(17, 7, 'yes')")
    insertData(dbFileName, answer_table, "(18, 7, 'no')")
    insertData(dbFileName, answer_table, "(19, 8, 'you wave and show them the way to the back')")
    insertData(dbFileName, answer_table,
               "(20, 8, 'you go over to the barkeeper and tell him to lead the way for the police')")
    insertData(dbFileName, answer_table, "(21, 9, 'yes')")
    insertData(dbFileName, answer_table, "(22, 9, 'no')")


def startQuestionOne(answer_table, dbFileName, question_table):
    FIRSTROUNDDICTIONARY = {"question": view(dbFileName, question_table)[0],
                            1: view(dbFileName, answer_table)[0],
                            2: view(dbFileName, answer_table)[1],
                            3: view(dbFileName, answer_table)[2],
                            4: view(dbFileName, answer_table)[3]}
    start_gui("Welcome " + USERNAME, FIRSTROUNDDICTIONARY, 1, TRUE)
    return FIRSTROUNDDICTIONARY


def startQuestionTwo(answer_table, dbFileName, question_table, user_answer_table):
    SECONDROUNDDICTIONARY = {"question": view(dbFileName, question_table)[1],
                             1: view(dbFileName, answer_table)[4],
                             2: view(dbFileName, answer_table)[5]}
    text = "While enjoying your drink, you observe a suspicious group of young men. They are sitting at the table next to you."
    start_gui(text, SECONDROUNDDICTIONARY, 2, FALSE)
    # wenn user_answers id 2 und auswahl 2 ist dann quit
    if (str(view(dbFileName, user_answer_table)[1][-1]) == "2"):
        quit_game()
    return text


def startQuestionThree(answer_table, dbFileName, question_table, text, user_answer_table):
    THIRDROUNDDICTIONARY = {"question": view(dbFileName, question_table)[2],
                            1: view(dbFileName, answer_table)[6],
                            2: view(dbFileName, answer_table)[7],
                            3: view(dbFileName, answer_table)[8],
                            4: view(dbFileName, answer_table)[9]}
    text = "They are talking about something that got stolen. One of the guys appears to be kind of nervous and he does" \
           " not participate in the discussion. \nThen the other guys threaten him because he owes them money"
    start_gui(text, THIRDROUNDDICTIONARY, 3, TRUE)
    if (view(dbFileName, user_answer_table)[2][-1] == 1):
        text = " The guy gives you a devastated look and signalizes you to go over to the phone in the corner of the bar\n" \
               "It looks like he wants you to call the police."
    elif (view(dbFileName, user_answer_table)[2][-1] == 2):
        text = " The guy takes out the piece of paper and reads it under the table. He then gives you a devastated look and\n" \
               " signalizes you to go over to the phone in the corner of the bar. It looks like he wants you to call the police."
    else:
        quit_game()
    return text


def startQuestionFour(answer_table, dbFileName, question_table, text, user_answer_table):
    FOURTHROUNDDICTIONARY = {"question": view(dbFileName, question_table)[3],
                             1: view(dbFileName, answer_table)[10],
                             2: view(dbFileName, answer_table)[11]}
    start_gui(text, FOURTHROUNDDICTIONARY, 4, FALSE)
    if (view(dbFileName, user_answer_table)[3][-1] == 2):
        quit_game()


def startQuestionFive(answer_table, dbFileName, question_table, text, user_answer_table):
    FIFTHROUNDDICTIONARY = {"question": view(dbFileName, question_table)[4],
                            1: view(dbFileName, answer_table)[12],
                            2: view(dbFileName, answer_table)[13]}
    text = "The police tells you to remain calm and wait until they arrive. Then suddenly the group gets up from \n" \
           "their table and leave into the backroom. They push the nervous guy thru the door. "
    start_gui(text, FIFTHROUNDDICTIONARY, 5, FALSE)
    # wenn user_answers id 2 und auswahl 2 ist dann quit
    if (view(dbFileName, user_answer_table)[4][-1] == 1):
        text = "You just get there in time to grab the door before it closes."
    elif (view(dbFileName, user_answer_table)[4][-1] == 2):
        print("when the police arrives the backroom is empty - game over")
        quit_game()
    return text


def startQuestionSix(answer_table, dbFileName, question_table, text):
    SIXTROUNDDICTIONARY = {"question": view(dbFileName, question_table)[5],
                           1: view(dbFileName, answer_table)[14],
                           2: view(dbFileName, answer_table)[15]}
    text = text, " You are following the group carefully and sneak into the backroom. There is a long hallway and you\n" \
                 "see a door closing at the end of it."
    start_gui(text, SIXTROUNDDICTIONARY, 6, FALSE)


def startQuestionSeven(answer_table, dbFileName, question_table, user_answer_table):
    SEVENTHROUNDDICTIONARY = {"question": view(dbFileName, question_table)[6],
                              1: view(dbFileName, answer_table)[16],
                              2: view(dbFileName, answer_table)[17]}
    text = "You can hear that the nervous man is playing for time and trying to wait until the police arrives."
    start_gui(text, SEVENTHROUNDDICTIONARY, 7, FALSE)
    if (view(dbFileName, user_answer_table)[6][-1] == 2):
        quit_game()


def startQuestionEight(answer_table, dbFileName, question_table):
    EIGTHROUNDDICTIONARY = {"question": view(dbFileName, question_table)[7],
                            1: view(dbFileName, answer_table)[18],
                            2: view(dbFileName, answer_table)[19]}
    start_gui("", EIGTHROUNDDICTIONARY, 8, FALSE)


def startQuestionNine(answer_table, dbFileName, question_table, user_answer_table):
    NINEROUNDDICTIONARY = {"question": view(dbFileName, question_table)[8],
                           1: view(dbFileName, answer_table)[20],
                           2: view(dbFileName, answer_table)[21]}
    text = "The police goes to the back and breaks up the situation. The other guys are told to leave.\n" \
           " The guy you helped comes over to you and wants to thank you. He asks if you want to drink something."
    start_gui(text, NINEROUNDDICTIONARY, 9, FALSE)
    if (view(dbFileName, user_answer_table)[8][-1] == 2):
        quit_game()


def valid_name(name):
    # a valid username has to have at least 2 characters and max 30
    # feel free to code a more sensible check ;)
    return 2 <= len(name) <= 30


def quit_game():
    print("GAME OVER")
    print("It was nice to play with you", USERNAME)
    quit()


if __name__ == "__main__":
    start_game()
