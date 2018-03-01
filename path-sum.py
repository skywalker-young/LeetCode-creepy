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
