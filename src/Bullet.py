import pygame

class Bullet(pygame.sprite.Sprite):
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
