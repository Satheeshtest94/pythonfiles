import re

text = "hey hai how hey"

inp = re.compile("[A-Z][a-z]*[0-9][a-z]*")
matches = inp.sub("ab")

print(matches)
