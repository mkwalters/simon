class solutionHandler():
	def __init__(self):
		self.number_of_solutions = 3
		self.current_solution = []
		self.index = 0
		self.time_between_flashes = time_between_flashes
		self.flash_times = []
	
	def build_solution_set(self):
		self.current_solution = []
		for i in range(0,self.number_of_solutions):
			roll = random.randint(1,4)
			self.current_solution.append(roll)
		self.number_of_solutions += 1
		print self.current_solution

	def build_solution_times(self):

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
			if pygame.time.get_ticks() > i and pygame.time.get_ticks() < i + 1000 :
				self.show_next_solution()
				self.flash_times.remove(i)

