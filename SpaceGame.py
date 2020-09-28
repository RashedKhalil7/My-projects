#IMPORT AND INITIALS
import pygame , math , time
from random import randint , randrange
pygame.init()
pygame.mixer.init()

def main():
	W , H = 700 , 580
	win= pygame.display.set_mode((W , H))
	pygame.display.set_caption('Space Invader')
	#All game images
	spaceImage = pygame.image.load('GameImage/spaceInvader.png')
	alienImage = pygame.image.load('GameImage/alien.png')
	bulletImage = pygame.image.load('GameImage/bullet.png')
	bgImage = pygame.image.load('GameImage/stars_bg.jpeg')
	player = pygame.image.load('GameImage/spaceship.png')
	playerImage = pygame.transform.scale(player , [70 , 70])
	bgImage = pygame.transform.scale(bgImage , [700 , 580])
	#Game sounds and music
	shoot_sound = pygame.mixer.Sound('GameSounds/pew.wav')
	expl_sound = pygame.mixer.Sound('GameSounds/expl3.wav')
	expl2_sound = pygame.mixer.Sound('GameSounds/expl6.wav')
	pygame.mixer.music.load('GameSounds/gamesound.ogg')
	pygame.mixer.music.set_volume(0.4)

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
			self.shoot_delay = 250
			self.last_shoot = pygame.time.get_ticks()
			self.shield = 100


		def update(self):
			self.speed = 0
			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]and self.rect.x > 0:
				self.speed =-8
			if keys[pygame.K_RIGHT] and self.rect.right <W:
				self.speed =8
			if keys[pygame.K_SPACE]:
				self.shoot()
			self.rect.x+=self.speed

		def shoot(self):
			now = pygame.time.get_ticks()
			if now - self.last_shoot > self.shoot_delay:
				self.last_shoot = now
				bullet = Bullet(self.rect.centerx , self.rect.bottom)
				all_sprite.add(bullet)
				bullets.add(bullet)
				shoot_sound.play()


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
				player.shield -=20

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

	class Explosion(pygame.sprite.Sprite):
		def __init__(self , center , size):
			pygame.sprite.Sprite.__init__(self)
			self.size = size
			self.image = explosion_img[self.size][0]
			self.rect = self.image.get_rect()
			self.rect.center = center
			self.last_update = pygame.time.get_ticks()
			self.frame = 0
			self.frame_rate = 50

		def update(self):
			now = pygame.time.get_ticks()
			if now -self.last_update >self.frame_rate:
				self.last_update = now
				self.frame +=1
				if self.frame == len(explosion_img[self.size]):
					self.kill()
				else:
					center = self.rect.center
					self.image = explosion_img[self.size][self.frame]
					self.rect = self.image.get_rect()
					self.rect.center = center


	def drawing():
		win.blit(bgImage , (0 , 0))
		win.blit(live , (W-40 , 5))
		draw_live(player.shield)
		win.blit(text , (5 , 5))
		all_sprite.update()
		all_sprite.draw(win)
		aliens.update()
		aliens.draw(win)
		bullets.update()
		bullets.draw(win)
		pygame.display.update()

	def draw_live(pec):
		if pec >50:
			pygame.draw.rect(win , GREEN , [W-140,5,pec,20])
			pygame.draw.rect(win , WHITE , [W-140,5,100 ,20],2)
		else:
			pygame.draw.rect(win , RED , [W-140,5,pec,20])
			pygame.draw.rect(win , WHITE , [W-140,5,100 ,20],2)

	def Create_Alien():
		alien= Alien()
		all_sprite.add(alien)
		aliens.add(alien)

	#VARIBALE
	all_sprite = pygame.sprite.Group()
	aliens = pygame.sprite.Group()
	bullets = pygame.sprite.Group()
	for i in range(5):
		aliens.add(Alien())
	player = Player()
	all_sprite.add(player)
	score = 0
	make_font = pygame.font.SysFont('comicsansms' , 20)
	live_font = pygame.font.SysFont('comicsansms' , 15)
	explosion_img = {}
	explosion_img[0] = []
	explosion_img[1] = []
	for i in range(9):
		img = pygame.image.load('GameImage/Explosions_kenney/regularExplosion0{}.png'.format(i))
		img_lg = pygame.transform.scale(img , [75,75])
		img_lg.set_colorkey((0,0,0))
		explosion_img[1].append(img_lg)
		img_sm = pygame.transform.scale(img , [32,32])
		explosion_img[0].append(img_sm)
	GREEN=(0,255,0)
	WHITE=(255,255,255)
	RED = (255,0,0)
	pygame.mixer.music.play(loops=-1)
	clock = pygame.time.Clock()
	run = True
	FPS = 30
	#MAINLOOP
	while run:
		clock.tick(FPS)
		text = make_font.render(f'Score :{score}' , True , (255,255,255))
		live = live_font.render(f'{player.shield}%' , True , (255,255,255))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					player.shoot()

		hit = pygame.sprite.spritecollide(player , aliens , True)
		if hit:
			player.shield -=20
			for h in hit:
				expl = Explosion(h.rect.center,0)
				all_sprite.add(expl)
				expl2_sound.play()
		if player.shield == 0:
			run = False
		hits = pygame.sprite.groupcollide(aliens , bullets , True , True)
		if hits:
			score +=5
		for hit in hits:
			expl = Explosion(hit.rect.center , 1)
			all_sprite.add(expl)
			expl_sound.play()
			Create_Alien()

		drawing()
	pygame.quit()

if __name__ == '__main__':
	main()