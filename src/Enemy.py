import pygame

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