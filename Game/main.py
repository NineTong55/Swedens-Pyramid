import pygame
import random
import time

if __name__ == "__main__":
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption("Swedens Pyramid")
	clock = pygame.time.Clock()
	
	font = pygame.font.Font(None, 36)
	
	background = pygame.image.load("background.png").convert()
	background = pygame.transform.scale(background, (800, 600))
	
	playerX = 400
	playerY = 600 - 50
	player = pygame.image.load("player.png").convert_alpha()
	player = pygame.transform.scale(player, (50, 50))

	iceX = random.randint(300, 400)
	iceY = random.randint(0, 0)
	iceX2 = random.randint(200, 200)
	iceY2 = random.randint(250, 250)
	iceX3 = random.randint(550, 550)
	iceY3 = random.randint(250, 250)
	iceX4 = random.randint(0, 800)
	iceY4 = random.randint(0, 600)
	iceX5 = random.randint(0, 800)
	iceY5 = random.randint(0, 600)
	
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				exit()

		playerRect = pygame.rect.Rect((playerX, playerY), player.get_size())
		
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			playerX -= 5
		if key[pygame.K_RIGHT]:
			playerX += 5
		if key[pygame.K_UP]:
			playerY -= 5
		if key[pygame.K_DOWN]:
			playerY += 5

		iceY += 10
		iceY2 += 10
		iceY3 += 10
		iceY4 += 10
		iceY5 += 10
		
		if iceY > 600 - 50:
			iceX = random.randint(300, 400)
			iceY = random.randint(0, 0)
		if iceY2 > 600 - 50:
			iceX2 = random.randint(200, 200)
			iceY2 = random.randint(250, 250)
		if iceY3 > 600 - 50:
			iceX3 = random.randint(550, 550)
			iceY3 = random.randint(250, 250)
		if iceY4 > 600 - 50:
			iceX4 = random.randint(0, 800)
			iceY4 = random.randint(0, 300)
		if iceY5 > 600 - 50:
			iceX5 = random.randint(0, 800)
			iceY5 = random.randint(0, 300)
		
		if playerY < 0 and playerX < 400 and playerX > 350:
			print "You win"
			exit()
		
		if playerX < 0:
			playerX += 5
		if playerX > 800 - 50:
			playerX -= 5
		
		clock.tick(30)
		print clock.get_fps()
		screen.blit(background, (0, 0))
		screen.blit(player, (playerX, playerY))
		ice = pygame.draw.rect(screen, (165, 242, 243), (iceX, iceY, 50, 50))
		iceRect = pygame.rect.Rect(iceX, iceY, 50, 50)
		ice2 = pygame.draw.rect(screen, (165, 242, 243), (iceX2, iceY2, 50, 50))
		ice2Rect = pygame.rect.Rect(iceX2, iceY2, 50, 50)
		ice3 = pygame.draw.rect(screen, (165, 242, 243), (iceX3, iceY3, 50, 50))
		ice3Rect = pygame.rect.Rect(iceX3, iceY3, 50, 50)
		ice4 = pygame.draw.rect(screen, (165, 242, 243), (iceX4, iceY4, 50, 50))
		ice4Rect = pygame.rect.Rect(iceX4, iceY4, 50, 50)
		ice5 = pygame.draw.rect(screen, (165, 242, 243), (iceX5, iceY5, 50, 50))
		ice5Rect = pygame.rect.Rect(iceX5, iceY5, 50, 50)
		if iceRect.colliderect(playerRect):
			print "You lose"
			exit()
		if ice2Rect.colliderect(playerRect):
			print "You lose"
			exit()
		if ice3Rect.colliderect(playerRect):
			print "You lose"
			exit()
		if ice4Rect.colliderect(playerRect):
			print "You lose"
			exit()
		if ice5Rect.colliderect(playerRect):
			print "You lose"
			exit()

		pygame.display.flip()
