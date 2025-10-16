class Adjacent:
    def __init__(self, city, distance):
        self.city = city
        self.distance = distance
        self.final_distance = self.distance + self.city.goal_distance
