def depth_first_search(graph: dict, vertex: int, visited: list) -> list:
    visited[vertex] = True
    visited_vertices = [vertex]

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            visited_vertices.extend(depth_first_search(graph, neighbor, visited))

    return visited_vertices

graph = {
    0: [1, 2],  # Vertex 0 is connected to vertices 1 and 2
    1: [0, 3, 4],  # Vertex 1 is connected to vertices 0, 3, and 4
    2: [0],  # Vertex 2 is connected to vertex 0
    3: [1],  # Vertex 3 is connected to vertex 1
    4: [1, 5],  # Vertex 4 is connected to vertices 1 and 5
    5: [4]  # Vertex 5 is connected to vertex 4
}

visited = [False] * len(graph)
print("Visited vertices (in order of searched):")
print(depth_first_search(graph, 0, visited))
