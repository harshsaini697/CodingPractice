# Consider a matrix where each cell contains either a  or a  and any cell containing a  is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. In the diagram below, the two colored regions show cells connected to the filled cells. Black on white are not connected.
# #
# # Cells adjacent to filled cells:
# # If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to at least one other cell in the region but is not necessarily directly connected to all the other cells in the region.
# #
# # Regions: image
# # Given an  matrix, find and print the number of cells in the largest region in the matrix.
#Input
#4
# 4
# # 1 1 0 0
# # 0 1 1 0
# # 0 0 1 0
# # 1 0 0 0

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxRegion function below.
def maxRegion(grid):
    def size(i,j):
        if (0<=i<len(grid) and 0<=j<len(grid[i]) and grid[i][j]==1):
            grid[i][j]=0
            return 1+ sum(size(i2,j2) for i2 in range(i-1,i+2) for j2 in range(j-1,j+2))
        return 0
    return  max( size(i,j ) for i in range(len(grid)) for j in range(grid[i])

if __name__ == '__main__':
    n = 4
    m = 4
    grid = [
            [1, 1 ,0, 0],
            [0 ,1 ,1, 0],
            [0 ,0, 1, 0],
            [1 ,0 ,0, 0]
            ]

    res = maxRegion(grid)



