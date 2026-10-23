class Level:
	def __init__(
		self
	) -> None:
	
		self.MAX_EXPERIENCE_POINTS_PER_LEVEL: float = None
		self.__current_experience_points	: float = None
		self.total_experience_points		: float = None

		self.current_level: int = 0

	@property
	def current_experience_points(
		self
	) -> float:

		return self.__current_experience_points
	
	@current_experience_points.setter
	def current_experience_points(
		self,
		new_experience_points: float
	) -> None:

		if new_experience_points < 0:
			raise ValueError("Non-positive values are invalid for experiences points.")
		
		self.__current_experience_points = new_experience_points
	
	def level_up(
		self
		# skill or entity reference
	) -> None:
		
		self.current_level += 1
		# Publish an event about leveling up
	
	def receive_experience_points(
		self,
		new_experience_points: float
	) -> None:

		self.total_experience_points += new_experience_points

		remainig_points_to_next_level: float = self.MAX_EXPERIENCE_POINTS_PER_LEVEL\
											  -self.__current_experience_points

		exceeding_points: float = remaining_points_to_next_level\
								 +new_experience_points\
						  		 -self.MAX_EXPERIENCE_POINTS_PER_LEVEL
		
		if not exceeding_points < 0:
			self.__current_experience_points += new_experience_points
			return

		self.level_up()
		self.__current_experience_points = exceeding_points
