from src.Config import *
from src.Utils.TextUtil import TextUtil
import pygame

class Pause():

	def __init__(self, view, screen):
		self.text = TextUtil()
		self.selected = 0
		self.screen = screen
		self.view = view
		self.menu = ['Start', 'Quit']
		print(self)
		pygame.display.set_caption('My Shmup - Pause')


	def run(self, pygame):
		run = True
		while run:
			self.screen.fill(MENU_BG_COLOR)
			self.text.write(self.screen, "PAUSED !", MENU_DEFAULT_TEXT_COLOR , 90, 50,  50)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

				if event.type == pygame.KEYDOWN :
					# Exit pause menu
					if event.key == pygame.K_p or event.key == pygame.K_ESCAPE  :
						run = False

			pygame.display.update()
