



# -*- coding: utf-8 -*-

import time
import Reversi
import math
from random import randint, choice
from playerInterface import *


nbnodes=0


milieudepartie=40
findepartie=15

class myPlayer(PlayerInterface):

    def __init__(self):
        self._board = Reversi.Board(10)
        self._mycolor = None

    def getPlayerName(self):
        return "NOUS"




    def evalBoard(self):
        boardValue=0
        line=0
        column=0

        #Matrice des poids de parite
        matParite=[[5, -4, 3, 2,2 ,2 ,2 ,3,-4,5],
                   [-4,-5,-1,-1,-1,-1,-1,-1,-5,-4],
                   [3,-1, 1 ,1 ,1 ,1 ,1 ,1,-1 ,3],
                   [2,-1, 1 ,-1 ,-1 ,-1 ,-1 ,1,-1,2],
                   [2,-1, 1 ,-1 ,0 ,0,-1 ,1,-1,2],
                   [2,-1, 1 ,-1 ,0 ,0,-1 ,1,-1,2],
                   [2,-1, 1 ,-1 ,-1 ,-1 ,-1 ,1,-1,2],
                   [3,-1, 1 ,1 ,1 ,1 ,1 ,1,-1 ,3],
                   [-4,-5,-1,-1,-1,-1,-1,-1,-5,-4],
                   [5, -4, 3, 2,2 ,2 ,2 ,3,-4,5]]
        
        ##Mobilite
        possible_move = self._board.legal_moves()
        if self._board._nextPlayer==self._mycolor:
            boardValue=boardValue+2*len(possible_move);
        else:
            boardValue=boardValue-2*len(possible_move);

        
        for line in range(10):
            for column in range(10):
                ##Recherche de coins
                if (line==0 or line==9) and (column==0 or column==9):
                    if self._board._board[line][column]==self._mycolor:
                        boardValue=boardValue+20
                    elif not self._board._board[line][column]==self._board._EMPTY:
                        boardValue=boardValue-20
                ##Calcul de la parite
                if self._board._board[line][column]==self._mycolor:
                    boardValue=boardValue+matParite[line][column]
                elif not self._board._board[line][column]==self._board._EMPTY:
                    boardValue=boardValue-matParite[line][column]

                

        


        boardValue= boardValue+self._board.heuristique()
        return boardValue

    
    def MaxMin(self,profMax,firstPlayer,a,b):
        global nbnodes
        nbnodes+=1
        if self._board.is_game_over():
            (nbwhites, nbblacks) = self._board.get_nb_pieces()
            if nbwhites < nbblacks:
                return 400 if firstPlayer else -400
            elif nbblacks < nbwhites:
                return -400 if firstPlayer else 400
            else:
                return 0
        if profMax==0:
            eval=self.evalBoard()
            return eval 
        possible_move = self._board.legal_moves()
        for x in possible_move:
            self._board.push(x)
            V=self.MinMax(profMax-1,firstPlayer,a,b)
            if V>a:
                a=V
                if (a>=b):
                    self._board.pop()
                    return b
            self._board.pop()
        return a

    def MinMax(self,profMax,firstPlayer,a,b):
        global nbnodes
        nbnodes+=1
        if self._board.is_game_over():
            (nbwhites, nbblacks) = self._board.get_nb_pieces()
            if nbwhites < nbblacks:
                return 400 if firstPlayer else -400
            elif nbblacks < nbwhites:
                return -400 if firstPlayer else 400
            else:
                return 0
        if profMax==0:
            eval=self.evalBoard()
            return eval
        possible_move = self._board.legal_moves()
        for x in possible_move:
            self._board.push(x)
            V=self.MaxMin(profMax-1,firstPlayer,a,b)
            if V<b:
                b=V
                if (a>=b):
                    self._board.pop()
                    return a
            self._board.pop()
        return b


    def IAMinMax(self, profmax):
        global nbnodes
        nbnodes = 0
        nbnodes+=1
        if self._mycolor == self._board._BLACK:
            firstPlayer=True
        else:
            firstPlayer=False
        best=-math.inf
        bestplay=None
        listofequalmoves=[]
        possible_move = self._board.legal_moves()
        for x in possible_move:
            self._board.push(x)
            v=self.MinMax(profmax-1,firstPlayer,a=-math.inf,b=math.inf)
            if v>best or bestplay==None:
                best=v
                bestplay=x
                listofequalmoves=[x]
            elif v==best:
                listofequalmoves.append(x)
            self._board.pop()
                        
        return choice(listofequalmoves)
    

    def getPlayerMove(self):
        profmax=2
        global milieudepartie
        global findepartie
        (nbwhites, nbblacks) = self._board.get_nb_pieces()
        couprestant=100-nbwhites-nbblacks
        if (milieudepartie>couprestant and findepartie<couprestant):
            profmax=4
        if (findepartie>=couprestant):
            profmax=8
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return (-1,-1)
        move=self.IAMinMax(profmax)
        self._board.push(move)
        print("I am playing ", move)
        print("wesh",couprestant)
        (c,x,y) = move
        assert(c==self._mycolor)
        print("My current board :")
        print(self._board)
        return (x,y) 




    def playOpponentMove(self, x,y):
        assert(self._board.is_valid_move(self._opponent, x, y))
        print("Opponent played ", (x,y))
        self._board.push([self._opponent, x, y])
        

    def newGame(self, color):
        self._mycolor = color
        self._opponent = 1 if color == 2 else 2

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")



