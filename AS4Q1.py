import sys
def main():
    limit = int(sys.stdin.readline().strip())
    overall_min = 0
    while limit != 0:
        digraph = []
        for i in range(limit):
            number = sys.stdin.readline().split()
            number = [int(x) for x in number]
            digraph.append(number)
        for i in range(len(digraph)):
            index_node = i
            back_arc_array = back_arc_find(digraph, index_node)
            distance_array = distance(digraph)
            current_min = find_cycle(distance_array, back_arc_array, digraph, index_node)
        if current_min < overall_min:
            overall_min = current_min
        print(overall_min)
        limit = int(sys.stdin.readline().strip())
        
 
   # for loop global i = 0
   # gloabl_current_min = 0
   
    
 
def distance(digraph):
    for i in range(len(digraph)):
        d_list = breadth_first_visit(digraph, i)
    return d_list
 
def back_arc_find(digraph, index_node):
    array = []
    for j in range(len(digraph)):
        for arc in digraph[j]:
            if index_node == arc:
                array.append(index_node)
    return array
 
def breadth_first_visit(digraph, s):
    queue = []
    colour = ["W"] * len(digraph)
    pred = [None] * len(digraph)
    d = [None] * len(digraph)
    colour[s] = "G"
    d[s] = 0
    queue.append(s)
    while not len(queue) == 0:
        u = queue[0]
        a_list = digraph[u]
        for v in a_list:
            if colour[v] == "W":
                colour[v] = "G"
                pred[v] = u
                d[v] = d[u] + 1
                queue.append(v)
        queue.pop(0)
        colour[u] = "B"  
    return d
 
def find_cycle(distance, back_arc_array, digraph, i):
    empty_array = []
    for node in back_arc_array:
        empty_array.append(distance[node])
    print(empty_array)
    return min(empty_array) + 1
 
main()
