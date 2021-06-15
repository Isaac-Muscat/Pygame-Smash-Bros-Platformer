import math

import pygame

import settings as s
from gameobjects.obstacles import platform, wall
import gameobjects.players.jonah as j
import gameobjects.players.isaac as i
import gameobjects.players.lucas as l
import gameobjects.players.arend as ar
from physics.collider2 import CircleCollider2, BoxCollider2
import physics.vector2 as vec
p1 = 1 # Global variables to move between scenes
p2 = 1


class Scene(object): # Base scene class
    '''
    This class is extended to create various scences to be used. It is to be used as an abstract class.
    '''
    def __init__(self):
        self.next = self


    def process_input(self, events, pressed_keys):
        '''
        This is where all of the inputs for the scene is controlled.

        :param events: the events of the program from pygame.events.
        :param pressed_keys: the currently pressed keys.
        :return: NA.
        '''
        print("You didn't override this in the child class.")

    def update(self, time):
        '''
        This is where all the logic should be placed such as physics updates.

        :param clock: the change in time since the last loop.
        :return: NA.
        '''
        print("You didn't override this in the child class.")

    def display(self, screen):
        '''
        This is where all of the drawing to the screen occurs.

        :param screen: the screen to be drawn to.
        :return: NA.
        '''
        print("You didn't override this in the child class.")

    def switch_to_scene(self, next_scene):
        '''
        This links scenes together and it dictates which scene comes next.

        :param next_scene: the next scene.
        :return: NA.
        '''
        self.next = next_scene

    def terminate(self):
        '''
        Stops and exits the program

        :return: NA.
        '''
        self.switch_to_scene(None)


class MainMenu(Scene):
    '''
    This is the main title screen. It is the first scene the user sees
    '''
    def __init__(self):
        super().__init__()

        # Image import and scaling
        self.titlescreen = pygame.image.load("gameobjects/players/sprites/Menus/Main/MainMenu.png")
        self.titlescreen = pygame.transform.scale(self.titlescreen, s.s_s)
        self.startbtn = pygame.image.load("gameobjects/players/sprites/Menus/Main/StartBtn.png")
        self.startbtn = pygame.transform.scale(self.startbtn, (int((s.s_s[0]) / 8), int((s.s_s[1]) / 10)))
        self.box1 = BoxCollider2(s.h_s_s[0] - int((s.s_s[0]) / 16),  # x1
                                 int(s.h_s_s[1] * 1.5),  # y1
                                 s.h_s_s[0] - int((s.s_s[0]) / 16) + int((s.s_s[0]) / 8),  # x2
                                 int(s.h_s_s[1] * 1.5) + int((s.s_s[1]) / 10))  # y2

    #
    def process_input(self, events, pressed_keys):
        x, y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.box1.point_has_collided(x, y):
                    self.switch_to_scene(CharacterSelect())

    def update(self, clock):
        pass

    def display(self, screen):
        self.box1.draw_collider(screen, s.WHITE)
        screen.blit(self.titlescreen, (0, 0))
        screen.blit(self.startbtn, ((s.h_s_s[0] - int((s.s_s[0]) / 16), int(s.h_s_s[1] * 1.5))))


class CharacterSelect(Scene):
    '''
    This is where player 1 and player 2 selects which character they will choose to play as.
    '''
    def __init__(self):
        super().__init__()
        self.startbtn = pygame.image.load("gameobjects/players/sprites/Menus/Main/StartBtn.png")
        self.startbtn = pygame.transform.scale(self.startbtn, (int((s.s_s[0]) / 8), int((s.s_s[1]) / 10)))
        self.selector1 = pygame.image.load("gameobjects/players/sprites/Menus/CharSel/selector.png")
        self.selector1 = pygame.transform.scale(self.selector1, (600, 300))
        self.selector2 = pygame.image.load("gameobjects/players/sprites/Menus/CharSel/selector.png")
        self.selector2 = pygame.transform.scale(self.selector2, (600, 300))
        self.choose = pygame.image.load("gameobjects/players/sprites/Menus/CharSel/choose.png")
        self.choose = pygame.transform.scale(self.choose, (1440, 200))
        self.pl1 = pygame.image.load("gameobjects/players/sprites/Menus/CharSel/Player 1.png")
        self.pl1 = pygame.transform.scale(self.pl1, (250, 45))
        self.pl2 = pygame.image.load("gameobjects/players/sprites/Menus/CharSel/Player 2 .png")
        self.pl2 = pygame.transform.scale(self.pl2, (250, 45))
        self.highlight = pygame.image.load("gameobjects/players/sprites/Menus/CharSel/highlight.png")
        self.highlight = pygame.transform.scale(self.highlight, (550-418, 530-255))
        self.h1coords = (145, 260)
        self.h2coords = (745, 260)
        self.p1controls = pygame.image.load("gameobjects/players/sprites/Menus/CharSel/p1controls.png")
        self.p1controls = pygame.transform.scale(self.p1controls, (300, 300))
        self.p2controls = pygame.image.load("gameobjects/players/sprites/Menus/CharSel/p2controls.png")
        self.p2controls = pygame.transform.scale(self.p2controls, (300, 300))
        self.box1 = BoxCollider2(s.h_s_s[0] - int((s.s_s[0]) / 16),  # x1
                                 int(s.h_s_s[1] * 1.5),  # y1
                                 s.h_s_s[0] - int((s.s_s[0]) / 16) + int((s.s_s[0]) / 8),  # x2
                                 int(s.h_s_s[1] * 1.5) + int((s.s_s[1]) / 10))  # y2


        # Hitboxes for each character selector
        self.iBox1 = BoxCollider2(145, 270, 275, 530) # Player 1
        self.aBox1 = BoxCollider2(290, 270, 410, 530)
        self.jBox1 = BoxCollider2(430, 270, 560, 530)
        self.lBox1 = BoxCollider2(570, 270, 700, 530)

        self.iBox2 = BoxCollider2(750, 270, 875, 530) # Player 2
        self.aBox2 = BoxCollider2(890, 270, 1010, 530)
        self.jBox2 = BoxCollider2(1030, 270, 1150, 530)
        self.lBox2 = BoxCollider2(1175, 270, 1300, 530)

    def process_input(self, events, pressed_keys):
        global p1
        global p2
        x, y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.box1.point_has_collided(x, y):
                    self.switch_to_scene(GameScene())
                elif self.iBox1.point_has_collided(x, y):
                    p1 = 1
                    self.h1coords = (145, 260)
                elif self.aBox1.point_has_collided(x, y):
                    p1 = 2
                    self.h1coords = (285, 260)
                elif self.jBox1.point_has_collided(x, y):
                    p1 = 3
                    self.h1coords = (425, 260)
                elif self.lBox1.point_has_collided(x, y):
                    p1 = 4
                    self.h1coords = (570, 260)

                elif self.iBox2.point_has_collided(x, y):
                    p2 = 1
                    self.h2coords = (745, 260)
                elif self.aBox2.point_has_collided(x, y):
                    p2 = 2
                    self.h2coords = (885, 260)
                elif self.jBox2.point_has_collided(x, y):
                    p2 = 3
                    self.h2coords = (1024, 260)
                elif self.lBox2.point_has_collided(x, y):
                    p2 = 4
                    self.h2coords = (1170, 260)

    def update(self, clock):
        pass

    def display(self, screen):

        self.box1.draw_collider(screen, s.WHITE)
        screen.fill(s.PURPLE)
        screen.blit(self.selector1, ((s.h_s_s[0] - 600), (s.h_s_s[1]) - 200))
        screen.blit(self.selector2, ((s.h_s_s[0]), (s.h_s_s[1]) - 200))
        screen.blit(self.startbtn, ((s.h_s_s[0] - int((s.s_s[0]) / 16), int(s.h_s_s[1] * 1.5))))
        screen.blit(self.choose, (0, 0))
        screen.blit(self.pl1, ((s.h_s_s[0] - 300), (s.h_s_s[1] + 100)))
        screen.blit(self.pl2, ((s.h_s_s[0] + 50), (s.h_s_s[1] + 100)))
        screen.blit(self.highlight, self.h1coords)
        screen.blit(self.highlight, self.h2coords)
        screen.blit(self.p1controls, (250, 600))
        screen.blit(self.p2controls, (900, 600))

class GameScene(Scene):
    '''
    This is the main scene where the two players can fight against each other.
    '''
    def __init__(self):
        super().__init__()
        # Dealing with the Map size and font.
        self.percent_font = pygame.font.SysFont("Arial", 100)
        self.map_s = (int(s.s_s[0] * s.map_multiplier), int(s.s_s[1] * s.map_multiplier))
        self.offset = ((self.map_s[0] - s.s_s[0]) / 2, (self.map_s[1] - s.s_s[1]) / 2)

        # buffer image blitted to screen for translations of the scene.
        self.buffer = pygame.surface.Surface(self.map_s)

        # Player 1 or Player 2 selection
        global p1
        global p2

        # Detect and spawn Player 1's character choice
        if p1 == 1:
            self.pl1 = i.Isaac(self.map_s[0] * 0.4, self.map_s[1] * 0.1, s.p1_bindings)
        elif p1 == 2:
            self.pl1 = ar.Arend(self.map_s[0] * 0.4, self.map_s[1] * 0.1, s.p1_bindings)
        elif p1 == 3:
            self.pl1 = j.Jonah(self.map_s[0] * 0.4, self.map_s[1] * 0.1, s.p1_bindings)
        elif p1 == 4:
            self.pl1 = l.Lucas(self.map_s[0] * 0.4, self.map_s[1] * 0.1, s.p1_bindings)

        # Detect and spawn Player 2's character choice
        if p2 == 1:
            self.pl2 = i.Isaac(self.map_s[0] * 0.6, self.map_s[1] * 0.1, s.p2_bindings, direction_facing=-1)
        elif p2 == 2:
            self.pl2 = ar.Arend(self.map_s[0] * 0.6, self.map_s[1] * 0.1, s.p2_bindings, direction_facing=-1)
        elif p2 == 3:
            self.pl2 = j.Jonah(self.map_s[0] * 0.6, self.map_s[1] * 0.1, s.p2_bindings, direction_facing=-1)
        elif p2 == 4:
            self.pl2 = l.Lucas(self.map_s[0] * 0.6, self.map_s[1] * 0.1, s.p2_bindings, direction_facing=-1)
        self.players = [self.pl1, self.pl2]

        # Spawn map
        self.obstacles = [
            platform.Platform(self.map_s[0] * 0.3, self.map_s[1] * 0.6, self.map_s[0] * 0.7, self.map_s[1] * 0.55,
                              s.GREEN),
            wall.Wall(self.map_s[0] * 0.31, self.map_s[1] * 0.6, self.map_s[0] * 0.69, self.map_s[1], s.GREY)]

        # BACKGROUND
        self.sun = CircleCollider2(self.map_s[0] / 2, self.map_s[1] * 0.2 / 2, 100).set_active(False)

    def process_input(self, events, keys):
        '''
        All inputs passed to the player class (Jonah, Isaac, Arend, Lucas).
        '''
        event_keys = []
        for event in events:
            if event.type == pygame.KEYDOWN:
                event_keys.append(event.key)
        for player in self.players:
            player.process_inputs(event_keys, keys)

    def update(self, time):
        # Check for dead players, move to winner's post-game screen.
        if self.players[0].lives == 0:
            self.switch_to_scene(PostGameP2())
        elif self.players[1].lives == 0:
            self.switch_to_scene(PostGameP1())
        for player in self.players:

            # Handle player attacks @arrays/lists/dictionaries
            for player_2 in self.players:
                # Current attack being evaluated.
                attack = player.attack_collider
                # Checks attack is in reference to opponent player and if there actually is an attack.
                if player is not player_2 and attack is not None and attack.active is True and \
                        attack.collider_has_collided(player_2.collider) and \
                        attack.post_lag < attack.total_lag < \
                        attack.peri_lag + attack.post_lag:

                    # Stuff to change and add if an attack has successfully collided. (Ex: adding a force).
                    player_2.velocity.multiply(0)
                    force = vec.multiply(attack.knockback_direction,
                                         attack.knockback_multiplier * (1 + player_2.damage_percentage))
                    force.x *= player.direction_facing
                    player_2.add_force(force)
                    player_2.damage_percentage += player.attack_collider.percent_damage
                    player_2.frames_in_tumble = player.attack_collider.stun_duration+s.FPS*player_2.damage_percentage/2
                    attack.set_active(False)

            # Handle obstacle collision @arrays/lists/dictionaries
            # Could be put into obstacles class
            for obstacle in self.obstacles:
                if obstacle.player_collided_from_top(player):
                    player.jumps_left = player.jumps
                    player.velocity.y = 0
                    player.position.y = obstacle.p1.y - player.collider.height
                    player.grounded_on = obstacle
                elif player.grounded_on == obstacle and obstacle.player_has_fallen_off(player):
                    player.grounded_on = None
                elif obstacle.player_collided_from_bottom(player):
                    player.velocity.y = 0
                    player.position.y = obstacle.p2.y
                elif obstacle.player_collided_from_left(player):
                    player.velocity.x = 0
                    player.position.x = obstacle.p1.x - player.collider.width
                elif obstacle.player_collided_from_right(player):
                    player.velocity.x = 0
                    player.position.x = obstacle.p2.x + 1

            # Add force or not based on if the character is on a platform
            if player.velocity.y < 0 and player.grounded_on is not None:
                player.grounded_on = None
            if player.velocity.y < player.max_fallspeed and player.grounded_on is None:
                player.add_gravity(player.gravity_coef)

            # Added the physics information to the player
            player.add_friction(player.friction_coef)
            player.add_drag(player.drag_coef)
            player.update(time)

        # Uncomment for players to face each other disregarding input
        '''
        if self.players[0].position.x < self.players[1].position.x:
            self.players[0].direction_facing = 1
            self.players[1].direction_facing = -1
        elif self.players[0].position.x > self.players[1].position.x:
            self.players[0].direction_facing = -1
            self.players[1].direction_facing = 1
        #'''

    def display(self, screen):
        # Display background
        self.buffer.fill(s.SKYBLUE)
        self.sun.draw_collider(self.buffer, s.YELLOW)

        # Uncomment for Blue and red id bars
        '''pygame.draw.rect(self.buffer, s.RED,
            pygame.Rect(self.players[0].collider.p1.x, self.players[0].collider.p1.y-20,
                        75, 10))
        pygame.draw.rect(self.buffer, s.BLUE,
                         pygame.Rect(self.players[1].collider.p1.x, self.players[1].collider.p1.y-20,
                        75, 10))#'''

        # Display physics objects @arrays/lists/dictionaries
        for obstacle in self.obstacles:
            obstacle.draw_collider(self.buffer)
        for player in self.players:
            player.draw(self.buffer)
            if player.attack_collider is not None and s.DEBUG:
                player.attack_collider.draw_collider(self.buffer, s.BLACK)

        # Handle translating the camera view by averaging the player positions
        dist_x = (self.players[0].collider.center.x + self.players[1].collider.center.x) / 2
        dist_y = (self.players[0].collider.center.y + self.players[1].collider.center.y) / 2

        # Ensures the camera postition stays within a certain boundary
        translation = vec.Vector2(
            vec.clamp((self.map_s[0] / 2) - dist_x, (s.s_s[0] - self.map_s[0]) / 2, (self.map_s[0] - s.s_s[0]) / 2),
            vec.clamp((self.map_s[1] / 2) - dist_y, (s.s_s[1] - self.map_s[1]) / 2, (self.map_s[1] - s.s_s[1]) / 2))

        # Diplays the buffer to the screen to be display based on the translation calulated above
        screen.blit(pygame.transform.scale(self.buffer, self.map_s),
                    (translation.x - self.offset[0], translation.y - self.offset[1]))

        # Display health and lives
        for i in range(len(self.players)):
            stats = self.percent_font.render(str(round(self.players[i].damage_percentage * 100)) + '%', False,
                                             (255, 0, 100))
            center = stats.get_rect(center=(self.offset[0] + self.map_s[0] * 0.3 * i, self.map_s[1] * 0.5))

            lives = self.percent_font.render("Lives: " + str(round(self.players[i].lives)), False,
                                             (255, 0, 100))
            screen.blit(stats, center)
            screen.blit(lives, (center[0], center[1] + 100))


class PostGameP1(Scene):
    '''
    This is the ending scene if player one wins
    '''
    def __init__(self):
        super().__init__()

        self.titlescreen = pygame.image.load("gameobjects/players/sprites/Menus/Postgame/Postgame.png")
        self.titlescreen = pygame.transform.scale(self.titlescreen, s.s_s)
        self.player1 = pygame.image.load("gameobjects/players/sprites/Menus/Postgame/player1.png")


        self.box1 = BoxCollider2(76, 665, 800, 740)
        self.box2 = BoxCollider2(916, 665, 1215, 730)

    def process_input(self, events, pressed_keys):
        x, y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.box1.point_has_collided(x, y):
                    self.switch_to_scene(CharacterSelect())
                elif self.box2.point_has_collided(x, y):
                    self.terminate()

    def update(self, clock):
        pass

    def display(self, screen):
        self.box1.draw_collider(screen, s.WHITE)
        screen.blit(self.titlescreen, (0, 0))

        screen.blit(self.player1, (700, 10))


class PostGameP2(Scene):
    '''
    This is the ending scene where player 2 wins
    '''
    def __init__(self):
        super().__init__()

        self.titlescreen = pygame.image.load("gameobjects/players/sprites/Menus/Postgame/Postgame.png")
        self.titlescreen = pygame.transform.scale(self.titlescreen, s.s_s)

        self.player2 = pygame.image.load("gameobjects/players/sprites/Menus/Postgame/player2.png")

        self.box1 = BoxCollider2(76, 665, 800, 740)
        self.box2 = BoxCollider2(916, 665, 1215, 730)

    def process_input(self, events, pressed_keys):
        x, y = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:

                if self.box1.point_has_collided(x, y):
                    self.switch_to_scene(CharacterSelect())
                elif self.box2.point_has_collided(x, y):
                    self.terminate()

    def update(self, clock):
        pass

    def display(self, screen):
        self.box1.draw_collider(screen, s.WHITE)
        screen.blit(self.titlescreen, (0, 0))

        screen.blit(self.player2, (700, 10))