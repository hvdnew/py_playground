
class Node:

    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def search(self, target):

        if self.data == target:
            print('Found it!')
            return self
        
        if self.left and target < self.data:
            return self.left.search(target)
        
        if self.right and target > self.data:
            return self.right.search(target)
        
        print('Not found')
        return None
    
    def traversePreorder(self):
        print(self.data)
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()


    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.data)
        if self.right:
            self.right.traverseInorder()
        

    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()
        if self.right:
            self.right.traversePostorder()
        print(self.data)


class Tree:
    def __init__(self, root, name='') -> None:
        self.root = root
        self.name = name

    def search(self, data):
        return self.root.search(data)

    def traversePreorder(self):
        self.root.traversePreorder()

    def traverseInorder(self):
        self.root.traverseInorder()
    
    def traversePostorder(self):
        self.root.traversePostorder()



if __name__ == '__main__':

    node = Node(10,
                left=Node(5, 
                        left=Node(3), 
                        right=Node(7)),
                right=Node(15, 
                        left=Node(11), 
                        right=Node(17)))

    myTree = Tree(node, 'HDTree')

    print('traversePreorder')
    myTree.traversePreorder()

    print('traverseInorder')
    myTree.traverseInorder()

    print('traversePostorder')
    myTree.traversePostorder()
    

