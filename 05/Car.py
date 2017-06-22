class Car:
	d = ['North', 'East', 'South', 'West']
	def __init__(self, kind):
		# Attributes
		self._kind = kind
		self._verosity = 0
		self._direction = 0

	# Methods
	# コマンド
	def speed_up(self, dv):
		self._verosity += dv

	def speed_down(self, dv):
		self._verosity -= dv

	def turn_right(self):
		self._direction += 1
		self._direction %= 4

	def turn_left(self):
		self._direction -= 1
		self._direction %= 4

	# 問い合わせ]
	def kind(self):
		return self._kind

	def info(self):
		return "Verosity is {}km/h\nDirection is {}".format(self._verosity, self.d[self._direction])


my_car = Car('Toyota')
print(my_car.info())

print()

my_car.speed_up(10)
my_car.turn_right()
print(my_car.info())