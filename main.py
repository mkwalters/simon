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

buttons = [green_button, red_button, yellow_button, blue_button]

solutions= solutionHandler()

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
		i.draw_self()



		if pygame.time.get_ticks() > i.turn_off_lights_timer:
			i.lit = False
	
	solutions.master_solution_flasher()
	pygame.display.update()
	clock.tick(30)
