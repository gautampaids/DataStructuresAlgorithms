# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 19:04:09 2020

@author: Gautam_Pai
"""


class MapSum(object):
    
    class TrieNode:
        def __init__(self):
            self.edgenodes = {}
            self.iswordend = False
            self.value = 0
            self.prefixSum = 0
    
    class Trie:
        def __init__(self):
            self.root = TrieNode()
    
        def insert(self, word):
            '''
            Inserts word into a trie

            Parameters
            ----------
            word : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            currentNode = self.root
            for char in word:
                if char not in currentNode.edgenodes:
                    currentNode.edgenodes[char] = TrieNode()
                currentNode = currentNode.edgenodes[char]
            
            currentNode.iswordend = True
        
        def search(self, word):
            '''
            Returns true if word is in the trie

            Parameters
            ----------
            word : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            currentNode = self.root
            for char in word:
                if char not in currentNode.edgenodes:
                    return False
                currentNode = currentNode.edgenodes[char]
            
            return currentNode.iswordend
        
        # def getWordValue(self, word):
        #     currentNode = self.root
        #     for c in word:
        #         if !currentNode.edgenodes
    

trie = Trie()
trie.insert("CANARY")
trie.insert("CANDLE")         
    