import numpy as np
import sys

class Board:
    def __init__(self):
        self.board = np.array([
            [0,0,0],
            [0,0,0],
            [0,0,0]])

        #These string lists will be displayed for the player
        self.A = ["","",""]
        self.B = ["","",""]
        self.C = ["","",""]
        
        self.won = False

        print("Use the function .play() to start a game.")
        print("The argument is \"X\" for starting as the crosses, and \"O\" to play second as the balls")
        print("Remember the rows and columns are numbered 0,1,2")

    def BigTranslate(self):
        """
        This function takes the numerical board and updates the A,B and C lists with Xs and Os.
        """
        def translate(self,i):
            out = ["","",""]
            for k in range(3):
                if self.board[i][k] == 1:  out[k] = "X" 
                if self.board[i][k] == -1: out[k] = "O"
            return out
        self.A = translate(self,0)
        self.B = translate(self,1)
        self.C = translate(self,2)

    def print(self):
        """
        Printing the board for the user to see
        """
        print("""
         |{:2}|{:2}|{:2}|
         |{:2}|{:2}|{:2}|
         |{:2}|{:2}|{:2}|
         """.format(*self.A,*self.B,*self.C))

    def play(self,who):
        """
        This function takes "X" or "O" as arguments and begins a game.
        """
        while not self.won:
            if who == "X":
                self.print() #The emtpy board is displayed
                wherei = int(input("Row to play: ")) # The user is prompted where to play
                wherej = int(input("Column to play: "))
                if self.board[wherei][wherej] != 0: 
                    print("Play not allowed!") #If there is already a piece there
                    while self.board[wherei][wherej] != 0:
                        wherei = int(input("Row to play: ")) # The user is prompted where to play
                        wherej = int(input("Column to play: "))
                self.board[wherei][wherej] = 1 #Place a 1 where X is played
                self.BigTranslate() 
                self.print() #The board is printed showing the player's move
                self.win()

                self.randomplay("O") #Computer plays
                self.BigTranslate()
                self.print()
                self.win()

            elif who == "O":
                self.randomplay("X") #Computer plays   
                self.BigTranslate()
                self.print()
                self.win()

                wherei = int(input("Row to play: ")) # The user is prompted where to play
                wherej = int(input("Column to play: "))
                if self.board[wherei][wherej] != 0: 
                    print("Play not allowed!") #If there is already a piece there
                    while self.board[wherei][wherej] != 0:
                        wherei = int(input("Row to play: ")) # The user is prompted where to play
                        wherej = int(input("Column to play: "))
                self.board[wherei][wherej] = -1 #-1 where O is played
                self.BigTranslate()
                self.print()
                self.win()

            else: print("Invalid Character")

    def randomplay(self,who):
        """
        Computer plays randomly
        """
        wherei,wherej = np.random.randint(0,3,2)
        while self.board[wherei][wherej] != 0:
            wherei,wherej = np.random.randint(0,3,2)
        if who == "X": self.board[wherei][wherej] = 1
        if who == "O": self.board[wherei][wherej] = -1

    def wonn(self):
        """
        Exit game upon ending
        """
        sys.exit()

    def win(self):
        """
        Check if somebody won
        """
        tot3 = 0 #Main Diagonal Count
        tot4 = 0 #Secondary Diagonal Count
        for i in range(3):
            tot = sum(self.board[i])
            if tot == 3:  
                print("¡Ganan las X!")
                self.wonn()
            if tot == -3: 
                print("¡Ganan las O!")
                self.wonn()

            tot = sum(self.board[:,i])
            if tot == 3:  
                print("¡Ganan las X!")
                self.wonn()
            if tot == -3: 
                print("¡Ganan las O!")
                self.wonn()

            tot3 += self.board[i][i]
            tot4 += self.board[-i-1][i]

        if tot3 == 3:  
            print("¡Ganan las X!")
            self.wonn()
        if tot3 == -3: 
            print("¡Ganan las O!")
            self.wonn()

        if tot4 == 3:  
            print("¡Ganan las X!")
            self.wonn()
        if tot4 == -3: 
            print("¡Ganan las O!")  
            self.wonn()

        draw = True
        for i in range(3):
            for j in range(3):
                if self.board[i,j] == 0:
                    draw = False

        if draw: 
            print("Draw :(")
            self.wonn()

