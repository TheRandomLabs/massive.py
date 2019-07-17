from enum import Enum

from massive import massivizer


class CaseBehavior(Enum):
	START_LOWERCASE = 1
	ALWAYS_START_LOWERCASE = 2
	START_UPPERCASE = 3
	ALWAYS_START_UPPERCASE = 4


class Vanessa(massivizer.Massivizer):
	def __init__(self, case_behavior=CaseBehavior.START_LOWERCASE, **kwargs):
		super().__init__(**kwargs)
		self.case_behavior = case_behavior
		self._lowercase = True

	@property
	def _lowercase(self):
		return self._thread_local.lowercase

	@_lowercase.setter
	def _lowercase(self, flag):
		self._thread_local.lowercase = flag

	def preprocess_input(self, input_string):
		return input_string.lower()

	def convert(self, c):
		upper = c.upper()

		if c == upper:
			return c

		self._lowercase = not self._lowercase
		return c if self._lowercase else upper

	def finalize_output(self, output_string):
		return output_string

	def massivize(self, input_string):
		if self.case_behavior == CaseBehavior.ALWAYS_START_LOWERCASE:
			self._lowercase = True
		elif self.case_behavior == CaseBehavior.ALWAYS_START_UPPERCASE:
			self._lowercase = False

		return super().massivize(input_string)
