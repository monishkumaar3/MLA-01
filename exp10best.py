import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def best_first_search(self, start, goal):
        visited = set()
        pq = [(0, start)]
        
        while pq:
            (cost, node) = heapq.heappop(pq)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                
                if node == goal:
                    print("\nGoal reached!")
                    return True
                
                for neighbor, weight in self.graph.get(node, []):
                    if neighbor not in visited:
                        heapq.heappush(pq, (weight, neighbor))
        print("\nGoal not reachable!")
        return False

# Example usage:
g = Graph()
g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'D', 8)
g.add_edge('C', 'E', 2)
g.add_edge('C', 'F', 4)
g.add_edge('F', 'G', 3)

print("Best-First Search Traversal:")
g.best_first_search('A', 'G')
