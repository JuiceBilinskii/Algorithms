def find_dist(graph_, start, goal):
    visited = {start: 0}
    queue = [start]

    while goal not in visited or queue:
        for vertice in graph_[queue[0]]:
            if vertice not in visited:
                visited[vertice] = visited[queue[0]] + 1
                queue.append(vertice)
        queue.pop(0)
    return visited[goal]





graph = {
    'cab': ('cat', 'car'),
    'cat': ('mat', 'bat'),
    'car': ('cat', 'bar'),
    'mat': ('bat',),
    'bar': ('bat',),
    'bat': tuple(),
}

weighted_graph = {}

print(find_dist(graph, 'cab', 'car'))
