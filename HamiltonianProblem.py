# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 22:54:13 2020

@author: Gautam_Pai
"""


#Hamiltonian Problem - Backtracking

class HamiltonianProblem:
    def __init__(self, adjacencyMatrix):
        self.numofVertexes = len(adjacencyMatrix)
        self.hamiltonianPath = [None]*self.numofVertexes
        self.adjacencyMatrix = adjacencyMatrix
    
    def hamiltonianCycle(self):
        
        self.hamiltonianPath[0] = 0
        
        if not self.findFeasibleSolution(1):
            print("No feasible solution exists...")
            return
        else:
            self.showHamiltonianPath()
    
    def findFeasibleSolution(self, position):
        
        #BASE CASE:: Check if the last node is connected to the first node
        if position == self.numofVertexes:
            x = self.hamiltonianPath[position-1]
            y = self.hamiltonianPath[0]
            
            if x is not None:
                if self.adjacencyMatrix[x][y] == 1:
                    return True
                else:
                    return False
            else:
                return False
        
        for vertextIndex in range(1, self.numofVertexes):
            
            if self.isFeasible(position, vertextIndex):
                self.hamiltonianPath[position] = vertextIndex
            
            if self.findFeasibleSolution(position+1):
                return True
            #BACKTRACK
            else:
                self.hamiltonianPath[position] = None
            
        return False
    
    def isFeasible(self, actualPosition, vertex):
        
        previousVertex = self.hamiltonianPath[actualPosition-1]
        #first criteria, whether the two nodes are connected
        if previousVertex is not None:
            if self.adjacencyMatrix[previousVertex][vertex] == 0:
                return False
        
            #second criteria,   whether we have already added this given node
            for i in range(actualPosition):
                if self.hamiltonianPath[i] == vertex:
                    return False
        
            return True
        return False
    
    def showHamiltonianPath(self):
        
        print('Hamiltonian cycle exists...')
        
        for i in range(self.numofVertexes):
            print(self.hamiltonianPath[i])
            
        print(self.hamiltonianPath[0])

if __name__ == "__main__":
    adjacencyMatrix = [[0,1,1,1,0,0],
                       [1,0,1,0,1,1],
                       [1,1,0,1,0,1],
                       [1,0,1,0,0,1],
                       [0,1,0,0,0,1],
                       [0,1,1,1,1,0]
                      ]
    hamiltonianPath = HamiltonianProblem(adjacencyMatrix)
    hamiltonianPath.hamiltonianCycle()
            
                
            
        
        
    