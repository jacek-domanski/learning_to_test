from point import Point


class Polygon:
    def __init__(self, points=list()):
        if len(points) < 3:
            raise Exception('At least 3 points are needed to create a polygon')
        self.points = points

    def add_point(self, point):
        self.points.append(point)

    def circumference(self):
        sum = 0

        for a, b in zip(self.points[:-1], self.points[1:]):
            sum += a-b
        sum += self.points[0]-self.points[-1]

        return sum
