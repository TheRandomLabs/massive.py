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


def map_to_emoji(c, use_alternate, main_mappings=None, alternate_mappings=None):
	if not main_mappings:
		main_mappings = MAIN_MAPPINGS

	if not alternate_mappings:
		alternate_mappings = ALTERNATE_MAPPINGS

	if 'A' <= c <= 'Z':
		c = c.lower()

	if 'a' <= c <= 'z':
		if use_alternate and c in alternate_mappings and random.choice([True, False]):
			return random.choice(alternate_mappings[c])

		return "regional_indicator_" + c

	if c in main_mappings:
		return main_mappings[c]

	return ""


class Massive(massivizer.Massivizer):
	def __init__(self, input_string):
		super().__init__(input_string)

		self.alternate = False
		self.ends_with_emoji = False

		self.main_mappings = MAIN_MAPPINGS
		self.alternate_mappings = ALTERNATE_MAPPINGS

	def is_using_alternate(self):
		return self.alternate

	def use_alternate(self, flag):
		self.alternate = flag
		return self

	def with_main_mappings(self, mappings):
		assert mappings, "mappings is empty"
		self.main_mappings = mappings

	def with_alternate_mappings(self, mappings):
		assert mappings, "mappings is empty"
		self.alternate_mappings = mappings

	def map_to_emoji(self, c):
		return map_to_emoji(
			c,
			self.alternate,
			main_mappings=self.main_mappings,
			alternate_mappings=self.alternate_mappings
		)

	def convert(self, c):
		self.ends_with_emoji = False

		emoji = self.map_to_emoji(c)

		if emoji:
			self.ends_with_emoji = True
			return ":" + emoji + ": "

		return c

	def modify_output(self, output_string):
		# If the output ends with an emoji, there is an extra space at the end that must be removed
		return output_string[:-1] if self.ends_with_emoji else output_string
