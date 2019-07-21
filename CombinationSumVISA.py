def combinationSum( nums, target: int) :
    res = []
    dfs(nums, target, 0, [], res)
    return res


def dfs( nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        dfs(nums, target - nums[i], i, path + [nums[i]], res)

print(combinationSum([2,3,6,7],7))