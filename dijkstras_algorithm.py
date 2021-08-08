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

    print(costs)
    print(parents)


weighted_graph = {
    'Start': {'A': 6, 'B': 2},
    'A': {'Fin': 1},
    'B': {'A': 3, 'Fin': 5},
    'Fin': {},
}

dijkstras_algorithm(weighted_graph, 'A', 'Fin')
