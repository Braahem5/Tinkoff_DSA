# Graph Theroy
from collections import deque

matrix = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 1],
]

list_Adjacency = [
    [1, 3],
    [2, 3],
    [0, 1],
    [1, 3],
]


def BFS(graph, start_node):
    Queue = deque([start_node])
    Visited = []

    while Queue:
        current_element = Queue.pop(0)
        if current_element not in Visited:
            Visited.append(current_element)
            Queue.extend(graph[current_element])
    return Visited


def DFS(graph, start_node):
    stack = [start_node]
    visited = []

    while stack:
        current_element = stack.pop()
        if current_element not in visited:
            visited.append(current_element)
            for neighbor in graph[current_element]:
                if neighbor not in visited:
                    visited.append(neighbor)
    return visited


def dfs_iterative_adj_matrix(matrix, start):
    visited = set()
    stack = [start]  # Initialize stack with the starting node

    while stack:
        node = stack.pop()  # Pop the top node

        if node not in visited:
            visited.add(node)
            print(f"Visiting node {node}")

            # Check all possible neighbors (columns in the matrix row)
            for neighbor in reversed(range(len(matrix[node]))):
                if matrix[node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return visited


# Example usage
visited_nodes = dfs_iterative_adj_matrix(matrix, 0)
print("Visited nodes:", visited_nodes)

# Run DFS starting from node 0
print(DFS(list_Adjacency, 0))  # Output: [0, 3, 1, 2]
