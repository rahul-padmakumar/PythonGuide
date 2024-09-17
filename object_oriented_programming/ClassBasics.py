
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x_portion = (self.coor2[0] - self.coor1[0]) ** 2
        y_portion = (self.coor2[1] - self.coor1[1]) ** 2
        return (x_portion + y_portion) ** 0.5

    def slop(self):
        x_diff = self.coor2[0] - self.coor1[0]
        y_diff = self.coor2[1] - self.coor1[1]
        return y_diff / x_diff


coordinate1 = (3, 2)
coordinate2 = (8, 10)
line = Line(coordinate1, coordinate2)
print(line.distance())
print(line.slop())


