import math

class Vector2(object):
    def __init__(self, x, y) -> object:
        self.x = x
        self.y = y
        self.magnitude = math.sqrt(self.x**2+self.y**2)

    def add(self, v2):
        self.x += v2.x
        self.y += v2.y

    def subtract(self, v2):
        self.x -= v2.x
        self.y -= v2.y

    def multiply(self, s1):
        self.x *= s1
        self.y *= s1

    def divide(self, s1):
        if s1!=0:
            self.x /=s1
            self.y /=s1
        else:
            print("Dividing by zero in physics.vector2.Vector2.divide.")
        return Exception

#OPTIMIZATION - sqrt is expensive
def dist_no_sqrt(v1, v2):
    return (v1.x-v2.x)**2+(v1.y-v2.y)**2

def dist(v1, v2):
    return math.sqrt((v1.x-v2.x)**2+(v1.y-v2.y)**2)

def add(v1, v2):
    return Vector2(v1.x+v2.x, v1.y+v2.y)

def subtract(v1, v2):
    return Vector2(v1.x - v2.x, v1.y - v2.y)

def abs(v1):
    return Vector2(abs(v1.x), abs(v1.y))

def divide(v1, s1):
    if s1!=0:
        return Vector2(v1.x/s1, v1.y/s1)
    else:
        print("Dividing by zero in physics.vector2.divide.")
    return Exception

def multiply(v1, s1):
    return Vector2(v1.x*s1, v1.y*s1)

def normalize(v1):
    if v1.magnitude != 0:
        return Vector2(v1.x/v1.magnitude, v1.y/v1.magnitude)
    return 0