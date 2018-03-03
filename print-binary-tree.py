# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        rows = get_height(root)
        cols = 2 ** rows - 1
        res = [['' for _ in range(cols)] for _ in range(rows)]

        def traverse(node, level, pos):
            if not node:
                return
            left_padding, spacing = 2 ** (rows - level - 1) - 1, 2 ** (rows - level) - 1
            index = left_padding + pos * (spacing + 1)
            print(level, index, node.val)
            res[level][index] = str(node.val)
            traverse(node.left, level + 1, pos << 1)
            traverse(node.right, level + 1, (pos << 1) + 1)
        traverse(root, 0, 0)
        return res
        
        '''
        This question involves quite a bit of math. It would help if you are familiar with the math involved for Binary Trees. Let’s recap some of the formulas involved:

Given a Binary Tree of height H:

The maximum total number of nodes is = 2^H - 1
Number of nodes at each level, L (0-indexed) = 2^L
We can view the final output as a 2-D matrix, where the number of rows is the height of the tree and the number of columns will be the 2^H - 1.

Taking this tree as example:

        1
      /   \
    2      3
   /  \    / \
  4   5   6   7
 / \
8   9
Our final matrix should look like this:

.......1....... <- Level 0, Left padding: 7, Spacing: 15
...2.......3... <- Level 1, Left padding: 3, Spacing: 7
.4...5...6...7. <- Level 2, Left padding: 1, Spacing: 3
8.9............ <- Level 3, Left padding: 0, Spacing: 1
The height is 4 and based on our calculations, the number of rows = 4, number of cols = 2^4 - 1 = 15. So we can directly initialize a 2-D matrix of size 4 x 15. We can observe that for each row, the first node has a left padding = 2^(H-L-1) - 1 and the space between each node is 2^(H-L) - 1.

With these formulas derived, the next task is to calculate the position of node in each row and we can do that as we traverse the tree. The position of each node in its own row can be represented by a number in its binary form, which can be obtained from the left/right paths taken from the root. Taking the node 6 in the tree above, 6 is found via root->right->left. The root node has number of 0. Each time we move to a left child, append 0 to the binary representation (multiply the number by 2). Each time we move to a right child, append 1 to the binary representation (multiply the number by 2 and add 1). Let’s have a look at some examples:

Node 6 is root->right->left = 0b10 and its position within row = (0*2+1)*2 = 2
Node 7 is root->right->right = 0b11 and its position within row = ((0*2+1)*2+1) = 3
Node 9 is root->left->left->right = 0b001 and its position within row = (((0*2)*2)*2+1) = 1

Representing the above tree in its binary form:

         0
       /    \
      0      1
    /  \    / \
   00  01  10  11
  /  \
000   001
Nodes 6 and 7 are index 2 and 3 in their rows.

As we traverse the tree, we will have the row and the position in the row of each node. Hence we can fill in the matrix with the node values based on the left padding and spacing in each row.
        
        '''
