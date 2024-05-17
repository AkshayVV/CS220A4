import sys
from collections import deque

def main():
    while True:
        limit = int(sys.stdin.readline().strip())
        if limit == 0:
            break

        digraph = []
        for _ in range(limit):
            line = sys.stdin.readline().strip().split()
            digraph.append([int(x) for x in line])

        overall_min = float('inf')
        for i in range(len(digraph)):
            distances = bfs(digraph, i)
            back_arcs = find_back_arcs(digraph, i)
            current_min = find_cycle(distances, back_arcs)

            if current_min < overall_min:
                overall_min = current_min

        if overall_min == float('inf'):
            print(0)
        else:
            print(overall_min)

def bfs(digraph, start):
    n = len(digraph)
    distances = [-1] * n
    queue = deque([start])
    distances[start] = 0

    while queue:
        u = queue.popleft()
        for v in digraph[u]:
            if distances[v] == -1:
                distances[v] = distances[u] + 1
                queue.append(v)

    return distances

def find_back_arcs(digraph, index_node):
    back_arcs = []
    for j in range(len(digraph)):
        if index_node in digraph[j]:
            back_arcs.append(j)
    return back_arcs

def find_cycle(distances, back_arcs):
    cycle_lengths = [distances[node] + 1 for node in back_arcs if distances[node] != -1]
    if cycle_lengths:
        return min(cycle_lengths)
    else:
        return float('inf')

main()
