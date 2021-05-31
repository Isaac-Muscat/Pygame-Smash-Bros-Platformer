import pygame

import settings as s
from gameobjects.obstacles import platform, wall
import src.gameobjects.players.jonah as j
import src.gameobjects.players.isaac as i
from physics.collider2 import CircleCollider2, BoxCollider2
import physics.vector2 as vec



class Scene(object):
    def __init__(self):
        self.next = self

    def process_input(self, events, pressed_keys):
        print("You didn't override this in the child class.")

    def update(self, clock):
        print("You didn't override this in the child class.")

    def display(self, screen):
        print("You didn't override this in the child class.")

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)


class MainMenu(Scene):
    def __init__(self):
        super().__init__()
        self.box1 = BoxCollider2(440, 50, 720, 100).set_active(False)
        self.box2 = BoxCollider2(520, 200, 590, 250)

    def process_input(self, events, pressed_keys):
        x, y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.box2.point_has_collided(x, y):
                    self.switch_to_scene(CharacterSelect())

    def update(self, clock):
        pass

    def display(self, screen):
        screen.fill(s.BLUE)
        self.box1.draw_collider(screen, s.WHITE)
        self.box2.draw_collider(screen, s.RED)
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 30)
        title = font.render("Duper Crash Bros", False, (0, 0, 0))
        center = title.get_rect(center=(self.box1.center.x, self.box1.center.y))
        screen.blit(title, center)
        start = font.render("Start", False, (0, 0, 0))
        center = start.get_rect(center=(self.box2.center.x, self.box2.center.y))
        screen.blit(start, center)


class CharacterSelect(Scene):
    def __init__(self):
        super().__init__()
        self.box1 = BoxCollider2(480, 650, 700, 700)

    def process_input(self, events, pressed_keys):
        x, y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.box1.point_has_collided(x, y):
                    self.switch_to_scene(GameScene())

    def update(self, clock):
        pass

    def display(self, screen):
        screen.fill(s.PURPLE)
        self.box1.draw_collider(screen, s.WHITE)
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 30)
        start = font.render("Start", False, (0, 0, 0))
        center = start.get_rect(center=(self.box1.center.x, self.box1.center.y))
        screen.blit(start, center)


class GameScene(Scene):
    # TODO Must add a list of players and change organization of functions into individual player classes
    def __init__(self):
        super().__init__()
        # self.players = [Player()]
        self.player_1 = j.Jonah()
        self.player_2 = i.Isaac()

        self.floor = platform.Platform(s.s_s[0] * 0.25, s.s_s[1] * 0.75, s.s_s[0] * 0.75, s.s_s[1] * 0.7)
        self.pillar = wall.Wall(s.s_s[0] * 0.26, s.s_s[1] * 0.7, s.s_s[0] * 0.74, s.s_s[1] + 200)

        # BACKGROUND
        self.sun = CircleCollider2(0, 0, 100).set_active(False)

    def process_input(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and self.player_1.jumps_left > 1 and self.player_1.frames_in_tumble == 0:
                    self.player_1.jumps_left -= 1
                    self.player_1.velocity.y = 0
                    self.player_1.add_force(self.player_1.jump_force)

                if event.key == pygame.K_s and self.player_1.frames_in_tumble == 0:
                    self.player_1.velocity.y = 0
                    self.player_1.add_force(vec.multiply(self.player_1.jump_force, -0.5))

                if event.key == pygame.K_UP and self.player_2.jumps_left > 1 and self.player_2.frames_in_tumble == 0:
                    self.player_2.jumps_left -= 1
                    self.player_2.velocity.y = 0
                    self.player_2.add_force(self.player_2.jump_force)

                if event.key == pygame.K_DOWN and self.player_2.frames_in_tumble == 0:
                    self.player_2.velocity.y = 0
                    self.player_2.add_force(vec.multiply(self.player_2.jump_force, -0.5))

        if keys[pygame.K_a] and self.player_1.velocity.x > -self.player_1.max_runspeed and self.player_1.frames_in_tumble == 0:
            run_force = vec.multiply(self.player_1.run_force, -1)
            self.player_1.add_force(run_force)
            self.player_1.direction_facing = -1

        if keys[pygame.K_d] and self.player_1.velocity.x < self.player_1.max_runspeed and self.player_1.frames_in_tumble == 0:
            run_force = self.player_1.run_force
            self.player_1.add_force(run_force)
            self.player_1.direction_facing = 1

        if keys[pygame.K_LEFT] and self.player_2.velocity.x > -self.player_2.max_runspeed and self.player_2.frames_in_tumble == 0:
            run_force = vec.multiply(self.player_2.run_force, -1)
            self.player_2.add_force(run_force)
            self.player_2.direction_facing = -1

        if keys[pygame.K_RIGHT] and self.player_2.velocity.x < self.player_2.max_runspeed and self.player_2.frames_in_tumble == 0:
            run_force = self.player_2.run_force
            self.player_2.add_force(run_force)
            self.player_2.direction_facing = 1

    def update(self, time):
        if self.floor.player_collided_from_top(self.player_1):
            self.player_1.jumps_left = self.player_1.jumps
            self.player_1.velocity.y = 0
            self.player_1.position.y = self.floor.p1.y - self.player_1.collider.height

        elif self.player_1.velocity.y < self.player_1.max_fallspeed:
            self.player_1.add_gravity(self.player_1.gravity_coef)

        self.player_1.add_friction(self.player_1.friction_coef)
        self.player_1.add_drag(self.player_1.drag_coef)
        self.player_1.update(time)

        if self.floor.player_collided_from_top(self.player_2):
            self.player_2.jumps_left = self.player_1.jumps
            self.player_2.velocity.y = 0
            self.player_2.position.y = self.floor.p1.y - self.player_2.collider.height

        elif self.player_2.velocity.y < self.player_2.max_fallspeed:
            self.player_2.add_gravity(self.player_2.gravity_coef)

        self.player_2.add_friction(self.player_2.friction_coef)
        self.player_2.add_drag(self.player_2.drag_coef)
        self.player_2.update(time)

    def display(self, screen):
        screen.fill(s.SKYBLUE)
        self.sun.draw_collider(screen, s.YELLOW)
        self.pillar.draw_collider(screen, s.GREY)
        self.floor.draw_collider(screen, s.GREEN)
        self.player_1.draw(screen)
        self.player_2.draw(screen)
