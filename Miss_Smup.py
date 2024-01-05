from src.Config import *
from src.View import View

view = View(RESOLUTION_X, RESOLUTION_Y)


if(NO_MENU_SCREEN):
	view.call('GAME')
else:
	view.call('VIEW_MENU')