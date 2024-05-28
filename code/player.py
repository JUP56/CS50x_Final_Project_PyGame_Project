import sys

import pygame
from pygame.math import Vector2 as vector
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, path, collision_sprites, enemies):
        super().__init__(pos, groups, path, collision_sprites)
        self.enemies = enemies
        self.attack_radius = 25

    def get_enemy_distance_direction(self):
        player_pos = vector(self.rect.center)
        for sprite in self.enemies.sprites():
            enemy_pos = vector(sprite.rect.center)
        distance = (player_pos - enemy_pos).magnitude()

        if distance != 0:
            direction = (player_pos - enemy_pos).normalize()
        else:
            direction = vector(0, 0)
        return (distance, direction)

    def get_status(self):

        # idle
        if self.direction.x == 0 and self.direction.y == 0:
            if '_idle' not in self.status:
                self.status = self.status.split('_')[0] + '_idle'
        if self.attacking:
            self.status = self.status.split('_')[0] + '_attack'

    def input(self):
        keys = pygame.key.get_pressed()
        if not self.attacking:
            # vertical movement
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            # horizontal movement
            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0

            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.direction = vector()
                self.frame_index = 0

    def animate(self, dt):
        current_animation = self.animations[self.status]
        self.frame_index += 4 * dt

        if self.frame_index >= len(current_animation):
            self.frame_index = 0
            if self.attacking:
                self.attacking = False
        self.image = current_animation[int(self.frame_index)]
        self.mask = pygame.mask.from_surface(self.image)

    def player_attack_logic(self):
        if int(self.frame_index) == 0 and self.attacking:
            enemy_list = []
            for sprite in self.enemies.sprites():
                pygame.sprite.spritecollide(self, self.enemies, True)

    def check_death(self):
        if self.health <= 0:
            pygame.quit()
            sys.exit()

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
        self.get_status()
        self.player_attack_logic()
        self.vulnerability_timer()
        self.check_death()
        self.blink()

