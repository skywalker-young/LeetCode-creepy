"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Note: m and n will be at most 100.


""" 
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        table = [[0 for x in range(n)] for x in range(m)]
        for i in range(m):
            table[i][0] = 1
        for i in range(n):
            table[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = table[i-1][j] + table[i][j-1]
        return table[m-1][n-1]






"""

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

"""


class Solution:
 def uniquePathsWithObstacles(self, obstacleGrid):
    if not obstacleGrid:
        return 
    r, c = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    dp[0][0] = 1 - obstacleGrid[0][0]
    for i in range(1, r):
        dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
    for i in range(1, c):
        dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])
    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])
    return dp[-1][-1]
    
