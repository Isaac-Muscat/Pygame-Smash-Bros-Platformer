import math

class Vector2(object):
    def __init__(self, x=0, y=0) -> object:
        self.x = x
        self.y = y

    def mag(self):
        return math.sqrt(self.x**2+self.y**2)

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
        self.x /=s1
        self.y /=s1

    def normalize(self):
        mag = self.mag()
        if mag > 0:
            self.divide(mag)

    def set(self, v):
        self.x = v.x
        self.y = v.y

    def clone(self):
        return Vector2(self.x, self.y)

def clamp_vector(vector, max_x, min_x, max_y, min_y):
    vector.x = clamp(vector.x, min_x, max_x)
    vector.y = clamp(vector.y, min_y, max_y)

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

#OPTIMIZATION - sqrt is expensive
def dist_no_sqrt(v1, v2):
    return (v1.x-v2.x)**2+(v1.y-v2.y)**2

def dist(v1, v2):
    return math.sqrt((v1.x-v2.x)**2+(v1.y-v2.y)**2)

def add(v1, v2):
    return Vector2(v1.x+v2.x, v1.y+v2.y)

def subtract(v1, v2):
    return Vector2(v1.x - v2.x, v1.y - v2.y)

def divide(v1, s1):
    return Vector2(v1.x/s1, v1.y/s1)

def multiply(v1, s1):
    return Vector2(v1.x*s1, v1.y*s1)

def normalize(v1):
    if v1.mag() > 0:
        return divide(v1, v1.mag())
    return v1

