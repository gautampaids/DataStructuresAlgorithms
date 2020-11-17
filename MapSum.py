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
            self.root = MapSum.TrieNode()
        
        def insert(self, word, value):
            '''
            Inserts word into a trie
    
            Parameters
            ----------
            word : TYPE
                DESCRIPTION.
            value : TYPE
                DESCRIPTION.
    
            Returns
            -------
            None.
    
            '''
            currentValue = self.getWordValue(word)
            diff = value - currentValue
            
            currentNode = self.root
            for char in word:
                if char not in currentNode.edgenodes:
                    currentNode.edgenodes[char] = MapSum.TrieNode()
                currentNode = currentNode.edgenodes[char]
                currentNode.prefixSum += diff
            
            currentNode.iswordend = True
            currentNode.value = value
        
        def getWordValue(self, word):
            currentNode = self.root
            for c in word:
                if c not in currentNode.edgenodes:
                    return 0
                currentNode = currentNode.edgenodes[c]
            return currentNode.value
    
        def getPrefixSum(self, prefix):
            currentNode = self.root
            for c in prefix:
                if c not in currentNode.edgenodes:
                    return 0
                currentNode = currentNode.edgenodes[c]
                
            return currentNode.prefixSum
    
    def __init__(self):
        #self.trieNode = self.TrieNode()
        self.trie = self.Trie()
        
    def insert(self,key,value):
        self.trie.insert(key,value)
    
    def sum(self, prefix):
        return self.trie.getPrefixSum(prefix)
    

mapSum = MapSum()
mapSum.insert("apple", 3)
mapSum.sum("ap")
mapSum.insert("app", 2)
mapSum.sum("ap")
     
    