from massive import massivizer


class Vanessa(massivizer.Massivizer):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.__uppercase = False

	def preprocess_input(self, input_string):
		return input_string.lower()

	def convert(self, c):
		self.__uppercase = not self.__uppercase

		if self.__uppercase:
			return c.upper()

		return c

	def finalize_output(self, output_string):
		return output_string
