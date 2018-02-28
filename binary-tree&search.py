class BinaryTree:
    def __init__(self,item):
        self.key=item
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self,item):
        if self.leftChild==None:
            self.leftChild = BinaryTree(item)
        else:
            t=BinaryTree(item)
            t.leftChild=self.leftChild
            self.leftChild=t

    def insertRight(self,item):
        if self.rightChild==None:
            self.rightChild=BinaryTree(item)
        else:
            t=BinaryTree(item)
            t.rightChild=self.rightChild
            self.rightChild=t



tree=BinaryTree('ka')
tree.insertLeft('bili')
tree.insertRight('ccc')
tree.leftChild.insertLeft('aa')
tree.leftChild.insertRight('bb')
tree.rightChild.insertLeft('right1')
tree.rightChild.insertRight('right2')
def levelSearch(tree):
    if not tree:
        return
    queue=[]
    queue.append(tree)
    while (len(queue))!=0:
        node=queue.pop(0)
        if node.leftChild:
            queue.append(node.leftChild)
        if node.rightChild:
            queue.append(node.rightChild)
        print(node.key)

levelSearch(tree)


def levelOrder(tree):
     if tree is None:
         return []
     q=[tree]
     output=[]
     while len(q):
         level =[]
         for x in q:
             level.append(x.key)
         output.append(level)
         q2=[]
         for x in q:
             if x.leftChild is not None:
                 q2.append(x.leftChild)
             if x.rightChild is not None:
                q2.append(x.rightChild)
         q=q2

     return print (output)


levelOrder(tree)


###############################把array变成树
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root
