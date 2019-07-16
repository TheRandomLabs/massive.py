# massive.py

Utilities for converting text to massive text, especially on Discord.

**Note:** aLtErNaTiNg CaPs has been dubbed *Vanessa-case* or *Vanessa text* by massive.py.

**Example:**

```python
from massive.discord import discord_massive

massivizer = discord_massive.Massive(alternate_chance=1.0)
massivizer.swap_random_chars(chance=0.02)

for part in massivizer.massivize("Massive text"):
	print(part)
```

The above code generates this:

![](https://raw.githubusercontent.com/TheRandomLabs/massive.py/master/example.png)
