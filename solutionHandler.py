
class solutionHandler():
	def __init__(self):
		self.number_of_solutions = 2
		self.current_solution = []
		self.index = 0
		self.time_between_flashes = time_between_flashes
		self.flash_times = []
		self.currently_flashing_solution = False
		self.loss = False
	
	def build_solution_set(self):
		self.current_solution = []
		for i in range(0,self.number_of_solutions):
			roll = random.randint(1,4)
			self.current_solution.append(roll)
		self.number_of_solutions += 1
		print self.current_solution

	def build_solution_times(self):
		
		self.currently_flashing_solution = True
		print "okay im starting up"

		current_time = pygame.time.get_ticks()
		
		for i in range(0,self.number_of_solutions - 1):
			self.flash_times.append(current_time + (i * self.time_between_flashes))
	
	def show_next_solution(self):
		if self.index < self.number_of_solutions - 1:
			self.show_next_solution_helper(self.current_solution[self.index])
			self.index +=1
			
		
	def show_next_solution_helper(self, roll):
		if roll == 1:
			green_button.light_up()
		elif roll == 2:
			red_button.light_up()
		elif roll == 3:
			yellow_button.light_up()
		else:
			blue_button.light_up()


	def master_solution_flasher(self):
		
		for i in self.flash_times:
			# the 1000 constant isnt important
			#im just trying to make sure the game doesnt pass a flash time
			if pygame.time.get_ticks() > i and pygame.time.get_ticks() < i + 1000 :
				self.show_next_solution()
				#this is mutating the list
				#if there are crashes start here:
				self.flash_times.remove(i)
				if self.flash_times == []:
					#uncomment me for debugging
					#print "finishing up the flash"
					self.currently_flashing_solution = False
					self.index = 0


	def check_user_solutions(self):
		# this is just a prototype
		#im not sure if i need to subtract on
		if len(player.current_guess) == self.number_of_solutions -1:
			print "im being checked now"
			if self.current_solution == player.current_guess:
				player.current_guess = []
				solutions.build_solution_set()
				solutions.build_solution_times()
			else:
				self.loss = True
				player.current_guess = []

	def display_number_of_solutions(self):
		score_display = score_font.render(str(self.number_of_solutions - 1), 0, score_display_color)
		gameDisplay.blit(score_display, (score_display_x,score_display_y))


	def display_losing_message(self):
		if self.loss == True:
			loss_display = loss_display_font.render(loss_message, 0, loss_display_color)
			gameDisplay.blit(loss_display, (loss_display_x,loss_display_y))
	

	def loop_tasks(self):
		solutions.master_solution_flasher()
		solutions.check_user_solutions()
		solutions.display_number_of_solutions()
		solutions.display_losing_message()

