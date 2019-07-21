# class Solution(object):
#     def reachingPoints( sx, sy, tx, ty):
#         while tx >= sx and ty >= sy:
#             if sx == tx and sy == ty: return True
#             if tx > ty:
#                 tx -= ty
#             else:
#                 ty -= tx
#         return False
# print(Solution.reachingPoints(6,
# 3,
# 6,
# 15))
