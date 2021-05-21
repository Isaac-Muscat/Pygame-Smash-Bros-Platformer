# Pygame-Smash-Bros-Platformer
___
An attempt at somewhat replicating the game of Super Smash Bros with Pygame.

##Structure of the Project
The '2' in the script names means **2D**. So much of the basic structure uses
a two dimensional coordinate system because SSB is a 2D game. All of the actual creative
programing should be done in extended ***Scene*** classes defined in scenes.py.
___
###Physics Package (Homemade)
####vector2.py
* Math package which contains a 2D vector coordinate (x,y)
* Provides simple vector math operations that may be useful
* Instance methods for modifying current object and static methods that return a vector
* Used in collider2.py and rigidbody.py
#####Example of usage:

        a = Vector2(3,5)
        b = Vector2(4,6)
        c = vector2.add(a, b)
  
        #c.x = 7, c.y = 11
        
        #OR
        a.add(b)
        #a.x = 7, a.y = 11

####collider2.py
This module is used to define and detect collisions in the game using basic geometry.
* Parent class is Collider2
* Defines 'CircleCollider2' and 'BoxCollider2' that are children of Collider2
* Gameobjects in gameobjects.py should have one of these colliders to detect any collisions
* Example: the Player class should have a collider to detect if other players or objects iteract with it
#####Example of usage:

        #circle = CircleCollider2(x1, y1, radius)
        #box = BoxCollider2(x1, y1, x2, y2)

        circle = CircleCollider2(1, 1, radius)
        box1 = BoxCollider2(0, 0, 2, 2)
        box2 = BoxCollider2(10, 10, 20, 20)
        
        #'collider_has_collided()' can be used for both circle and box
        
        return circle.collider_has_collided(box1) #Returns True
        return box1.collider_has_collided(box2) #Returns False
        

####rigidbody.py
This module is used to handle the physics updates in the game using forces.
* Should be extended by a gameobject (Ex: class Player(rigidbody))
* Ensure that *object*.update() is called every iteration of the main loop
* When adding gravity or an impact use *object*.add_force(Vector2 vector)
___
###main.py
Try not to update this file as most of the work should be done in scenes.py.
* Iterates over the three critical methods of the Scene class every loop
* If the current scene changes (Ex: MainMenu to GameScene) it calls the same methods
___
###gameobjects.py
This is where all the game features like obstacles, bullets, players, etc should be created.
Simply create a class in gameobject.py (Ex: class Obstacle()) and use 
it in scenes.py.
___
###settings.py
Simply put, this holds all of the random variables that need to be access throughout the project.
Put any finals/constants in or unchangable variables here.
___
###scenes.py
This is theoretically where all of the programming should be done.
If you want a menu scene, then extend the generic *Scene* class. There are a few methods (and the constructor)
to modify:
1. **__init__**: handles creating obstacle, player, projectile objects and runs once before main loop executes other methods 2-4.
2. **process_input**: handles key inputs specifically. ***DO NOT*** draw in this method.
3. **update**: handles physics updates of rigidbodies, collisions, and updating positions.
4. **display**: handles drawing images to the screen such as sprites.
5. **switch_to_scene**: handles the next scene to switch to (Ex: GameScene()). 
This can be called during any of the 2-4 methods. **Last scene should return ***None***
   to break the while loop in main.py.**
   