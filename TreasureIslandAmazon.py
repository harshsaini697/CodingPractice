input1=[
['O', 'O', 'O', 'O'],
['D', 'O', 'D', 'O'],
['O', 'O', 'O', 'O'],
['X', 'D', 'D', 'O']]


def searchMatrix(self, matrix) -> bool:
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])

    # binary search
    left, right = 0, m * n - 1
    while left <= right:
        pivot_idx = (left + right) // 2
        pivot_element = matrix[pivot_idx // n][pivot_idx % n]
        if 'X' == pivot_element:
            return
        else:
            if 'X' < pivot_element:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1
    return False