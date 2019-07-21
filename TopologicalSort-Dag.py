"""
Given a list of packages that need to be built and the dependencies for each package,
determine a valid order in which to build the package.
eg.
0:
1:0
2:0
3:1,2
4:3

o/p : 0,1,2,3,4


Ans: Topological Sort

dfs(node):
    visited=set([])
    for neigh in items.neigh:
        if not visited:
        dfs(neigh)
    item.visited
    result.append(item)

"""

from collections import defaultdict

def package_dependencies(dependencies):

    visited=set([])
    visiting=set([])
    result=[]
    def dfs(node):
        visiting.add(node)
        for neighbor in dependencies[node]:
            if neighbor in visiting:
                raise Exception( "Cycle Detected")
            if neighbor not in visited:
                dfs(neighbor)
        visited.add(node)
        visiting.remove(node)
        result.append(node)

    for nodes in dependencies.keys():
        dfs(nodes)
    return result

mapping={
    0: [],
    1: [0],
    2: [0],
    3: [1,2],
    4: [3]

}
print(package_dependencies(mapping))
