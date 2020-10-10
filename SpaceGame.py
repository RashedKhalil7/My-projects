#IMPORT AND INITIALS
import pygame ,time,sys
from random import randint , randrange
pygame.init()
pygame.mixer.init()
per=True
m=False

def main(per , m):
	W , H = 700 , 580
	win= pygame.display.set_mode((W , H))
	pygame.display.set_caption('THE SPACE WAR (:')
	#All game images
	spaceImage = pygame.image.load('GameImage/spaceInvader.png')
	alienImage = pygame.image.load('GameImage/alien.png').convert()
	bulletImage = pygame.image.load('GameImage/bullet.png')
	bgImage = pygame.image.load('GameImage/bg5.jpg')
	player = pygame.image.load('GameImage/spaceship.png').convert()
	enemy_bullet = pygame.image.load('GameImage/atom_bullet.png').convert()
	Menu_image = pygame.image.load('GameImage/bkg.png')
	bg_img = pygame.image.load('GameImage/stars.jpeg')
	About_menu = pygame.image.load('GameImage/space_menu.jpg')
	Help_menu = pygame.image.load('GameImage/help_menu.jpg')
	start = pygame.image.load('GameImage/buttons-2/start-2.png')
	helper = pygame.image.load('GameImage/buttons-2/help-2.png')
	about = pygame.image.load('GameImage/buttons-2/about-2.png')
	exit = pygame.image.load('GameImage/buttons-2/exit-2.png')
	rect = start.get_rect()
	BLACK=(0,0,0)
	playerImage = pygame.transform.scale(player , [70 , 70])
	playerImage.set_colorkey(BLACK)
	bgImage = pygame.transform.scale(bgImage , [700 , 580])
	Menu_image = pygame.transform.scale(Menu_image, [700 , 580])
	About_menu = pygame.transform.scale(About_menu , [700 , 580])
	enemy_bullet = pygame.transform.scale(enemy_bullet , [8,10])
	enemy_bullet.set_colorkey(BLACK)


	alienImage.set_colorkey(BLACK)
	#Game sounds and music
	shoot_sound = pygame.mixer.Sound('GameSounds/pew.wav')
	expl_sound = pygame.mixer.Sound('GameSounds/expl3.wav')
	expl2_sound = pygame.mixer.Sound('GameSounds/expl6.wav')
	pygame.mixer.music.load('GameSounds/06_battle_in_space_intro.ogg')
	menu_music = pygame.mixer.Sound('GameSounds/gamesound.ogg')
	click_sound = pygame.mixer.Sound('GameSounds/click.wav')
	pygame.mixer.music.set_volume(0.8)
	menu_music.set_volume(0.1)
	pygame.display.set_icon(spaceImage)
	#CLASS AND FUNCIONS
	class Player(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			self.image =playerImage
			self.rect = self.image.get_rect()
			self.speed = 0
			self.rect.centerx = W/2
			self.rect.bottom = H-10
			self.shoot_delay = 300
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
			if 1 == randrange(400):
				self.atou_shoot()

		def atou_shoot(self):
			bullet = Enemy_bullet(self.rect.centerx , self.rect.bottom)
			all_sprite.add(bullet)
			Atoum_bullet.add(bullet)

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

	class Enemy_bullet(pygame.sprite.Sprite):
		def __init__(self , x ,y):
			pygame.sprite.Sprite.__init__(self)
			self.image = enemy_bullet
			self.rect = self.image.get_rect()
			self.speed = 15
			self.rect.centerx = x
			self.rect.bottom = y

		def update(self):
			self.rect.y +=self.speed
			if self.rect.top>H:
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
		draw_live(player.shield)
		win.blit(live , (W-110 , 5))
		win.blit(text , (5 , 5))
		all_sprite.update()
		all_sprite.draw(win)
		aliens.update()
		aliens.draw(win)
		bullets.update()
		bullets.draw(win)
		Atoum_bullet.update()
		Atoum_bullet.draw(win)
		pygame.display.update()

	def MENU():
		menu_music.play()
		pygame.mixer.music.stop()
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type ==pygame.MOUSEBUTTONDOWN:
				if start_rect.collidepoint(mouse):
					click_sound.play()
					menu_music.stop()
					main(False,True)
				if help_rect.collidepoint(mouse):
					click_sound.play()
					HELP()
				if exit_rect.collidepoint(mouse):
					click_sound.play()
					pygame.quit()
					sys.exit()
				if about_rect.collidepoint(mouse):
					click_sound.play()
					ABOUT()
		#read score and user name from SCORE file
		dic = {}
		f = open('SCORE.txt' , 'r')
		for i , text in enumerate(f.readlines()):
			dic[i]=text
		f.close()
		dic[0] = dic[0][:-2]

		m = make_font.render('name', True , WHITE)
		win.blit(Menu_image , [0,0])
		pygame.draw.rect(win , WHITE , (w-50 , 400 , 200 , 30),2)
		pygame.draw.rect(win , WHITE , (w-50 , 460 , 50 , 30),2)
		NAME = make_font.render('Name :' , True , GREEN)
		RESULT = make_font.render('Score :' , True , GREEN)
		S = make_font.render(dic[1] , True , WHITE)
		N = make_font.render(dic[0] , True , WHITE)
		win.blit(start , [w ,100 ])
		win.blit(helper , [w,180])
		win.blit(about , [w,260])
		win.blit(exit , [w , 340])
		win.blit(N , [w-40 , 400])
		win.blit(S , [w-40 ,460 ])
		win.blit(NAME , [w-120 , 400])
		win.blit(RESULT , [w-120 , 460])
		pygame.display.update()

	def ABOUT():
		t = True
		while t:
			mouse = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if MENU_rect.collidepoint(mouse):
						t = False
						click_sound.play()
				
			win.blit(About_menu,[0,0])
			go = make_font.render('GO TO MENU' , True,(255,0,0))
			text = "This game have been programed with Rashed Khalil" 
			text1 =  "it's about The war between Aliens and Hero space"
			text = make_font.render(text , True , (0,255,0))
			text1 = make_font.render(text1 , True , (0,255,0))
			pygame.draw.rect(win , (255,255,255),[300 , 50 , 180 , 30],2)
			win.blit(text , [100 , 160])
			win.blit(text1 , [100 , 190])
			win.blit(go , [320 , 50])
			pygame.display.update()

	guide_font = pygame.font.SysFont('comicsansms' , 15)
	def HELP():
		t = True
		while t:
			mouse = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if MENU_rect.collidepoint(mouse):
						t = False
						click_sound.play()
		
			win.blit(Help_menu,[0,0])
			go = make_font.render('GO TO MENU' , True,(0,255,0))
			text = "YOU CAN MOVE YOUR SPACE WITH THE LEFT ARROW AND THE RIGHT ARROW"
			text1 =  "AND SHOOT SOME BULLETS WIHT SPACE KEY ON KEYBOARD"
			text = guide_font.render(text , True , (0,255,0))
			text1 = guide_font.render(text1 , True , (0,255,0))
			pygame.draw.rect(win , (255,255,255),[300 , 50 , 180 , 30])
			win.blit(text , [80 , 160])
			win.blit(text1 , [100 , 190])
			win.blit(go , [320 , 50])
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

	input_rect = pygame.Rect(100 , 220 , 140 , 30)
	user_name = ""
	n = ''
	score = 0
	def player_name(user_name):
		r = True
		while r:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					r = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE:
						user_name = user_name[:-1]
					elif event.key == pygame.K_RETURN:
						n = user_name
						user_name = ''
						r = False
						scores = open('SCORE.txt' , 'w')
						scores.write(f'{n}\n {score}')
					else:
						user_name += event.unicode

			win.blit(bg_img , [0,0])
			pygame.draw.rect(win , (0,245,200) , (160 , 220 , 300 , 30) , 2)
			t = make_font.render("Enter Name ",True , RED)
			name = make_font.render(user_name , True , WHITE)
			win.blit(t , [50 , 220])
			win.blit(name , [170 , 220])
			pygame.display.update()


	#VARIBALE
	all_sprite = pygame.sprite.Group()
	aliens = pygame.sprite.Group()
	bullets = pygame.sprite.Group()
	Atoum_bullet = pygame.sprite.Group()
	for i in range(5):
		Create_Alien()
	player = Player()
	all_sprite.add(player)
	make_font = pygame.font.SysFont('comicsansms' , 20)
	live_font = pygame.font.SysFont('comicsansms' , 15)
	explosion_img = {}
	explosion_img[0] = []
	explosion_img[1] = []
	for i in range(8):
		img = pygame.image.load('GameImage/Explosions/expl{}.png'.format(i))
		img_lg = pygame.transform.scale(img , [75,75])
		img_lg.set_colorkey(BLACK)
		explosion_img[1].append(img_lg)
		img_sm = pygame.transform.scale(img , [32,32])
		explosion_img[0].append(img_sm)
	w = W//2-rect.width//2
	start_rect=pygame.Rect(w,100,rect.width , rect.height)
	help_rect = pygame.Rect(w,180 , rect.width,rect.height)
	about_rect = pygame.Rect(w,260,rect.width,rect.height)
	exit_rect = pygame.Rect(w,340,rect.width,rect.height)
	MENU_rect = pygame.Rect(300 , 50 ,180 , 30)
	if m:
		pygame.mixer.music.play(loops=-1)
	GREEN=(0,255,0)
	WHITE=(255,255,255)
	RED = (255,0,0)
	clock = pygame.time.Clock()
	game_over = per
	run = True
	FPS = 30
	#MAINLOOP
	while run:
		clock.tick(FPS)
		text = make_font.render(f'Score :{score}' , True , (255,255,255))
		live = live_font.render(f'{player.shield}%' , True , (255,255,255))
		#GAME MENU
		while game_over:
			MENU()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()


		hit = pygame.sprite.spritecollide(player , aliens,True)
		if hit:
			player.shield -=20
			for h in hit:
				expl = Explosion(h.rect.center,0)
				all_sprite.add(expl)
				expl2_sound.play()
		if player.shield == 0:
			lost = make_font.render('YOUR LOST THE GAME):' , True ,(255,0,0))
			win.blit(lost , [250 ,50])
			pygame.display.update()
			time.sleep(2)
			player_name(user_name)
			game_over=True

		atu_bullet = pygame.sprite.spritecollide(player , Atoum_bullet , True)
		if atu_bullet:
			for b in atu_bullet:
				player.shield -=20
				expl = Explosion(b.rect.center,0)
			all_sprite.add(expl)
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
	main(per,m)