import random


class RandomCharSwapper(object):
	def __init__(self, char_predicate, swap_chance):
		self.char_predicate = char_predicate
		self.swap_chance = swap_chance

	@property
	def swap_chance(self):
		return self.__swap_chance

	@swap_chance.setter
	def swap_chance(self, chance):
		self.__swap_chance = max(0.0, min(chance, 1.0))

	# Swaps random sets of two characters if predicate returns True for both characters in the sets
	def swap(self, input_string):
		to_swap = []

		for i in range(0, len(input_string) - 1, 2):
			c1 = input_string[i]
			c2 = input_string[i + 1]

			if c1 == c2:
				continue

			if not self.char_predicate(c1) or not self.char_predicate(c2):
				continue

			if random.random() < self.swap_chance:
				to_swap.append(i)

		chars = list(input_string)

		for i in to_swap:
			chars[i], chars[i + 1] = chars[i + 1], chars[i]

		return "".join(chars)

	@classmethod
	def swap_random(cls, predicate, swap_chance, input_string):
		return cls(predicate, swap_chance).swap(input_string)
