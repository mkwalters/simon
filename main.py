import pygame
import math
import random
pygame.init()

display_width = 710
display_height = 600
button_length = 200
still_playing = True
green_button_x = 100
green_button_y = 75
red_button_x = 400
red_button_y = 75
yellow_button_x = 100
yellow_button_y = 350
blue_button_x = 400
blue_button_y = 350

background_color = (200,200,200)

red_color = (128,0,0)
green_color = (0,128,0)
yellow_color = (128,128,0)
blue_color = (0,0,128)

red_lit_color = (255,0,0)
green_lit_color = (0,255,0)
yellow_lit_color = (255,255,0)
blue_lit_color = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Simon')
clock = pygame.time.Clock()


class Player():

	def click_square(self,x,y):
		solutions.show_solution_set()



class solutionHandler():
	def __init__(self):
		self.number_of_solutions = 3
		self.current_solution = []
		self.index = 0
		self.time_between_flashes = 200
	
	def build_solution_set(self):
		for i in range(0,self.number_of_solutions):
			roll = random.randint(1,4)
			self.current_solution.append(roll)
		print self.current_solution
		self.number_of_solutions += 1
	
	def show_solution_set(self):
		if self.index < self.number_of_solutions - 1:
			self.show_solution_helper(self.current_solution[self.index])
			self.index += 1
		
	def show_solution_helper(self, roll):
		if roll == 1:
			green_button.light_up()
		elif roll == 2:
			red_button.light_up()
		elif roll == 3:
			yellow_button.light_up()
		else:
			blue_button.light_up()

class Button():
	def __init__(self):
		self.lit = False
		self.turn_off_lights_timer = 0
	def draw_self(self):
		if self.lit == False:
			pygame.draw.rect(gameDisplay, self.color, [self.x, self.y, button_length, button_length])
		else:
			pygame.draw.rect(gameDisplay, self.lit_color, [self.x, self.y, button_length, button_length])


	def light_up(self):
		self.lit = True
		self.turn_off_lights_timer = pygame.time.get_ticks() + 1000

class RedButton(Button):
	def __init__(self):
		Button.__init__(self)
		self.color = red_color
		self.lit_color = red_lit_color
		self.x = red_button_x
		self.y = red_button_y
	

class GreenButton(Button):
	def __init__(self):
		Button.__init__(self)
		self.color = green_color
		self.lit_color = green_lit_color
		self.x = green_button_x
		self.y = green_button_y
	

class YellowButton(Button):
	def __init__(self):
		Button.__init__(self)
		self.color = yellow_color
		self.lit_color = yellow_lit_color
		self.x = yellow_button_x
		self.y = yellow_button_y
	

class BlueButton(Button):
	def __init__(self):
		Button.__init__(self)
		self.color = blue_color
		self.lit_color = blue_lit_color
		self.x = blue_button_x
		self.y = blue_button_y
	

player = Player()
green_button = GreenButton()
red_button = RedButton()
yellow_button = YellowButton()
blue_button = BlueButton()


buttons = [green_button, red_button, yellow_button, blue_button]

solutions= solutionHandler()
solutions.build_solution_set()




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

	pygame.display.update()
	clock.tick(30)
