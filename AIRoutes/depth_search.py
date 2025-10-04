from stack import Stack

class DepthSearch:
    def __init__(self, start, goal):
        self.start = start
        self.start.visited = True
        self.goal = goal
        self.stack = Stack(30)
        self.stack.push(start)
        self.found = False

    def search(self):
        top = self.stack.get_top()
        print(f"Top: {top.name}")

        if top == self.goal:
            self.found = True
        else:
            for adjacent in top.adjacents:
                if not self.found:
                    print(f"Checking if already visited: {adjacent.city.name}")
                    if not adjacent.city.visited:
                        adjacent.city.visited = True
                        self.stack.push(adjacent.city)
                        # Call recursion
                        DepthSearch.search(self)

        # Pop from stack
        print(f"Popped {self.stack.pop().name}")
