

class TreeNode:

    def __inti__(self, data, output):
        self.output = output
        self.data = data 
        self.children = {}
        self.index = -1
    
    def add_child(self, feature_value, object):
        self.children[feature_value] = object