# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:28:41 2020

@author: Gautam_Pai
"""


#N-Queens problem - Backtracking problem

class QueensProblem:
    
    def __init__(self, numofQueens):
        self.numofQueens = numofQueens
        self.chessTable = [[None for i in range(numofQueens)] for j in range(numofQueens)]
    
    def solveQueensProblem(self):
        
        if self.solve(0):
            self.printQueens()
        else:
            print("There is no solution...")            
    
    
    def solve(self, colIndex):
        
        if colIndex == self.numofQueens:
            return True
        
        for rowIndex in range(self.numofQueens):
            if self.isPlaceValid(rowIndex, colIndex):
                self.chessTable[rowIndex][colIndex] = 1
                
                if self.solve(colIndex+1):
                    return True
                
                #IF the constraint is not followed revert the position of the queen to 0
                self.chessTable[rowIndex][colIndex] = 0
        return False
    
    def printQueens(self):
        
        for i in range(self.numofQueens):
            for j in range(self.numofQueens):
                
                if self.chessTable[i][j] == 1:
                    print(' * ', end="")
                else:
                    print(' - ', end="")
            print('\n')
    
    
    def isPlaceValid(self, rowIndex, colIndex):
        
        #Same row
        for i in range(colIndex):
            if self.chessTable[rowIndex][i] == 1:
                return False
        
        #traverse from top left to bottom right diagonally on the placed queen
        j=colIndex
        for i in range(rowIndex, -1, -1):
            
            if j<0:
                break
            
            if self.chessTable[i][j] == 1:
                return False
            
            j-=1
        
        #traverse from bottom left to top right diagonally on the placed queen
        j=colIndex
        for i in range(rowIndex, len(self.chessTable)):
            
            if j<0:
                break
            
            if self.chessTable[i][j] == 1:
                return False
            
            j-=1
        return True


if __name__ == "__main__":
    queensProblem = QueensProblem(20)
    queensProblem.solveQueensProblem()
        
        