def dijkstras_algorithm(graph, start, goal):
    costs = graph[start].copy()
    parents = {k: start for k in graph[start]}
    for node in set(graph) - set(graph[start]):
        costs[node] = float('inf')
        parents[node] = None

    accessed = [start]

    def find_lowest_cost_node():
        nonlocal costs
        nonlocal accessed

        lowest_cost = float('inf')
        lowest_cost_node = None
        for node_, cost in costs.items():
            if node_ not in accessed and cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_node = node_
        return lowest_cost_node

    node = find_lowest_cost_node()
    while node is not None:
        for neighbour in graph[node]:
            new_cost = costs[node] + graph[node][neighbour]
            if new_cost < costs[neighbour]:
                costs[neighbour] = new_cost
                parents[neighbour] = node
        accessed.append(node)
        node = find_lowest_cost_node()

    return costs, parents


# weighted_graph = {
#     'Start': {'A': 5, 'B': 2},
#     'A': {'C': 4, 'D': 2},
#     'B': {'A': 8, 'D': 7},
#     'C': {'D': 6, 'Fin': 3},
#     'D': {'Fin': 1},
#     'Fin': {},
# }

# weighted_graph = {
#     'Start': {'A': 10},
#     'A': {'B': 20},
#     'B': {'C': 1, 'Fin': 30},
#     'C': {'A': 1},
#     'Fin': {},
# }

weighted_graph = {
    'Start': {'A': 2, 'B': 2},
    'A': {'B': 2},
    'B': {'C': 2, 'Fin': 2},
    'C': {'A': -1, 'Fin': 2},
    'Fin': {},
}

start, goal = 'Start', 'Fin'
costs, parents = dijkstras_algorithm(weighted_graph, start, goal)

path = [goal]
node = parents[goal]
while node is not None:
    path.append(node)
    node = parents[node]
print(path[::-1])
print(costs[goal])