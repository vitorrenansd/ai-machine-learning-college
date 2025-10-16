class AStar:
    def __init__(self, goal):
        self.goal = goal
        self.found = False

    def search(self, current):
        print(f"Current: {current.name}")
        current.visited = True

        if current == self.goal:
            self.found = True
        else:
            self.frontier = []
            for adj in current.adjacents:
                if adj.city.visited is False:
                    adj.city.visited = True
                    self.frontier.append(adj)
                    # sorting the list by distance to Curitiba
                    self.frontier = sorted(self.frontier, key=lambda adj: adj.final_distance)
            print(self.frontier)
            print()
            if self.frontier[0] is not None:
                AStar.search(self, self.frontier[0].city)
