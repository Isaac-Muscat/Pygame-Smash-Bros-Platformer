from vector2 import Vector2
import vector2 as vec
import pygame

class Collider2(object):
    def collider_has_collided(self, collider):
        if type(collider) is BoxCollider2:
            return self.box_collider_has_collided(collider)
        if type(collider) is CircleCollider2:
            return self.circle_collider_has_collided(collider)

    def box_collider_has_collided(self, collider):
        return False

    def circle_collider_has_collided(self, collider):
        return False

class BoxCollider2(Collider2):
    def __init__(self, x1, y1, x2, y2):

        #Used to toggle the collider
        self.active = True

        #Ensures point1 vector will always be smaller than point2
        self.p1 = Vector2(x2, y2)
        self.p2 = Vector2(x1, y1)
        if x1 < x2:
            self.p1.x = x1
            self.p2.x = x2
        if y1 < y2:
            self.p1.y = y1
            self.p2.y = y2

        self.set_pos_values()

    #set width, height, and ceneter of box
    def set_pos_values(self):
        self.width = self.p2.x - self.p1.x
        self.height = self.p2.y - self.p1.y
        self.center = Vector2(self.p1.x + self.width / 2, self.p1.y + self.height / 2)

    #Sets the position of the collider using upper left (Defualt pygame coords)
    def set_position(self, x, y):
        self.p1.x = x
        self.p1.y = y
        self.p2.x = x+self.width
        self.p2.y = y+self.height
        self.set_pos_values()

    def vector_point_has_collided(self, v1):
        if self.p1.x < v1.x < self.p2.x and self.p1.y < v1.y < self.p2.y and self.active:
            return True
        return False

    def point_has_collided(self, x, y):
        if self.p1.x < x < self.p2.x and self.p1.y < y < self.p2.y and self.active:
            return True
        return False

    def box_collider_has_collided(self, collider):
        if self.vector_has_collided(collider.p1) or self.vector_has_collided(collider.p2)\
                or self.point_has_collided(collider.p1.x, collider.p2.y) or self.point_has_collided(collider.p2.x, collider.p1.y)\
                and self.active and collider.active:
            return True
        return False

    def circle_collider_has_collided(self, collider):
        return collider.box_collider_has_collided(self)

    def draw_collider(self, screen, color):
        pygame.draw.rect(screen, color,
            pygame.Rect(self.p1.x, self.p1.y, self.p2.x - self.p1.x, self.p2.y-self.p1.y))

class CircleCollider2(Collider2):
    def __init__(self, x, y, r):

        #Used to toggle the collider
        self.active = True

        self.p1 = Vector2(x, y)
        self.radius = r

    #Sets the position of the collider using upper left (Defualt pygame coords)
    def set_Position(self, x, y):
        self.p1.x = x
        self.p1.y = y

    def vector_point_has_collided(self, v1):
        if vec.dist_no_sqrt(self.p1, v1) > self.radius**2:
            return True
        return False

    def point_has_collided(self, x, y):
        if vec.dist_no_sqrt(self.p1, Vector2(x, y)) > self.radius ** 2:
            return True
        return False

    def circle_collider_has_collided(self, collider):
        distance_squared = vec.dist_no_sqrt(self.p1, collider.p1)
        return distance_squared < self.radius**2 and distance_squared < collider.radius

    def box_collider_has_collided(self, collider):
        dx = abs(self.p1.x - collider.center.x);
        dy = abs(self.p1.y - collider.center.y);

        if dx > collider.width / 2 + self.radius:
            return False
        if dy > collider.height / 2 + self.radius:
            return False

        if dx <= collider.width / 2:
            return True
        if dy <= collider.height / 2:
            return True

        corner_distance = vec.dist_no_sqrt(Vector2(dx, dy), Vector2(collider.width/2, collider.height/2))
        corner_distance = (dx - collider.width / 2)**2 + (dy - collider.height / 2)**2
        return corner_distance <= self.radius**2

    def draw_collider(self, screen, color):
        pygame.draw.circle(screen, color, (self.p1.x, self.p1.y), self.radius)

