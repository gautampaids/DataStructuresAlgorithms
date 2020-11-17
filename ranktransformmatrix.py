# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:17:21 2020

@author: Gautam_Pai
"""
from typing import List
from collections import Counter

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        output = [len(j) * [0 * len(j)] for i,j in enumerate(matrix)] #list comprehension trick to initialize list[list]
        dict1 = dict()
        for i in range(len(matrix)): 
            for j in range(len(matrix[i])):
                dict1[i,j] = matrix[i][j]
        while len(dict1) != 0:
            coordinates = [k for k,v in dict1.items() if v == min(dict1.values())]
            
            if min(dict1.values()) == 44:
                print('got 44')
            
            duplicate_rows = [count for count in Counter(x for x,y in [[k,v] for k,v in coordinates]) if Counter(x for x,y in [[k,v] for k,v in coordinates])[count] > 1]
            overlapping_rows = [elem for elem in coordinates if elem[0] in duplicate_rows]
            duplicate_cols = [count for count in Counter(y for x,y in [[k,v] for k,v in coordinates]) if Counter(y for x,y in [[k,v] for k,v in coordinates])[count] > 1]
            overlapping_cols = [elem for elem in coordinates if elem[1] in duplicate_cols]
            
            overlapping_rows_cols =  overlapping_rows + overlapping_cols
            
            nonoverlapping_coordinates = [coordinate for coordinate in coordinates if coordinate not in overlapping_rows_cols]
            
            coordinates_duplicates = [coordinate for coordinate in overlapping_rows if coordinate in overlapping_cols]
            
            entries = []
            if len(coordinates_duplicates) > 0:
                
                if len(coordinates_duplicates) > 1:
                    #Find those non overlapping duplicate tuples
                    non_overlap_duplicates = [elem for elem in coordinates_duplicates if elem[0] not in [k for k,v in coordinates_duplicates if elem != (k,v)] and elem[1] not in [v for k,v in coordinates_duplicates if elem != (k,v)]]
                    for c in non_overlap_duplicates:
                        overlapping_tuple_entries = [elem for elem in coordinates if elem[0] == c[0] or elem[1] == c[1]]
                        entries.append(overlapping_tuple_entries)
                        for entry in overlapping_tuple_entries:
                            overlapping_rows_cols.remove(entry)
                    
                        coordinates_duplicates = [c for c in coordinates_duplicates if c not in non_overlap_duplicates]
                
                [elem for elem in coordinates_duplicates if elem[0] in [k for k,v in coordinates_duplicates if elem != (k,v)] and elem[1] in [v for k,v in coordinates_duplicates if elem != (k,v)]]
                
                overlapping_row_col_entries = [elem for elem in coordinates if elem[0] in [k for k,v in coordinates_duplicates] or elem[1] in [v for k,v in coordinates_duplicates]]                
                entries.append(overlapping_row_col_entries)
                for entry in overlapping_row_col_entries:
                    overlapping_rows_cols.remove(entry)                
            else:
                #Merging the entries having similar index coordinates
                
                for row in duplicate_rows:
                    overlapping_row_entries = [elem for elem in coordinates if elem[0] == row]
                    entries.append(overlapping_row_entries)
                    for entry in overlapping_row_entries:
                        overlapping_rows_cols.remove(entry)
                
                for col in duplicate_cols:
                    overlapping_col_entries = [elem for elem in coordinates if elem[1] == col]
                    entries.append(overlapping_col_entries)
                    for entry in overlapping_col_entries:
                            overlapping_rows_cols.remove(entry)
                
                if len(overlapping_rows_cols) > 0:
                    for entry in overlapping_rows_cols:
                        entries.append([entry])             
            
            for i,j in nonoverlapping_coordinates:
                    elements = output[i] + [y[j] for x,y in enumerate(output)]
                    output[i][j] = max(elements) + 1
                    del dict1[i,j]
            
            for entry in entries:
                temp = []
                for row in entry: 
                    i,j = row                                                  
                    elements = output[i] + [y[j] for x,y in enumerate(output)]                
                    temp.append(max(elements) + 1)
                for row in entry:                        
                    i,j = row
                    # if (i,j) in dict1.keys(): 
                    output[i][j] = max(temp)
                    del dict1[i,j]
        return output
                
        

sln = Solution()
#sln.matrixRankTransform(matrix=[[7,3,6],[1,4,5],[9,8,2]])
# sln.matrixRankTransform(matrix=[[-49,-26,41,20,3,-42,25,44,-49,-6,21,-28,3],
#                                 [-50,13,28,-25,42,33,-8,-17,18,49,-36,-17,38],
#                                 [-11,40,43,-22,-43,-48,-5,6,13,-28,19,-38,-7],
#                                 [24,-45,-38,-19,-44,-37,46,-3,20,-1,38,41,28],
#                                 [23,18,5,-4,47,-18,29,12,3,-2,-7,16,-5],
#                                 [-30,-47,0,-25,-2,-19,32,-33,30,49,40,-37,38],
#                                 [-39,32,-29,-10,9,-12,43,-38,45,-24,-9,18,21],
#                                 [-12,35,-46,-31,-24,-1,-22,5,48,-13,2,-27,28],
#                                 [-5,-10,49,-24,39,26,9,8,27,-22,21,24,15],
#                                 [26,-31,-12,-45,46,21,36,47,-34,21,-20,43,10],
#                                 [5,-16,-17,10,9,8,-37,18,-39,40,39,-26,37],
#                                 [-28,-21,-38,-7,-4,-29,6,1,16,-45,34,5,-48],
#                                 [47,-30,-11,36,-49,-42,29,-40,-17,-14,-11,-20,35]])
# sln.matrixRankTransform(matrix=[[7,7],[7,7]])
# sln.matrixRankTransform(matrix=[[-32,15,38,17,-44,43,42,-47,-44,-41],
#                                 [34,-43,-24,7,-10,-43,36,-5,-22,37],
#                                 [4,-13,-38,49,16,-21,30,13,-20,47],
#                                 [2,-35,32,11,26,-31,40,31,-46,-7],
#                                 [4,19,18,-27,16,43,-10,-11,44,39],
#                                 [18,9,48,-29,30,5,8,-13,-42,-43],
#                                 [48,47,30,29,24,-29,22,-31,12,-37],
#                                 [38,-23,44,-13,-46,37,-12,31,14,-31],
#                                 [-28,23,-50,-23,12,23,18,-11,-44,31],
#                                 [-10,37,16,11,-18,17,40,-41,26,-31]])

# sln.matrixRankTransform(matrix=[[25,8,31,42,-39,8,31,-10,33,-44,7,-30,9,44,15,26],
#                                 [-3,-48,-17,-18,9,-12,-21,10,1,44,-17,14,-27,48,-21,-6],
#                                 [49,28,27,-18,-31,4,-13,34,49,48,47,-18,33,40,15,38],
#                                 [5,-28,-49,-38,1,32,-25,-50,29,-32,35,-46,-43,48,-49,-6],
#                                 [-27,-24,23,-14,-47,-12,7,6,25,-16,47,-26,13,-12,-33,-18],
#                                 [45,-48,3,-26,-23,-36,-17,38,17,12,15,46,37,40,47,26],
#                                 [-19,-24,-21,-2,-7,-48,47,30,5,-8,23,-46,21,-32,-33,-26],
#                                 [-27,32,27,-26,21,-32,-49,-10,5,20,-29,46,-43,-44,39,22],
#                                 [-43,48,27,26,-27,12,-1,-10,-27,12,-29,-34,41,-28,-25,-30],
#                                 [25,-36,35,-26,37,-20,31,14,-19,-40,-29,-2,-39,-28,11,46],
#                                 [49,-32,-29,-6,-47,32,-17,-18,-23,24,23,22,-47,-44,27,14],
#                                 [37,-44,-33,-18,-47,24,-17,-46,-43,-32,15,-46,-27,-8,-25,46],
#                                 [41,-40,31,-30,13,-24,-29,22,-15,-16,47,2,-39,4,-25,-42],
#                                 [-3,12,7,14,-7,8,-37,-34,-7,-12,39,-38,1,44,27,-34],
#                                 [-47,4,7,-2,-43,-32,27,2,-43,-8,-33,14,49,-48,-5,30],
#                                 [-15,8,-33,-26,-23,-32,-25,22,13,-20,-9,26,29,4,-1,2]])

sln.matrixRankTransform(matrix=[[28,-45,22,-27,4,11,-30,-15,-20,-25,2,-27,-32,23,26,-43,-12,47,-10,-39,-28,7,26,13,-32,-21,-6],
                                [-7,-32,-13,10,1,4,-49,-42,-47,16,23,30,49,-28,-9,-10,5,48,-45,-38,-23,36,-45,-6,37,40,-29],
                                [14,33,48,-5,38,-23,44,-21,-34,25,-12,-13,-10,-23,12,-9,-34,5,-8,27,-14,29,-8,39,-26,29,-40],
                                [-25,6,-43,-20,35,6,-11,-12,-13,-50,-35,44,-25,-30,-43,-32,-49,38,9,40,-29,-42,17,16,39,-50,-35],
                                [4,19,14,33,40,39,-42,-23,20,15,26,37,-4,19,-10,45,-12,-41,-10,-7,-28,-5,6,-11,-44,-1,-34],
                                [33,20,31,46,41,0,11,-30,-15,-24,-5,-38,-35,36,31,6,-19,40,-13,-30,-43,8,-1,6,41,-24,-9],
                                [-6,-7,16,-21,-10,-43,-20,-49,-46,-19,-16,15,-38,-35,-20,-37,-22,1,12,19,-2,-11,-4,-29,26,29,40],
                                [43,-18,-19,-4,19,-50,13,-40,-21,-42,-47,32,-17,46,-15,-44,43,46,-31,-4,-45,-18,-7,-8,47,-10,1],
                                [-32,-21,22,-43,-44,39,-2,-23,-28,47,-18,25,-20,-17,18,45,8,23,-42,9,-16,-21,6,-31,-16,-29,-6],
                                [-39,28,-33,-2,-19,8,-49,22,-15,16,31,18,-11,-48,35,-14,-15,-24,-25,-46,-31,40,39,42,-39,-36,15],
                                [-22,45,4,-33,-6,-47,-28,-45,-26,49,12,-49,46,-7,8,3,38,-39,-20,19,-10,33,40,39,42,33,0],
                                [-29,-14,-31,40,39,-26,45,-20,-9,-46,37,-40,3,-22,49,-28,-25,26,5,32,15,30,-23,-20,11,42,37],
                                [-24,-13,-14,-7,16,-29,-22,-47,-28,-33,-6,-19,48,-33,26,-35,-16,7,46,49,20,27,-14,-23,8,-9,-34],
                                [-27,16,35,-26,49,32,7,-6,49,20,-1,-42,21,32,-29,2,33,8,31,2,37,8,-21,2,-31,24,-17],
                                [-34,9,16,-5,-22,-23,20,-13,42,37,44,35,-14,37,24,-49,-10,33,-20,-45,22,33,12,-49,-6,-15,-40],
                                [-9,38,33,32,-41,30,5,-12,-41,22,-3,44,-13,-42,25,36,-1,34,13,44,-37,-18,-43,-12,43,46,29],
                                [-28,19,38,-31,0,-13,-6,25,-32,47,-30,13,0,-9,42,-27,4,43,34,29,36,31,30,-39,48,-13,22],
                                [-15,36,-49,26,29,-28,-5,46,37,44,-13,-18,-11,40,-37,-50,37,20,-45,-14,-27,0,43,-26,13,-20,-41],
                                [-14,21,40,-37,-38,-47,-12,-9,18,-11,-28,23,22,49,44,43,-30,-15,-12,11,38,37,-44,-13,-42,9,-12],
                                [-21,-6,49,12,-9,-38,-15,-40,-13,-22,-15,-8,47,46,-23,-48,3,22,-43,-4,-25,10,-23,28,-1,-18,-11],
                                [-44,-33,14,-27,-16,15,-38,17,-16,39,2,17,-28,39,38,-39,-4,-41,22,-27,48,-45,-6,-35,32,-37,-30],
                                [-35,4,-33,10,21,-32,43,22,37,-16,-17,-42,-31,-44,-41,22,-19,24,-5,-6,-23,44,-17,-42,49,-24,-49],
                                [2,-3,28,-49,26,-35,40,-5,38,41,-8,-41,-38,-31,-36,-29,-26,5,-16,-1,-30,41,12,-25,-46,-15,44],
                                [19,26,-39,-12,7,-10,21,-24,31,30,-3,48,31,42,1,-48,19,-38,-23,44,19,-6,-43,0,-13,22,9],
                                [-32,-37,-50,-23,-20,-41,22,45,-48,-33,-14,-39,40,35,-18,33,-40,31,26,9,20,-33,-14,5,8,3,-18],
                                [29,-20,43,-34,-3,40,27,26,-15,48,-29,-6,13,32,-5,42,13,4,15,18,-43,-20,27,14,1,-8,43],
                                [22,29,20,-49,22,5,48,-25,22,41,-44,-17,-30,21,44,-33,-6,-23,0,-49,-42,-27,4,-45,-6,1,44]])