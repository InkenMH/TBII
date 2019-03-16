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
