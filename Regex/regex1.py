import re
"""



matches = re.finditer(r"(Mr|Mrs|Ms)\.?\s\w+",test_string)
#print(matches)

#Match ,# search , # findall
#group ,span ,start,end
for i in matches:

 print(i)

"""

test_string = """

Mr Simpson
Mrs Simpson
Mr.Brown
Ms Smith
Mr.T

"""



k = "aaaabbbccccdefgha"

new = re.findall("a$",k)

print(new)

