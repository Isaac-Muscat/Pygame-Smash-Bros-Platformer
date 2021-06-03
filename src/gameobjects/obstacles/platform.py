from obstacles import Obstacle


class Platform(Obstacle):
    def __init__(self, x1, y1, x2, y2, color):
        super().__init__(int(x1), int(y1), int(x2), int(y2), color)

    def handle_player_collision(self, player, time):
        if self.player_collided_from_top(player):
            player.jumps_left = player.jumps
            player.velocity.y = 0
            player.position.y = self.p1.y - player.collider.height
            player.grounded = True

        elif player.velocity.y < player.max_fallspeed:
            player.add_gravity(player.gravity_coef)

        player.add_friction(player.friction_coef)
        player.add_drag(player.drag_coef)
        player.update(time)