#IMPORT AND INITIALS
import pygame , math , time
from random import randint , randrange
pygame.init()

def main():
	W , H = 700 , 580
	win= pygame.display.set_mode((W , H))
	pygame.display.set_caption('Space Invader')
	spaceImage = pygame.image.load('GameImage/spaceInvader.png')
	alienImage = pygame.image.load('GameImage/alien.png')
	bulletImage = pygame.image.load('GameImage/bullet.png')
	bgImage = pygame.image.load('GameImage/stars_bg.jpeg')
	player = pygame.image.load('GameImage/spaceship.png')
	playerImage = pygame.transform.scale(player , [70 , 70])
	bgImage = pygame.transform.scale(bgImage , [700 , 580])

	#CLASS AND FUNCIONS
	class Player(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image =playerImage
			self.rect = self.image.get_rect()
			self.speed = 0
			self.rect.centerx = W/2
			self.rect.bottom = H-10
			self.health = 3

		def update(self):
			self.speed = 0
			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]and self.rect.x > 0:
				self.speed =-8
			if keys[pygame.K_RIGHT] and self.rect.right <W:
				self.speed =8
			self.rect.x+=self.speed

		def shoot(self):
			bullet = Bullet(self.rect.centerx , self.rect.bottom)
			all_sprite.add(bullet)
			bullets.add(bullet)

	class Alien(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image = alienImage
			self.rect = self.image.get_rect()
			self.speed = randint(1 , 3)
			self.rect.x = randrange(W - self.rect.width)
			self.rect.y = randrange(-400 , -40)

		def update(self):
			if self.rect.bottom < 580:
				self.rect.y +=self.speed
			else:
				self.rect.x = randrange(W - self.rect.width)
				self.rect.y = randrange(-400 , -40)
				player.health -=1

	class Bullet(pygame.sprite.Sprite):
		def __init__(self , x , y):
			pygame.sprite.Sprite.__init__(self)
			self.image = bulletImage
			self.rect = self.image.get_rect()
			self.speed = -15
			self.rect.centerx = x
			self.rect.bottom = y

		def update(self):
			self.rect.y +=self.speed
			if self.rect.bottom <0:
				self.kill()


	def drawing():
		win.blit(bgImage , (0 , 0))
		win.blit(live , (W-100 , 5))
		win.blit(text , (5 , 5))
		all_sprite.update()
		all_sprite.draw(win)
		aliens.update()
		aliens.draw(win)
		bullets.update()
		bullets.draw(win)
		pygame.display.update()
	#VARIBALE
	all_sprite = pygame.sprite.Group()
	aliens = pygame.sprite.Group()
	bullets = pygame.sprite.Group()
	for i in range(5):
		aliens.add(Alien())
	player = Player()
	all_sprite.add(player)
	score = 0
	make_font = pygame.font.SysFont('comicsansms' , 30)
	clock = pygame.time.Clock()
	run = True
	FPS = 30
	#MAINLOOP
	while run:
		clock.tick(FPS)
		text = make_font.render(f'Score :{score}' , True , (255,255,255))
		live = make_font.render(f'Live :{player.health}' , True , (255,255,255))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					player.shoot()

		hit = pygame.sprite.spritecollide(player , aliens , True)
		if hit:
			player.health -=1
		if player.health == 0:
			run = False
		hits = pygame.sprite.groupcollide(aliens , bullets , True , True)
		if hits:
			score +=5
		for hit in hits:
			a = Alien()
			all_sprite.add(a)
			aliens.add(a)

		drawing()
	pygame.quit()

if __name__ == '__main__':
	main()