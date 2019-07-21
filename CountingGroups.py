class Groups:
    def findCircle(M):
        N=len(M)
        seen=set()
        def dfs(node):
            for i, j in enumerate(M[node]):
                if i and j not in seen:
                    seen.add(i)
                    dfs(i)
        ans=0
        for i in range(0,N):
            if i not in seen:
                dfs(i)
                ans+=1
        return ans

if __name__ == '__main__':



    M=[[1,1,0],
       [1,1,0],
       [0,0,1]]
    Groups.findCircle(M)