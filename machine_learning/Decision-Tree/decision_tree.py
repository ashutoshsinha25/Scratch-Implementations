import math
from tree_node import TreeNode 


class buildTree:

    def __init__(self):
        self.__root =  None 
    
    def frequency_count(self, Y):
        count = {}
        for i in Y:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        return count 

    def entropy(self, Y):
        freq = self.frequency_count(Y)
        ent = 0
        total = len(Y)
        for i in freq:
            p = freq[i] / total 
            ent += (-p)*math.log(p)
        return ent 
    
    def gain_ration(self, X, Y, selected_features):
        pass 