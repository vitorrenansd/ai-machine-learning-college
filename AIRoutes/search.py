class Search:
    def depth_first_search(self, graph, start, goal, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        print(f"Visiting: {start}")
        visited.add(start)
        path.append(start)

        if start == goal:
            return path
        
        for neighbor in graph.adjacency.get(start, []):
            if neighbor not in visited:
                result = self.depth_first_search(graph, neighbor, goal, visited, path[:])
                if result:
                    return result

        return None
    