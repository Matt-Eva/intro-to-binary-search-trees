# Python code for a self-balancing binary search tree.

class Node:

    def __init__(self, val):
        self.val
        self.left = None
        self.right = None
        self.parent = None
        self.left_height = 0 #vals for right_height and left_height can be >= 0, <= 2
        self.right_height = 0
    
    def search(self, val):
        if self.val == val:
            return true
        if val > self.val and self.right == None:
            return false
        elif val > self.val:
            return self.right.search(val)
        elif val < self.val and self.left == None:
            return false
        else:
            return self.left.search(val)
        

    def insert(self, val, traversal):
        if val >= self.val:
            if self.right == None:
                right_node = Node(val)
                right_node.parent = self
                self.right = right_node
                self.right_height +=1
                self.parent.right_height += 1
                if (self.parent.right_height - self.parent.left_height > 1):
                    self.parent.rotate_left()
                    return traversal - 1
                return traversal
            return self.right.insert(val, traversal + 1)
        if self.left == None:
            left_node = Node(val)
            left_node.parent = self
            self.left = left_node
            self.left_height +=1
            self.parent.left_height +=1
            if (self.parent.left_height - self.parent.right_height > 1):
                self.parent.rotate_right()
                return traversal - 1
            return traversal
        return self.left.insert(val, traversal + 1)
        
        def rotate_right(self):
            super_parent = self.parent
            new_parent = self.left
            new_parent.parent = super_parent
            self.parent = new_parent
            if new_parent.right == None:
                new_parent.right = self
                self.left = None
            else:
                new_parent_node.right.parent = self
                self.left = new_parent_node.right
                new_parent_node.right = self


        def rotate_left(self):
            super_parent = self.parent
            new_parent = self.right
            new_parent.parent = super_parent
            self.parent = new_parent
            if new_parent.left == None:
                new_parent.left = self
                self.right = None
            else:
                new_parent.left.parent = self
                self.right = new_parent.left
                new_parent.left = self

class BSTree:

    def __init__(self):
        self.root = None
        self.left_height = 0
        self.right_height = 0

    def search(self, val):
        if self.root == None:
            return false
        return self.root.search(val)

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
            return
        traversal_height = self.root.insert(val)
        if val >= self.root.val:
            if traversal_height > self.right_height:
                self.right_height = traversal_height
            if (self.right_height - self.left_height) > 1:
                self.rotate_left()
        else:
            if traversal_height > self.left_height:
                self.left_height = traversal_height
            if (self.left_height - self.right_height) >1:
                self.rotate_right()


    def rotate_right(self):
        current_root = self.root
        new_root = current_root.left
        self.root = new_root
        current_root.parent = new_root
        if new_root.right == None:
            new_root.right = current_root
            current_root.left = None
        else:
            current_root.left = new_root.right
            new_root.right = current_root
        self.left_height -= 1
        self.right_height += 1

    def rotate_left(self):
        current_root = self.root
        new_root = current_root.right
        self.root = new_root
        current_root.parent = new_root
        if new_root.left == None:
            new_root.left = current_root
            current_root.right = None
        else:
            current_root.right = new_root.left
            new_root.left = current_root
        self.right_height -= 1
        self.left_height += 1
