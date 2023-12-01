from src.Config import *
from src.Utils.TextUtil import TextUtil
from sys import exit

import pygame

class Menu():

	def __init__(self, view, screen):
		self.text = TextUtil()
		self.selected = 0
		self.screen = screen
		self.view = view
		self.menu = ['Start', 'Quit']
		#print(self)
		pygame.display.set_caption('My Shmup - Menu')


	def build_menu(self):
		# Init
		spacing = 70
		startY = 50
		fontSize = 80
		positionY = startY
		# Begin menu building
		for index, choice in enumerate(self.menu) :
			color = MENU_DEFAULT_TEXT_COLOR
			if index == self.selected:
				color =  MENU_SELECTED_TEXT_COLOR
			self.text.write(self.screen, choice, color , fontSize, 50,  positionY)
			positionY += spacing

	def run(self, pygame):
		run = True
		while run:
			self.screen.fill(MENU_BG_COLOR)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

				if event.type == pygame.KEYDOWN :
					# Menu navigation
					if event.key == pygame.K_DOWN  :
						self.selected+=1
						# Infinite loop over menu elements
						if(self.selected > len(self.menu) -1 ):
							self.selected = 0
					if event.key == pygame.K_UP  :
						self.selected-=1
						if(self.selected == -1 ):
							self.selected = len(self.menu) -1

					# Quit with escape key
					if event.key == pygame.K_ESCAPE:
						run = False
					# Any menu element is selected
					if event.key == pygame.K_RETURN:
						if self.selected == 0 :
							self.view.call(self.view.VIEW_GAME)
						if self.selected == 1 :
							pygame.quit()
							exit()
			self.build_menu()

			pygame.display.update()
