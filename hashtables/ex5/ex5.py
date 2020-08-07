# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    # create a cache
    cache = {}
    # create array to hold final result
    result = []

    # loop through queries, if not in cache add it
    for query in queries:
        if query not in cache:
            cache[query] = query

    # split file names by /
    # loop through file names

    for file in files:
        split_file = file.split('/')
        # if we find part of the file name in cache, we add it to result
        for frag in split_file:
            if frag in cache:
                result.append(file)

    return result


if __name__ == "__main__":
    files = ['/bin/foo', '/bin/bar', '/usr/bin/baz']
    queries = ["foo", "qux", "baz"]
    print(finder(files, queries))
