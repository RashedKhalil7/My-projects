import pygame
pygame.init()

win = pygame.display.set_mode((500 , 500))
font = pygame.font.Font(None , 25)
user_text = ''
save = ''
input_rect = pygame.Rect(200 , 220 , 140 , 30)

run = True
while run:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			run = False
		if ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_BACKSPACE:
				user_text = user_text[:-1]
			elif ev.key == pygame.K_ENTER:
				save = user_text
				user_text = ''
				print(save)
			else:
				user_text += ev.unicode

	win.fill((255 ,255,255))
	pygame.draw.rect(win , (255 , 0 , 100) , input_rect , 2)
	text = font.render(user_text , True , (0,0,0))
	win.blit(text , [input_rect.x+5 , input_rect.y+5])
	input_rect.w = max(100 , text.get_width()+10)
	pygame.display.update()
pygame.quit()