from src.Config import *
from src.View import View

resolutionX = 800
resolutionY = 400

view = View(resolutionX, resolutionY)

if(NO_MENU_SCREEN):
	view.call(view.VIEW_GAME)
else:
	view.call(view.VIEW_MENU)
