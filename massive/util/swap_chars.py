import random


class RandomCharSwapper(object):
	def __init__(self, predicate, swap_chance):
		assert isinstance(predicate('a'), bool), "predicate does not return a bool"
		assert swap_chance > 0, "swap_chance is not positive"

		self.predicate = predicate
		self.swap_chance = swap_chance

	def swap(self, input_string):
		return swap_random_chars(input_string, self.predicate, self.swap_chance)


# Swaps random sets of two characters if predicate returns True for both characters in the sets
# Each viable set has an n in swap_chance chance of being swapped
def swap_random_chars(input_string, predicate, swap_chance):
	assert input_string, "input_string is empty"
	assert isinstance(predicate('a'), bool), "predicate does not return a bool"
	assert swap_chance > 0, "swap_chance is not positive"

	to_swap = []

	for i in range(0, len(input_string) - 1, 2):
		c1 = input_string[i]
		c2 = input_string[i + 1]

		if c1 != c2 and predicate(c1) and predicate(c2) and random.randint(0, swap_chance) == 0:
			to_swap.append(i)

	chars = list(input_string)

	for i in to_swap:
		chars[i], chars[i + 1] = chars[i + 1], chars[i]

	return "".join(chars)
