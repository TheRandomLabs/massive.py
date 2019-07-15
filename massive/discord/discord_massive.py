import random

from massive import massivizer


MAX_MESSAGE_LENGTH = 2000
MAX_EMBED_FIELD_LENGTH = 1024

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

ALTERNATE_MAPPINGS = {
	"a": ["a"],
	"b": ["b"],
	"m": ["m"],
	"o": ["o2"],
	"p": ["parking"],
	"x": ["negative_squared_cross_mark"]
}


def map_to_emoji(c, use_alternate):
	if 'A' <= c <= 'Z':
		c = c.lower()

	if 'a' <= c <= 'z':
		if use_alternate and c in ALTERNATE_MAPPINGS and random.choice([True, False]):
			return random.choice(ALTERNATE_MAPPINGS[c])

		return "regional_indicator_" + c

	if c in MAIN_MAPPINGS:
		return MAIN_MAPPINGS[c]

	return ""


class Massive(massivizer.Massivizer):
	def __init__(self, input_string):
		super().__init__(input_string)
		self.use_alternate = False

	def is_using_alternate(self):
		return self.use_alternate

	def use_alternate(self, flag):
		self.use_alternate = flag
		return self

	def modify_input(self, line):
		return line

	def convert(self, c):
		emoji = map_to_emoji(c, self.use_alternate)

		if emoji:
			return ":" + emoji + ": "

		return c

	def modify_output(self, line):
		# Remove extra space - TODO what happens when the line doesn't end with an emoji?
		return line[:-1]
