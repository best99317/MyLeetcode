class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insertLeft(self, newVal):
        if self.left is None:
            self.left = TreeNode(newVal)
        else:
            temp = TreeNode(newVal)
            temp.left = self.left
            self.left = temp

    def insertRight(self, newVal):
        if self.right is None:
            self.right = TreeNode(newVal)
        else:
            temp = TreeNode(newVal)
            temp.right = self.right
            self.right = temp


class BinaryTree:
    def __init__(self, val):
        self.root = TreeNode(val)

    def preOrder(self, root):
        if root:
            print(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.val)

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.val)
            self.inOrder(root.right)

class BinaryHeap():
    def __init__(self):
        self.heapList = [0]
        self.curSize = 0

    def insert(self, val):
        def percUp(i):
            while i // 2 > 0:
                if self.heapList[i] < self.heapList[i // 2]:
                    temp = self.heapList[i // 2]
                    self.heapList[i // 2] = self.heapList[i]
                    self.heapList[i] = temp
                i // 2

        self.heapList.append(val)
        self.curSize += 1
        percUp(self.curSize)

