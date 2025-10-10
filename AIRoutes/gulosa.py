class Gulosa:
    def __init__(self, goal):
        self.goal = goal
        self.find = False

    def search(self, current):
        print(f"Current: {current.name}")

        if current == self.goal:
            self.find = True
        else:
            self.fronteira = []
            for adj in current.adjacents:
                if adj.city.visited == False:
                    adj.city.visited = True
                    self.fronteira.append(adj.city)

                    # ordenando a lista pela distancia ate curitiba
                    self.fronteira = sorted(self.fronteira, key=lambda city:city.goal_distance)
            print(self.fronteira)
            if self.fronteira[0] is not None:
                Gulosa.search(self, self.fronteira[0])
