import physics.collider2 as col
import physics.vector2 as vec
import settings as s

class Attack(col.BoxCollider2):
    '''
    This class holds generic characteristics of any attack.
    '''
    def __init__(self, x1, y1, x2, y2, **settings):
        super().__init__(x1, y1, x2, y2)

        # Lag measured in frames
        self.pre_lag = settings.get('pre_lag',s.FPS*0.01)
        self.peri_lag = settings.get('peri_lag',s.FPS*0.5)
        self.post_lag = settings.get('post_lag',s.FPS*0.1)
        self.total_lag = self.pre_lag+self.peri_lag+self.post_lag

        self.percent_damage = settings.get('percent_damage',0.05)
        self.knockback_multiplier = settings.get('knockback_force',5)
        self.knockback_direction = settings.get('knockback_direction', vec.normalize(vec.Vector2(1, -2)))
        self.stun_duration = settings.get('stun_duration', s.FPS*0.1)


class NormalAttack(Attack):
    '''
    This class holds basic characterstics of a regular attack.
    '''
    def __init__(self, p_center_x, p_center_y, **settings): # p stands for 'player' - Ex: player_x
        # Local is position relative to player or the offset
        settings['peri_lag'] = s.FPS/6
        self.local_p1 = settings.get('local_p1', vec.Vector2(0, 0))
        self.local_p2 = settings.get('local_p2', vec.Vector2(0, 0))
        super().__init__(p_center_x+self.local_p1.x, p_center_y+self.local_p1.y,
                         p_center_x+self.local_p2.x, p_center_y+self.local_p2.y, **settings)

    def set_position_from_player(self, player):
        if player.direction_facing == -1:
            x_offset = -self.width
        else:
            x_offset = 0

        self.set_position(player.collider.center.x+x_offset, player.collider.center.y-self.height+max(self.local_p1.y, self.local_p2.y))

class OrbAttack(Attack):
    '''
    Projectile attack specifically used for Arend's character.
    '''
    def __init__(self, p_center_x, p_center_y, **settings):
        settings['pre_lag'] = 0
        settings['post_lag'] = 0
        settings['peri_lag'] = s.FPS*0.3
        self.local_p1 = settings.get('local_p1', vec.Vector2(0, 0))
        self.local_p2 = settings.get('local_p2', vec.Vector2(0, 0))
        self.velocity = settings.get('velocity', 1)
        super().__init__(p_center_x + self.local_p1.x, p_center_y + self.local_p1.y,
                         p_center_x + self.local_p2.x, p_center_y + self.local_p2.y, **settings)

    def set_position_from_player(self, player):
        self.set_position(self.p1.x+self.velocity, self.p1.y)

class VineAttack(Attack):
    '''
    Long-ranged melee attack specifically used for Jonah's ability.
    '''
    def __init__(self, p_center_x, p_center_y, **settings): # p stands for 'player' - Ex: player_x
        # Local is position relative to player or the offset
        settings['peri_lag'] = s.FPS*0.6
        settings['knockback_direction'] = vec.normalize(vec.Vector2(1, -1))
        settings['knockback_force'] = 10
        settings['stun_duration'] = s.FPS * 0.5
        self.local_p1 = settings.get('local_p1', vec.Vector2(0, 0))
        self.local_p2 = settings.get('local_p2', vec.Vector2(0, 0))
        super().__init__(p_center_x+self.local_p1.x, p_center_y+self.local_p1.y,
                         p_center_x+self.local_p2.x, p_center_y+self.local_p2.y, **settings)

    def set_position_from_player(self, player):
        if player.direction_facing == -1:
            x_offset = -self.width
        else:
            x_offset = 0

        self.set_position(player.collider.center.x+x_offset, player.collider.center.y-self.height+max(self.local_p1.y, self.local_p2.y))