from src.Config import Config
from src.View import View

config = Config()
resolutionX = 800
resolutionY = 400

view = View(resolutionX, resolutionY)

if(config.NO_MENU_SCREEN):
	view.call(view.VIEW_GAME)
else:
	view.call(view.VIEW_MENU)
