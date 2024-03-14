from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = defaultdict(bool)
        self.dfs_util(start, visited)

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS Traversal:")
g.dfs(2)
