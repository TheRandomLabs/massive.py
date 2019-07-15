import random

from massive import massivizer
from massive.discord import discord_massive


class MassiveVanessa(massivizer.Massivizer):
	def __init__(self, input_string):
		super().__init__(input_string)
		self.use_alternate = True
		self.ends_with_emoji = False

	def is_using_alternate(self):
		return self.use_alternate

	def use_alternate(self, flag):
		self.use_alternate = flag

	def convert(self, c):
		self.ends_with_emoji = False

		if c == ' ':
			return "  "

		lower = random.choice([True, False])

		if 'a' <= c.lower() <= 'z':
			if lower:
				return c.lower()

			emoji = discord_massive.map_to_emoji(c, self.use_alternate)

			if emoji:
				self.ends_with_emoji = True
				return ":" + emoji + ": "

			return c.upper()

		return c

	def modify_output(self, line):
		return line[:-1] if self.ends_with_emoji else line
