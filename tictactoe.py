# TIC TAC TOE Game  version 2.0
# Developed By:  Pawan Sir at CID An Education Hub
# Youtube Channel : youtube.com/c/cidaneducationhub
# copyright: This Product/game is not for resale .
# =========================================================================
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar

p1, p2 = 'Player1','Player2' # by default  two players name are : player 1 and player 2
Z = 0  # variable Z will count score of winner
sX, sO = 0, 0  # score for X and Score for O is by default 0
player = 'X'


def exitWindow(e):
    try:
        mainWindow.wm_attributes('-topmost', False)# its necessary 
        msg = messagebox.askyesno(title='Exit Game',
                                  message='Do you really want to exit Game?')
    except:
        msg = messagebox.askyesno(title='Exit Game',
                                  message='Do you really want to exit Game?')
    if msg == True:
        sys.exit(root.destroy())


def callback(r, c):
    global player
    # print(player,states[r][c],stop_game)
    if player == 'X' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='X', fg='blue', bg='white')
        states[r][c] = 'X'
        player = 'O'
    if player == 'O' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='O', fg='orange', bg='black')
        states[r][c] = 'O'
        player = 'X'
    check_for_winner()


def check_for_winner():
    global stop_game, Z

    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            b[i][0].configure(bg='grey')
            b[i][1].configure(bg='grey')
            b[i][2].configure(bg='grey')
            stop_game = True
            Z = states[i][0]  # counting winner score

            winner = messagebox.showinfo("Winner", states[i][0] + '  Won!')
            desableAllButton()
            score()  # score is printing
            break

        elif states[0][i] == states[1][i] == states[2][i] != 0:
            b[0][i].configure(bg='grey')
            b[1][i].configure(bg='grey')
            b[2][i].configure(bg='grey')
            stop_game = True
            Z = states[0][i]  # counting winner score

            winner = messagebox.showinfo("Winner", states[1][i] + '  Won!')
            desableAllButton()
            score()  # score is printing
            break

        elif states[0][0] == states[1][1] == states[2][2] != 0:
            b[0][0].configure(bg='grey')
            b[1][1].configure(bg='grey')
            b[2][2].configure(bg='grey')
            stop_game = True
            Z = states[0][0]  # counting winner score

            winner = messagebox.showinfo("Winner", states[1][1] + '  Won!')
            desableAllButton()
            score()  # score is printing
            break

        elif states[2][0] == states[1][1] == states[0][2] != 0:
            b[2][0].configure(bg='grey')
            b[1][1].configure(bg='grey')
            b[0][2].configure(bg='grey')
            stop_game = True
            Z = states[2][0]  # counting winner score

            winner = messagebox.showinfo("Winner", states[1][1] + '  Won!')
            desableAllButton()
            score()  # score is printing
            break
    nextPlay.config(text="Play Again", bg='red', state=NORMAL)


def score():
    global player, Z, sX, sO, root
    won = Z  # states[i][0]
    nextPlay.config(state=DISABLED)
    if won == 'X':
        sX += 1
        scoreX.config(text="{}[X]: {}".format(p1, sX))
    elif won == 'O':
        sO += 1
        scoreO.config(text="{}[O]: {}".format(p2, sO))
    # game over when any of player got score 3
    if sX == 3 or sO == 3:
        stop_game = True
        winner = messagebox.askyesno("Game Over",
                    "Highest Score:\n\t{}\n\t{}\nDo you want to play  again?".format(
                                         scoreX.cget('text'), scoreO.cget('text')))
        if winner == True:
            playAgain()
            sX, sO = 0, 0
            scoreX.config(text="{}[X]: {}".format(p1, sX))
            scoreO.config(text="{}[O]: {}".format(p2, sO))
        elif winner == False:
            exiting = messagebox.showinfo("Come Soon",
                            "Hope! you have enjoyed the game.\n game is Exiting...")
            root.destroy()


def playAgain():
    global stop_game
    stop_game = False
    enableAllButton()
    for i in range(3):
        for j in range(3):
            states[i][j] = 0
            b[i][j].configure(text='', bg='powder blue')


def getName():
    global player, p1, p2, player1E, player2E
    p1 = player1E.get()
    p2 = player2E.get()
    print("Player1: ", p1, " Player2: ", p2)
    scoreX.config(text="{}[X]: 0".format(p1))
    scoreO.config(text="{}[O]: 0".format(p2))
    root.deiconify()
    mainWindow.destroy()



def desableAllButton():
    for i in range(3):
        for j in range(3):
            b[i][j].config(state=DISABLED)


def enableAllButton():
    for i in range(3):
        for j in range(3):
            b[i][j].config(state=NORMAL)


# Game design ==============================================================================================>
root = Tk()
root.title('TIC TAC TOE **CID**')
root.resizable(0, 0)
#============ add any image as icon of game
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='tictactoe.png'))
root.bind('<Escape>', exitWindow)  # press esc key anytime to exit game
bg = PhotoImage(file="tictactoe.png")    # background image of game 
bgImage = Label(root, image=bg).place(x=-60, y=0)
# buttons====================
b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
# text on buttons    (by default 0)
states = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 60), width=3, bg='powder blue',
                         command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j)

# toplevel designed for getting name of two players
mainWindow = Toplevel(root)
mainWindow.title("TIC TAC TOE v2.0 [ Main Menu ]")
mainWindow.resizable(0, 0)
mainWindow.wm_iconbitmap('game1.ico')
mainWindow.config(bg='green')
mainWindow.bind('<Escape>', exitWindow)  # press esc key anytime to exit game
# ===============ADDING extra designs
# place ur app on center of Windows
height = 450
width = 580
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
mainWindow.geometry("{}x{}+{}+{}".format(width, height, x, y))
mainWindow.overrideredirect(1)  # it hides title bar
mainWindow.wm_attributes('-topmost', True)  # will be on top of all window

# game menu UI design ====================
bgImage = Label(mainWindow, image=bg).place(x=-30, y=0)

devBy = Label(mainWindow, text="TIC TAC TOE v2.0 By: CID An Education Hub",
              font=('mistral', 10, 'bold'), fg='blue', bg='powder blue', width=150)
devBy.pack(side=TOP)
# =============choose mode   SINGLE or TWO PLAYERS
mode = Label(mainWindow, text='CHOOSE MODE', bg='blue', fg='goldenrod1',
             font=('impact', 12), width=20)
mode.place(x=180, y=220)


# Hover effect for single player button
def onButtonS(e):
    singleMode['bg'] = 'goldenrod3'


def leaveButtonS(e):
    singleMode['bg'] = 'goldenrod1'


# Hover effect for two player button
def onButtonT(e):
    twoMode['bg'] = 'goldenrod3'


def leaveButtonT(e):
    twoMode['bg'] = 'goldenrod1'


# =============single player mode===============
singleMode = Button(mainWindow, text='Single player', bg='goldenrod1', width=20,
                    activebackground='goldenrod3', activeforeground='blue')
singleMode.place(x=190, y=250)  # its inactive now , will come in version 3.0
singleMode.bind('<Enter>', onButtonS)
singleMode.bind('<Leave>', leaveButtonS)

# login System===========================>
i = 0  # a global value
loadingLabel = 0
progress = 0


def load():  # loading message upadating
    global i, progress, loadingLabel
    loadingLabel = Label(mainWindow, text="", font=('arial', 10, 'bold'), fg='blue')
    loadingLabel.place(x=400, y=420)
    progress = Progressbar(mainWindow, orient=HORIZONTAL, length=250,
                           mode='determinate')
    progress.place(x=150, y=420)
    if i <= 10:
        txt = str(10 * i) + '%'
        loadingLabel.config(text=txt)
        loadingLabel.after(1000, load)
        progress['value'] = int(10 * i)
        i += 1
    if progress['value'] == 100:
        getName()


# ============= two players mode==========
def mode2():
    global player1E, player2E
    mode.destroy()
    singleMode.destroy()
    twoMode.destroy()
    player1 = Label(mainWindow, text="Player 1 Name: ", bg='red',
                    font=('arial', 10), fg='white')
    player1.place(x=200, y=330)
    player1E = Entry(mainWindow, fg='blue', highlightbackground='blue',
                     highlightthickness=2, width=30)
    player1E.place(x=310, y=330)

    player2 = Label(mainWindow, text="Player 2 Name: ", bg='red',
                    font=('arial', 10), fg='white')
    player2.place(x=200, y=360)
    player2E = Entry(mainWindow, fg='blue', highlightbackground='blue',
                     highlightthickness=2, width=30)
    player2E.place(x=310, y=360)
    submit = Button(mainWindow, text="Play Game", bg='blue', fg='white',
                    width=15, command=load)
    submit.place(x=280, y=390)


twoMode = Button(mainWindow, text='Two player', bg='goldenrod1', width=20,
                 activebackground='goldenrod3', activeforeground='blue',command=mode2)
twoMode.place(x=190, y=280)
twoMode.bind('<Enter>', onButtonT)
twoMode.bind('<Leave>', leaveButtonT)

# toplevel finished

# play again
nextPlay = Button(root, text="", width=10,bd=0,command=playAgain)
nextPlay.grid(row=4, column=1)

scoreX = Label(root, text="Score X: ", font=('mistral', 12))
scoreX.grid(row=4, column=0)

scoreO = Label(root, text="Score O: ", font=('mistral', 12))
scoreO.grid(row=4, column=2)
stop_game = False

copyri8 = Label(root, text="Developed By: Pawan Sir @CID An Education Hub",
                font=('mistral', 12, 'bold'), fg='blue', bg='powder blue', width=70)
copyri8.grid(row=5, columnspan=3)
root.withdraw()
mainloop()
