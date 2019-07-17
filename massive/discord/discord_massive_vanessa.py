import random

from massive.discord import discord_massive


class MassiveVanessa(discord_massive.Massive):
	def __init__(self, massive_chance=0.5, **kwargs):
		super().__init__(**kwargs)
		self.massive_chance = massive_chance

	@property
	def massive_chance(self):
		return self.__massive_chance

	@massive_chance.setter
	def massive_chance(self, chance):
		self.__massive_chance = max(0.0, min(chance, 1.0))

	def convert(self, c):
		self.__ends_with_emoji = False

		if c == ' ':
			return "  "

		lower = random.random() < self.massive_chance

		if 'a' <= c.lower() <= 'z':
			if lower:
				return c.lower()

			emoji = self.map_to_emoji(c)

			if emoji:
				self.__ends_with_emoji = True
				return ":" + emoji + ": "

			return c.upper()

		return c
