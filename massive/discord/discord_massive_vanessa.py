import random

from massive.discord import discord_massive


class MassiveVanessa(discord_massive.Massive):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def convert(self, c):
		self.__ends_with_emoji = False

		if c == ' ':
			return "  "

		lower = random.choice([True, False])

		if 'a' <= c.lower() <= 'z':
			if lower:
				return c.lower()

			emoji = self.__map_to_emoji(c)

			if emoji:
				self.__ends_with_emoji = True
				return ":" + emoji + ": "

			return c.upper()

		return c
