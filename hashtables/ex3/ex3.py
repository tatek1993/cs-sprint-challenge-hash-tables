# We're given a list of lists that contain integers:
# And we need to compute the numbers that exist in all lists.

# we need to know the length of list
# create cache and result array

# for each num in list[i] -> append to cache -> cache[num] = num
## if num already in cache -> cache[num] += 1

# for each num in cache
## if count == list.length -> append to result


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    result = []

    for array in arrays:
        for num in array:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1

    for num in cache:
        if cache[num] == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
