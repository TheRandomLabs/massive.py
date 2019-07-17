from massive import massivizer


class Vanessa(massivizer.Massivizer):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.__uppercase = False

	def preprocess_input(self, input_string):
		return input_string.lower()

	def convert(self, c):
		upper = c.upper()

		if c == upper:
			return c

		self.__uppercase = not self.__uppercase
		return upper if self.__uppercase else c

	def finalize_output(self, output_string):
		return output_string
