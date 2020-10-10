import pygame , time , datetime
from random import randrange
pygame.init()
pygame.mixer.init()

WIDTH , HEIGHT = 660 , 480
win = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption('SNAKE GAME')
perm = True

def gameLoop(perm):
	#variable
	apple = pygame.image.load('GameImage/Apple.jpg')
	bgImage = pygame.image.load('GameImage/SnakeBgroud.jpg')
	bgsound = pygame.mixer.Sound('GameSounds/sound.wav')
	bgsound.set_volume(0.2)
	apple = pygame.transform.scale(apple , [20 , 20])
	menuImage = pygame.transform.scale(bgImage , [660 , 480])
	apple.set_colorkey((255 ,255 ,255))
	game_over = perm
	run = True
	RED = (255 , 0 ,0)
	WHITE = (255 ,255,255)
	white = (240 , 235 ,240)
	BLUE = (0,0,255)
	BLACK = (0,0,0)
	GREEN = (0,255 ,0)
	YELLOW = (255 ,230 ,20)
	BGC = (0 , 215,0)
	x_pos ,y_pos= 340 , 240
	x_food = randrange(20 , 620 , 20)
	y_food = randrange(20 , 440 , 20)
	x_change =0
	y_change =0
	v= 20
	snake_list = []
	lenght = 1
	score = 0
	font = pygame.font.SysFont('comicsansms', 15)
	big_font = pygame.font.SysFont('comicsansms', 30)
	programmer_font = pygame.font.SysFont('comicsansms' , 20)
	pause_font = pygame.font.SysFont('arial' , 15)
	p_b_rect = pygame.Rect(WIDTH-100,0 ,60 , 18)
	#function
	def draw_snake(win ,snake_list, color ,x , y , v):
		for pos in snake_list:
			pygame.draw.rect(win , BLACK , [pos[0]-2 , pos[1]-2 , v+3 , v+3] , 2)
			pygame.draw.rect(win , color , [pos[0] , pos[1] , v , v])

	def draw_food(x , y):
		win.blit(apple , [x , y])

	def Score(mes , color):
		mesg = font.render(mes , True , color)
		win.blit(mesg , [0 , 0])

	def p_botton(WIDTH):
		pygame.draw.rect(win , (0,0,0) ,p_b_rect , 2)
		text = pause_font.render('Pause !' , True , (0,0,0))
		win.blit(text , [WIDTH-90 , 1])

	def MENU():
		if WIDTH/2-50 <= mouse[0]<=WIDTH/2+50 and 50 <=mouse[1] <=70:
			pygame.draw.rect(win , GREEN , [WIDTH/2-50 , 50 , 100 , 20])
		elif WIDTH/2-50 <= mouse[0]<=WIDTH/2+50 and 130 <=mouse[1] <=150:
			pygame.draw.rect(win , RED , [WIDTH/2-50, 130 , 100 , 20])
		elif WIDTH/2-50 <= mouse[0]<=WIDTH/2+50 and 90 <=mouse[1] <=110:
			pygame.draw.rect(win , BLUE , [WIDTH/2-50, 90 , 100 , 20])
		else:
			pygame.draw.rect(win , WHITE , [WIDTH/2-50 , 50 , 100 , 20])
			pygame.draw.rect(win , WHITE , [WIDTH/2-50 , 90 , 100 , 20])
			pygame.draw.rect(win , WHITE, [WIDTH/2-50, 130 , 100 , 20]) 
		start = font.render('START' , True , BLACK)			
		menu = big_font.render('MAIN MENU' , True , BLACK , BLUE)
		quit = font.render('QUIT' , True , BLACK)
		save = font.render('SAVE!' , True , BLACK)
		programmer = programmer_font.render('THE PROGRAMMER IS RAHSED KHALIL :)' , True , BLACK)
		win.blit(menu , [WIDTH/2-100 , 0])
		win.blit(start , [WIDTH/2-30 , 50])
		win.blit(save , [WIDTH/2-30 , 90])
		win.blit(quit , [WIDTH/2-30 , 130])
		win.blit(programmer , [100 , HEIGHT-100])
		pygame.display.update()

	def LostMessage():
		lost = big_font.render('You Lost ):' ,True, (0,0 ,0))
		win.blit(lost , [WIDTH/2-50 , HEIGHT/2-50])
		pygame.display.update()
	def draw_bound(WHITE):
		pygame.draw.rect(win , WHITE, [0 , 0 , 20 , 479])
		pygame.draw.rect(win , WHITE , [640 , 0 , 20 , 479])
		pygame.draw.rect(win , WHITE, [0 , 0 , 690 , 20])
		pygame.draw.rect(win , WHITE , [0 , 460 , 659 , 20])

	def Save_Score(score):
		t = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S'))
		scores = open('socre.txt' , 'a')
		scores.write('\t'+str(score) + '\t \t||' +t +'\n') 

	#main loopb
	clock = pygame.time.Clock()
	while run:
		clock.tick(14)
		x, y = pygame.mouse.get_pos()
		while game_over:
			bgsound.play()
			pygame.display.update()
			win.blit(menuImage , (0,0))
			mouse =pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if WIDTH/2-50 <= mouse[0]<=WIDTH/2+50 and 50 <=mouse[1] <=70:
						bgsound.stop()
						gameLoop(False)
					if WIDTH/2-50 <= mouse[0]<=WIDTH/2+50 and 90 <=mouse[1] <=110:
						Save_Score(score)
					if WIDTH/2-50 <= mouse[0]<=WIDTH/2+50 and 130 <=mouse[1] <=150:
						exit()
						
				if event.type == pygame.QUIT:
					exit()

			MENU()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type==pygame.MOUSEBUTTONDOWN:
				if p_b_rect.collidepoint((x,y)):
					print(68)
		# moving snake
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			x_change = -20
			y_change = 0
		if keys[pygame.K_RIGHT]:
			x_change = 20
			y_change =0
		if keys[pygame.K_UP]:
			y_change = -20
			x_change =0
		if keys[pygame.K_DOWN]:
			y_change =20
			x_change =0

		x_pos +=x_change
		y_pos += y_change
		#gives postion to snake
		pos =[]
		pos.append(x_pos)
		pos.append(y_pos)
		snake_list.append(pos)
		if len(snake_list) > lenght:
			snake_list.pop(0)
		for i in snake_list[:-1]:
			if i== pos:
				LostMessage()
				time.sleep(2)
				game_over = True

		#eating a food
		if x_pos == x_food and y_pos == y_food:
			x_food =randrange(20 , 640 , 20)
			y_food =randrange(20 , 460 , 20)
			lenght +=1
			score +=5

		if x_pos <= 0 or x_pos>= 640 or  y_pos >= 460 or y_pos <=10:
			LostMessage()
			time.sleep(2)
			game_over = True


		win.fill(BGC)
		draw_bound(white)
		#p_botton(WIDTH)
		draw_snake(win ,snake_list, YELLOW , x_pos , y_pos , v)
		draw_food(x_food , y_food)
		Score('Your Score : ' + str(score) , BLACK)
		pygame.display.update()

	pygame.quit()
if __name__ == '__main__':
	gameLoop(perm)