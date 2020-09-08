from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        dist_x = other.x - self.x
        dist_y = other.y - self.y

        return sqrt(pow(dist_x, 2) + pow(dist_y, 2))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

if __name__ == '__main__':
    pt_a = Point(0, 0)
    pt_b = Point(3, 4)
    print(pt_a-pt_b)