class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_edge(self, origin, destination):
        if origin not in self.adjacency:
            self.adjacency[origin] = []
        if destination not in self.adjacency:
            self.adjacency[destination] = []
        self.adjacency[origin].append(destination)

    def print_graph(self):
        for node, neighbors in self.adjacency.items():
            print(f"{node} -> {', '.join(neighbors)}")
