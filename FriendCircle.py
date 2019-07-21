class Friends:
    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    def findCircleNum( M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        parents = [-1] * len(M)

        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1 and i != j:
                    Friends.union(parents, i, j)

        return sum([x == -1 for x in parents])


    def find( parents, i):
        if parents[i] == -1:
            return i
        return Friends.find(parents, parents[i])


    def union(parents, a, b):
        rootA = Friends.find(parents, a)
        rootB = Friends.find(parents, b)
        if rootA != rootB:
            parents[rootA] = rootB

M = [[1, 1, 0],[1, 1, 0],[0, 0, 1]]

print(Friends.findCircleNum(M))