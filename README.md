# massive.py

[![Foo](http://badge.fury.io/py/massive.py.svg)](http://badge.fury.io/py/massive.py)

Utilities for converting text to massive text, especially on Discord.

## Installation

	$ pip install massive.py

## Example

```python
from massive.discord import discord_massive

massivizer = discord_massive.Massive(alternate_chance=1.0)
massivizer.swap_random_chars(chance=0.02)

for part in massivizer.massivize("Massive text"):
	print(part)
```

The above code generates this:

![](https://raw.githubusercontent.com/TheRandomLabs/massive.py/master/example.png)

## Massivizers

* **Vanessa-case/Vanessa text**: aLtErNaTiNg CaPs.
* **Massive text (Discord)**: `regional_indicator` and other emojis on Discord.
* **Massive Vanessa text (Discord)**: A combination of massive text and lower case letters.
