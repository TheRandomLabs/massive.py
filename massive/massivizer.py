import abc

from massive.util import swap_chars


class Massivizer(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, input_string):
		assert input_string, "input_string is empty"

		self.input_string = input_string
		self.newlines_start_new_parts = False
		self.max_part_length = 0

		self.input_modifiers = []
		self.random_char_swapper = None

	def get_input_string(self):
		return self.input_string

	def do_newlines_separate_parts(self):
		return self.newlines_start_new_parts

	def newlines_separate_parts(self, flag):
		self.newlines_start_new_parts = flag
		return self

	def get_max_part_length(self):
		return self.max_part_length

	def set_max_part_length(self, length):
		assert length >= 0, "max_part_length is negative"
		self.max_part_length = length
		return self

	def get_input_modifiers(self):
		return self.input_modifiers

	def swap_random_chars(self, predicate=lambda c: 'a' <= c.lower() <= 'z', chance=50):
		self.random_char_swapper = swap_chars.RandomCharSwapper(predicate, chance)
		return self

	def modify_input(self, line):
		return line

	@abc.abstractmethod
	def convert(self, c):
		return c

	def modify_output(self, line):
		return line

	def apply_input_modifiers(self, line):
		if self.random_char_swapper:
			line = self.random_char_swapper.swap(line)

		line = self.modify_input(line)

		for input_modifier in self.input_modifiers:
			line = input_modifier(line)

		return line

	def massivize(self):
		input_lines = []
		current_line = ""

		for c in self.input_string:
			if c == '\r':
				continue

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
			input_line = self.apply_input_modifiers(input_line)

			for c in input_line:
				to_add = self.convert(c)
				length = len(to_add)

				if self.max_part_length is 0 or line_length + length <= self.max_part_length:
					current_line += to_add
					line_length += length
				else:
					massivized.append(self.modify_output(current_line))
					current_line = to_add
					line_length = length

			massivized.append(self.modify_output(current_line))
			current_line = ""
			line_length = 0

		return massivized
