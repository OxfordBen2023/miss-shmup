import pygame
import pygame
from sys import exit

# from src.Player import Player
# from src.Enemy import Enemy
# from src.Bullet import Bullet
# from src.Impact import Impact
from src.Views.Game import Game
from src.Views.Menu import Menu
from src.Views.Pause import Pause

from .Config import Config

# This class is responsible of view switching
# It contains screen object
class View():

	VIEW_MENU = "MENU"
	VIEW_GAME = "GAME"
	VIEW_PAUSE = "PAUSE"

	def __init__(self, resolutionX, resolutionY):
		pygame.init()
		self.screen = pygame.display.set_mode((resolutionX,resolutionY))
		pygame.display.set_caption('My Shmup')

	def getActualView(self):
		return self.view

	def call(self, name):
		match name:
			case self.VIEW_GAME :
				self.view = Game(self, self.screen)
			case self.VIEW_PAUSE :
				self.view = Pause(self, self.screen)
			case _:
				self.view = Menu(self, self.screen)

		self.view.run(pygame)
