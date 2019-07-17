import abc
import threading

from massive.util import swap_chars


class Massivizer(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, newlines_separate_parts=False, max_part_length=0):
		self.newlines_start_new_parts = newlines_separate_parts
		self.max_part_length = max_part_length
		self.input_preprocessors = []
		self.random_char_swapper = None
		self._thread_local = threading.local()

	@property
	def max_part_length(self):
		return self.__max_part_length

	@max_part_length.setter
	def max_part_length(self, length):
		self.__max_part_length = 0 if length < 0 else length

	@property
	def input_preprocessors(self):
		return self.__input_preprocessors

	@input_preprocessors.setter
	def input_preprocessors(self, modifiers):
		self.__input_preprocessors = modifiers or []

	def swap_random_chars(self, char_predicate=lambda c: 'a' <= c.lower() <= 'z', chance=0.5):
		self.random_char_swapper = swap_chars.RandomCharSwapper(char_predicate, chance)

	@abc.abstractmethod
	def preprocess_input(self, input_string):
		return input_string

	@abc.abstractmethod
	def convert(self, c):
		return c

	@abc.abstractmethod
	def finalize_output(self, output_string):
		return output_string

	def massivize(self, input_string):
		input_lines = []
		current_line = ""

		for c in input_string:
			if c == '\r':
				continue

			# Useful if newlines are used to mark separate parts/messages
			if c == '\n' and self.newlines_start_new_parts:
				input_lines.append(current_line)
				current_line = ""
				continue

			current_line += c

		if current_line:
			input_lines.append(current_line)
			current_line = ""

		massivized = []
		line_length = 0

		for input_line in input_lines:
			input_line = self.__apply_input_preprocessors(input_line)

			for c in input_line:
				to_add = self.convert(c)
				length = len(to_add)

				if self.max_part_length == 0 or line_length + length <= self.max_part_length:
					current_line += to_add
					line_length += length
				else:
					massivized.append(self.finalize_output(current_line))
					current_line = to_add
					line_length = length

			massivized.append(self.finalize_output(current_line))
			current_line = ""
			line_length = 0

		return massivized

	# Applies random char swaps and custom input modifiers as well as preprocess_input
	def __apply_input_preprocessors(self, input_string):
		if self.random_char_swapper:
			input_string = self.random_char_swapper.swap(input_string)

		input_string = self.preprocess_input(input_string)

		for input_modifier in self.input_preprocessors:
			input_string = input_modifier(input_string)

		return input_string
