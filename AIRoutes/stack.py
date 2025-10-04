class Stack:
    def __init__(self, size):
        self.size = size
        self.cities = [None] * self.size
        self.top = -1

    def push(self, city):
        self.top += 1
        self.cities[self.top] = city

    def pop(self):
        temp = self.cities[self.top]
        self.top -= 1
        return temp

    def get_top(self):
        return self.cities[self.top]
