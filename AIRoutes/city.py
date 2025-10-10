class City:
    def __init__(self, name, goal_distance):
        self.name = name
        self.adjacents = []
        self.visited = False
        self.goal_distance = goal_distance

    def __repr__(self):
        return f"{self.name} (h={self.goal_distance})"

    def add_adjacent_city(self, city):
        self.adjacents.append(city)
