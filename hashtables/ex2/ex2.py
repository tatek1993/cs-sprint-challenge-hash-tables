#  Hint:  You may not need all of these.  Remove the unused functions.

# we have a list of tickets

# create a cache and route array
# for ticket in tickets, if ticket.source == None
## route[0] = ticket.desitnation
# current = route[i]

# for ticket in tickets -> add to cache key=source, destination=value

# for current:
## if cache[key] == current -> route.append(cache.value)
# current += 1


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = []

    for ticket in tickets:
        if ticket.source == "NONE":
            route.append(ticket.destination)
    current = route[len(route) - 1]

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    while current != "NONE":
        route.append(cache[current])
        current = route[len(route) - 1]

    print(route)
    return route
