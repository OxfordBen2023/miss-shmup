import pygame
from sys import exit

from src.Player import Player
from src.Enemy import Enemy
from src.Bullet import Bullet
from src.Impact import Impact
from src.Config import *

class Game:
	def __init__(self, view, screen):
		pygame.init()
		self.screen = screen
		self.view = view
		self.reset_window_name()

	def reset_window_name(self):
		pygame.display.set_caption('My Shmup - Play')

	def get_screen(self):
		return self.screen
		
	def run(self, pygame):

		sky_surface = pygame.image.load('assets/graphics/starSky.png').convert()

		# Groups
		player = pygame.sprite.GroupSingle()
		player.add(Player())
		bullet_group = pygame.sprite.Group()
		enemy_group = pygame.sprite.Group()
		impact_group = pygame.sprite.Group()
		enemy_group.add(Enemy((750,60),1.5))
		enemy_group.add(Enemy((700,160),1))
		enemy_group.add(Enemy((720,260),1.9))
		enemy_group.add(Enemy((600,300),1))
		enemy_group.add(Enemy((710,350),2))

		block_hit_list = []

		run = True
		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				if	event.type == pygame.KEYDOWN :
					if event.key == pygame.K_SPACE :
						bullet_group.add(Bullet(player.sprite.rect.center))
					if event.key == pygame.K_p :
						# To pause
						self.view.call("PAUSE")
						self.reset_window_name()
					if event.key == pygame.K_m :
						# To menu
						self.view.call("MENU")
						self.reset_window_name()

			clock = pygame.time.Clock()

			self.screen.blit(sky_surface,(0,0))

			for bullet in bullet_group:
				block_hit_list = pygame.sprite.spritecollide(bullet, enemy_group, True)
				if block_hit_list:
					bullet.kill()
					impact_group.add(Impact(block_hit_list[0].rect.center))

			player.draw(self.screen)
			enemy_group.draw(self.screen)
			bullet_group.draw(self.screen)
			impact_group.draw(self.screen)


			player.update()
			enemy_group.update()
			bullet_group.update()
			impact_group.update()

			pygame.display.update()
			clock.tick(60)
