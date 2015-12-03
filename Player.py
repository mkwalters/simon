
class Player():
	def __init__(self):
		self.current_guess = []

	def click_square(self,mousex,mousey):
		#solutions.build_solution_set()
		#solutions.build_solution_times()
		if solutions.currently_flashing_solution == False:
			self.guess_helper(mousex, mousey)

	def make_a_guess(self, color):
		#this method is being called by guess helper
		#i guess i should switch the names...
		if color == "green":
			self.current_guess.append(1)
			green_button.light_up_for_click_confirmation()
		elif color == "red":
			self.current_guess.append(2)
			red_button.light_up_for_click_confirmation()
		elif color == "yellow":
			self.current_guess.append(3)
			yellow_button.light_up_for_click_confirmation()
		else:
			self.current_guess.append(4)
			blue_button.light_up_for_click_confirmation()
		print self.current_guess

	def guess_helper(self,x,y):

		# im so sorry if you have to read this mess....
		# this function just checks the bounds of the users mouse clicks
		# its checking the x positions and then the y positions

		if x > left_x and x < left_x + button_length:
			if y > top_y and y < top_y + button_length:
				self.make_a_guess("green")
			elif y > bottom_y and y < bottom_y + button_length:
				self.make_a_guess("yellow")
		elif x > right_x and x < right_x + button_length:
			if y > top_y and y < top_y + button_length:
				self.make_a_guess("red")
			elif y > bottom_y and y < bottom_y + button_length:
				self.make_a_guess("blue")

