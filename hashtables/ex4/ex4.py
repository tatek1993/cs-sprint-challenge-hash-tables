# make a cache
# make a result array

# in a
## add each number which is > 0 to cache
## loop through a
## if number * -1 is in cache, append to result array


def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for num in a:
        if num > 0:
            cache[num] = num
    for num in a:
        if num * -1 in cache:
            result.append(num * -1)

    print(result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
