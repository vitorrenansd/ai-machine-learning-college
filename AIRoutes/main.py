from graph import Graph
from search import Search

g = Graph()
s = Search()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("B", "E")
g.add_edge("C", "F")
g.add_edge("E", "F")

g.print_graph()

path = s.depth_first_search(g, "A", "D")
print("Path found: ", path)
