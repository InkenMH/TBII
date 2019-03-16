from tkinter import *
from sql_save import *


def sel():
    selection = "You selected the option " + str(var.get())
    db_name = "game.db"
    user_answer_table = "user_answers"
    insertData(db_name, user_answer_table, "(" + str(QUESTIONID) + "," + str(QUESTIONID) + "," + str(var.get()) + ")")
    root.destroy()


def start_gui(text, dict, question, onlyTwo):
    global root, user, frage, R1, R2, R3, R4, var
    root = Tk()
    root.attributes("-topmost", True)
    root.title('Drinking Game')
    w = 900  # width for the Tk root
    h = 200  # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    var = IntVar()

    user = Label(root)
    user.pack()

    frage = Label(root)
    frage.pack()

    R1 = Radiobutton(root, variable=var, value=1, command=sel)
    R1.pack(anchor=W)

    R2 = Radiobutton(root, variable=var, value=2, command=sel)
    R2.pack(anchor=W)

    if (onlyTwo):
        R3 = Radiobutton(root, variable=var, value=3, command=sel)
        R3.pack(anchor=W)

        R4 = Radiobutton(root, variable=var, value=4, command=sel)
        R4.pack(anchor=W)

    user.config(text=text)
    frage.config(text=dict["question"][-1])

    max_choice = len(dict)
    for i in range(1, max_choice):
        if (i == 1):
            R1.config(text=dict[i][-1])
        elif (i == 2):
            R2.config(text=dict[i][-1])
        elif (i == 3):
            R3.config(text=dict[i][-1])
        else:
            R4.config(text=dict[i][-1])

    global QUESTIONID
    QUESTIONID = question
    root.mainloop()
