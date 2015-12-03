import pygame
import math
import random
pygame.init()

execfile("Player.py")
execfile("constants.py")
execfile("solutionHandler.py")
execfile("Button.py")
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Simon')
clock = pygame.time.Clock()
player = Player()
green_button = GreenButton()
red_button = RedButton()
yellow_button = YellowButton()
blue_button = BlueButton()
score_font = pygame.font.Font(None, score_display_size)
loss_display_font = pygame.font.Font(None, score_display_size)

buttons = [green_button, red_button, yellow_button, blue_button]

solutions= solutionHandler()
solutions.build_solution_set()
solutions.build_solution_times()

while still_playing:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse = pygame.mouse.get_pos()
			player.click_square(mouse[0],mouse[1])


	gameDisplay.fill(background_color)
	for i in buttons: 
		i.loop_tasks()
	
	solutions.loop_tasks()
	pygame.display.update()
	clock.tick(30)
