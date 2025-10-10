class City:
    def __init__(self, name):
        self.name = name
        self.adjacents = []
        self.visited = False
        self.goal_distance = None

    def add_adjacent_city(self, city):
        self.adjacents.append(city)
