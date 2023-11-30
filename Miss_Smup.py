import pygame
from sys import exit


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
		player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2]
		self.player_index = 0
		self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(center = (100,200))
		self.gravity = 0

		self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
		self.jump_sound.set_volume(0.02)

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			self.jump_sound.play()
		if keys[pygame.K_LEFT]:
			self.rect.x -= 4
		if keys[pygame.K_RIGHT]:
			self.rect.x += 4
		if keys[pygame.K_UP]:
			self.rect.y -= 4
		if keys[pygame.K_DOWN]:
			self.rect.y += 4

	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300

	def animation_state(self):
		self.player_index += 0.1
		if self.player_index >= len(self.player_walk):self.player_index = 0
		self.image = self.player_walk[int(self.player_index)]

	def update(self):
		self.player_input()
		#self.apply_gravity()
		self.animation_state()

class Bulet(pygame.sprite.Sprite):
	def __init__(self,emit):
		super().__init__()
		self.image = pygame.Surface([7, 7])
		self.image.fill((254,233,161))
		self.rect = self.image.get_rect(center = (emit))

	def shoot_forward(self):
		self.rect.x += 20

	def update(self):
		self.shoot_forward()
		self.destroy()

	def destroy(self):
		if self.rect.x < 0 or self.rect.x >800 or self.rect.y < 0 or self.rect.y > 400 :
			self.kill()

class Enemy(pygame.sprite.Sprite):
	def __init__(self,emit, speed):
		super().__init__()
		self.image = pygame.Surface([30, 30])
		self.image.fill((180,220,180))
		self.rect = self.image.get_rect(center = (emit))
		self.speed = speed

	def moove(self):
		self.rect.x -= self.speed

	def update(self):
		self.destroy()
		self.moove()

	def destroy(self):
		if self.rect.x < 0 or self.rect.x >800 or self.rect.y < 0 or self.rect.y > 400 :
			self.kill()

class Impact(pygame.sprite.Sprite):
	def __init__(self,emit):
		super().__init__()
		self.image = pygame.Surface([40, 40])
		self.image.fill((255,255,255))
		self.rect = self.image.get_rect(center = (emit))
		self.age = 0

	def update(self):
		self.destroy()
		self.age += 0.5

	def destroy(self):
		if self.rect.x < 0 or self.rect.x >800 or self.rect.y < 0 or self.rect.y > 400 :
			self.kill()
		if self.age > 1:
			self.kill()

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('My Shmup')
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf' , 50)
sky_surface = pygame.image.load('graphics/starSky.png').convert()


#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

bulet_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()

impact_group = pygame.sprite.Group()

enemy_group.add(Enemy((750,60),1.5))
enemy_group.add(Enemy((700,160),1))
enemy_group.add(Enemy((720,260),1.9))
enemy_group.add(Enemy((600,300),1))
enemy_group.add(Enemy((710,350),2))

block_hit_list = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if	event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE :
            bulet_group.add(Bulet(player.sprite.rect.center))

    screen.blit(sky_surface,(0,0))

    for bulet in bulet_group:
        block_hit_list = pygame.sprite.spritecollide(bulet, enemy_group, True)
        if block_hit_list:
            bulet.kill()
            impact_group.add(Impact(block_hit_list[0].rect.center))
    player.draw(screen)
    player.update()

    enemy_group.draw(screen)
    enemy_group.update()

    bulet_group.draw(screen)
    bulet_group.update()

    impact_group.draw(screen)
    impact_group.update()

    pygame.display.update()
    clock.tick(60)
