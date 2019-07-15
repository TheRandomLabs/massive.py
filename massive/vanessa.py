from massive import massivizer


class Vanessa(massivizer.Massivizer):
	def __init__(self, input_string):
		super().__init__(input_string)
		self.uppercase = False

	def convert(self, c):
		self.uppercase = not self.uppercase

		if self.uppercase:
			return c.upper()

		return c.lower()
