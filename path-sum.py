#########################You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
不一定从根部开始，但是必须往下走
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
###############################
   
   def helper(self, root, target, so_far, cache):
        if root:
            complement = so_far + root.val - target
            if complement in cache:
                self.result += cache[complement]
            cache.setdefault(so_far+root.val, 0)
            cache[so_far+root.val] += 1
            self.helper(root.left, target, so_far+root.val, cache)
            self.helper(root.right, target, so_far+root.val, cache)
            cache[so_far+root.val] -= 1
        return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.helper(root, sum, 0, {0:1})
        return self.result
        
        
        ##########################
        Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
        这个必须从根部开始
        
        ########################
class Solution(object):
 def pathSum(self, root, sum):
    if not root: return []
    if root.left == None and root.right == None:
        if sum == root.val: 
            return [[root.val]]
        else: 
            return []
    a = self.pathSum(root.left, sum - root.val) + \
        self.pathSum(root.right, sum - root.val)
    return [[root.val] + i for i in a]
########################找到并输出符合指定值的数字，从根部往下走
class Solution:


# @param {TreeNode} root
# @param {integer} sum
# @return {integer[][]}
 def pathSum(self, root, sum):
    ans = []
    self.dfs(root, sum, [], ans)
    return ans


 def dfs(self, root, sum, tmp, ans):
    if not root:
        return

    if root.left == None and root.right == None and sum == root.val:
        ans.append(tmp + [root.val])
        return

    self.dfs(root.left, sum - root.val, tmp + [root.val], ans)
    self.dfs(root.right, sum - root.val, tmp + [root.val], ans)

bb=[5,4,8,11,None,13,4,7,2,None,None,None,1]
a=TreeNode(5)


a.left=TreeNode(4)
a.right =TreeNode(8)
a.left.left =TreeNode(11)
a.left.right =TreeNode(0)
a.left.left.left =TreeNode(7)
a.left.left.right =TreeNode(2)
a.right.left =TreeNode(13)
a.right.right =TreeNode(4)
a.right.right.right =TreeNode(1)
a.right.right.left =0
a.right.left.left =TreeNode(99)
a.right.left.right =TreeNode(0)


b=Solution()
c=b.pathSum(a,22)
print(c)
