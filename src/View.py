import pygame
from sys import exit


from src.Views.Game import Game
from src.Views.Menu import Menu
from src.Views.Pause import Pause

from .Config import *

# This class is responsible of view switching
# It contains screen object
class View:
	def __init__(self, resolutionX, resolutionY):
		pygame.init()
		self.screen = pygame.display.set_mode((resolutionX,resolutionY))

	def getActualView(self):
		return self.view

	def call(self, name):
		match name:
			case "GAME" :
				self.view = Game(self, self.screen)
			case "PAUSE" :
				self.view = Pause(self, self.screen)
			case "MENU":
				self.view = Menu(self, self.screen)

		self.view.run(pygame)
