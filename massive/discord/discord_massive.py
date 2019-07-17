import random

from massive import massivizer

MAX_MESSAGE_LENGTH = 2000
MAX_EMBED_FIELD_LENGTH = 1024

# These are the preferred mappings. Ideally, they don't look as out of place as the alternate
# ones, i.e. if possible, the background is blue and the text is white.
MAIN_MAPPINGS = {
	"0": "zero",
	"1": "one",
	"2": "two",
	"3": "three",
	"4": "four",
	"5": "five",
	"6": "six",
	"7": "seven",
	"8": "eight",
	"9": "nine",
	" ": "ok_hand",
	"*": "asterisk",
	"\"": "pause_button",
	".": "record_button",
	"!": "exclamation",
	"?": "question",
	"+": "heavy_plus_sign",
	",": "arrow_down_small",
	"-": "no_entry"
}

# These are the alternate mappings. Go wild.
ALTERNATE_MAPPINGS = {
	"a": ["a"],
	"b": ["b"],
	"i": ["information_source"],
	"m": ["m"],
	"o": ["o2"],
	"p": ["parking"],
	"x": ["negative_squared_cross_mark"]
}


def map_to_emoji(c, alternate_chance=0.0, main_mappings=None, alternate_mappings=None):
	if not main_mappings:
		main_mappings = MAIN_MAPPINGS

	if not alternate_mappings:
		alternate_mappings = ALTERNATE_MAPPINGS

	if 'A' <= c <= 'Z':
		c = c.lower()

	if 'a' <= c <= 'z':
		if c in alternate_mappings and random.random() < alternate_chance:
			return random.choice(alternate_mappings[c])

		return "regional_indicator_" + c

	if c in main_mappings:
		return main_mappings[c]

	return ""


def map_from_emoji(input_emoji, main_mappings=None, alternate_mappings=None):
	if not main_mappings:
		main_mappings = MAIN_MAPPINGS

	if not alternate_mappings:
		alternate_mappings = ALTERNATE_MAPPINGS

	if input_emoji.startswith("regional_indicator_"):
		return input_emoji[-1]

	for c, emoji in main_mappings.items():
		if emoji == input_emoji:
			return c

	for c, emojis in alternate_mappings.items():
		for emoji in emojis:
			if emoji == input_emoji:
				return c

	return ""


def demassivize(input_string, main_mappings=None, alternate_mappings=None):
	if not main_mappings:
		main_mappings = MAIN_MAPPINGS

	if not alternate_mappings:
		alternate_mappings = ALTERNATE_MAPPINGS

	output_string = ""

	emoji = False
	current_emoji = ""

	skip_next_space = False

	for c in input_string:
		if skip_next_space:
			skip_next_space = False

			if c == ' ':
				continue

		if c.isspace() and emoji:
			emoji = False
			output_string += ":" + current_emoji
			current_emoji = ""

		if c != ':':
			if emoji:
				current_emoji += c
			else:
				output_string += c

			continue

		emoji = not emoji

		if emoji:
			continue

		# :: is a colon and the start of a new emoji
		if not current_emoji:
			output_string += ":"
			emoji = True
			continue

		# Added mapped emoji to output

		mapped = map_from_emoji(
			current_emoji,
			main_mappings=main_mappings,
			alternate_mappings=alternate_mappings
		)

		if mapped:
			output_string += mapped
		else:
			output_string += ":" + current_emoji + ":"

		current_emoji = ""
		skip_next_space = True

	if emoji:
		output_string += ":" + current_emoji

	return output_string


def demassivize_recursively(input_string, main_mappings=None, alternate_mappings=None):
	output_string = input_string
	next_output_string = ""

	while output_string != next_output_string:
		if next_output_string:
			output_string = next_output_string

		demassivized = demassivize(
			output_string,
			main_mappings=main_mappings,
			alternate_mappings=alternate_mappings
		)
		next_output_string = demassivized

	return output_string


class Massive(massivizer.Massivizer):
	def __init__(
			self,
			newlines_separate_parts=False,
			max_part_length=MAX_MESSAGE_LENGTH,
			alternate_chance=0.0
	):
		super().__init__(newlines_separate_parts, max_part_length)
		self.alternate_chance = alternate_chance
		self.main_mappings = None
		self.alternate_mappings = None
		self._ends_with_emoji = False

	@property
	def alternate_chance(self):
		return self.__alternate_chance

	@alternate_chance.setter
	def alternate_chance(self, chance):
		self.__alternate_chance = max(0.0, min(chance, 1.0))

	@property
	def main_mappings(self):
		return self.__main_mappings

	@main_mappings.setter
	def main_mappings(self, mappings):
		self.__main_mappings = mappings or MAIN_MAPPINGS

	@property
	def alternate_mappings(self):
		return self.__alternate_mappings

	@alternate_mappings.setter
	def alternate_mappings(self, mappings):
		self.__alternate_mappings = mappings or ALTERNATE_MAPPINGS

	@property
	def _ends_with_emoji(self):
		return self._thread_local.ends_with_emoji

	@_ends_with_emoji.setter
	def _ends_with_emoji(self, flag):
		self._thread_local.ends_with_emoji = flag

	def map_to_emoji(self, c):
		return map_to_emoji(
			c,
			self.alternate_chance,
			main_mappings=self.main_mappings,
			alternate_mappings=self.alternate_mappings
		)

	def preprocess_input(self, input_string):
		return input_string

	def convert(self, c):
		self._ends_with_emoji = False

		emoji = self.map_to_emoji(c)

		if emoji:
			self._ends_with_emoji = True
			return ":" + emoji + ": "

		return c

	def finalize_output(self, output_string):
		# If the output ends with an emoji, there is an extra space at the end that must be removed
		return output_string[:-1] if self._ends_with_emoji else output_string
