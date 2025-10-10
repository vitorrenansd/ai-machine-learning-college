class GreedySearch:
    def __init__(self, goal):
        self.goal = goal
        self.found = False

    def search(self, current):
        print(f"Current: {current.name}")

        if current == self.goal:
            self.found = True
        else:
            self.frontier = []
            for adj in current.adjacents:
                if adj.city.visited == False:
                    adj.city.visited = True
                    self.frontier.append(adj.city)

                    ## sorting the list by distance to the goal (e.g., Curitiba)
                    self.frontier = sorted(self.frontier, key=lambda city:city.goal_distance)
            print(f"{self.frontier} \n")
            if self.frontier[0] is not None:
                GreedySearch.search(self, self.frontier[0])
