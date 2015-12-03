
class Button():
	def __init__(self):
		self.lit = False
		self.turn_off_lights_timer = 0
		self.turn_of_confirmation_light_timer = 0
	def draw_self(self):
		if self.lit == False:
			pygame.draw.rect(gameDisplay, self.color, [self.x, self.y, button_length, button_length])
		else:
			pygame.draw.rect(gameDisplay, self.lit_color, [self.x, self.y, button_length, button_length])


	def light_up(self):
		self.lit = True
		self.turn_off_lights_timer = pygame.time.get_ticks() + 500


	def light_up_for_click_confirmation(self):
		self.lit = True
		self.turn_off_lights_timer = pygame.time.get_ticks() + 100


	def turn_off_lights(self):
		if pygame.time.get_ticks() > i.turn_off_lights_timer: #turn this bad boy into a function
			i.lit = False

	def loop_tasks(self):
		self.draw_self()
		self.turn_off_lights()


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
	
