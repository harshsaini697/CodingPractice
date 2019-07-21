def findLargestSumPair(numbers):
    n=len(numbers)
    if n<1:
        return 0
    if n ==1:
        return (numbers[0])
    if numbers[0] > numbers[1]:
        first = numbers[0]
        second = numbers[1]

    else:
        first = numbers[1]
        second = numbers[0]
    for i in range(2, n):
        if numbers[i] > first:
            second = first
            first = numbers[i]
        elif numbers[i] > second :
            second = numbers[i]

    return (first + second)

numbers = [5,9,9,9]
n = len(numbers)
print(findLargestSumPair(numbers))