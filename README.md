# massive.py

Utilities for converting text to massive text, especially on Discord.

*Vanessa-case* or *Vanessa text* is massive.py's name for aLtErNaTiNg CaPs.

**Example:**

```python
from massive.discord import discord_massive

massivized = discord_massive.Massive("Massive text").\
    use_alternate(True).\
    swap_random_chars(chance=3).\
    massivize()

for part in massivized:
    print(part)
```

The above code generates this:

![](example.png)
