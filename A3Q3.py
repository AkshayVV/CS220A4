import sys

contents = sys.stdin.read()


#Get distance from index to n-1
def find_distance(index, order, digraph):

    checked_nodes = [False] * order # Knowing which nodes have been checked
    distances = [0] * order # Keep track of all the distance from index
    nodes_to_check = [] # List for the nodes to check

    checked_nodes[index] = True
    nodes_to_check.append(index)

    while nodes_to_check != []:

        current_node = nodes_to_check.pop(0)

        if current_node == order-1:
            return distances[current_node]

        current_digraph = digraph[current_node].split()
        for node in current_digraph:
            node = int(node)
            if not checked_nodes[int(node)]:
                nodes_to_check.append(node)
                checked_nodes[node] = True
                distances[node] = distances[current_node] + 1

    return order

contents = contents.split("\n")
index = 0

while contents[index] != "0":

    order = int(contents[index]) # Getting the order of the current diagraph

    dist_zero = find_distance(0, order, contents[index+1:index+order+1]) # distance of 0 to n-1
    dist_one = find_distance(1, order, contents[index+1:index+order+1])  # distance of 1 to n-1
    distance = min(dist_zero, dist_one)
    idx = [dist_zero, dist_one].index(distance)
    print(idx, distance)

    index += order+1 # Going to the next digraph rotation#