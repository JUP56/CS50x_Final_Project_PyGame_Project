import pygame, sys
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, PATHS
from pygame.math import Vector2 as vector
from pytmx.util_pygame import load_pygame
from sprite import Sprite
from player import Player
from enemy import Ninja


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = vector()
        self.display_surface = pygame.display.get_surface()
        self.bg = pygame.image.load('../tilesets/ground.png')

    def customize_draw(self, player):

        # change offset vector
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

        # blit to surface
        self.display_surface.blit(self.bg, -self.offset) # make sure to use negative offset for camera
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_rect = sprite.image.get_rect(center=sprite.rect.center)
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("CS50x Final project game")
        self.clock = pygame.time.Clock()


        # groups
        self.all_sprites = AllSprites()
        self.obstacles = pygame.sprite.Group()
        # self.attack_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # sounds
        # ------------ To be added ----------- #

        self.setup()

    def setup(self):
        tmx_map = load_pygame('../data/map.tmx')

        # objects
        for obj in tmx_map.get_layer_by_name('Objects'):
            Sprite((obj.x, obj.y), obj.image, [self.all_sprites, self.obstacles])
        # self.player = Player((192, 288), self.all_sprites, PATHS['player'], collision_sprites=self.obstacles)
        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                self.player = Player(
                    pos=(obj.x, obj.y),
                    groups=self.all_sprites,
                    path=PATHS['player'],
                    collision_sprites=self.obstacles,
                    enemies=self.enemies
                )
            if obj.name == 'enemy_1':
                Ninja(
                    pos=(obj.x, obj.y),
                    groups=[self.all_sprites, self.enemies],
                    path=PATHS['enemies'],
                    collision_sprites=self.obstacles,
                    player=self.player
                )

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.dt = self.clock.tick() / 1000

            # update
            self.all_sprites.update(self.dt)

            # draw
            self.display_surface.fill('black')
            self.all_sprites.customize_draw(self.player)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
