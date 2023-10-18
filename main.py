
#context manager, preffered use
with open("mydefaults.ini") as defaultf: 
    data = defaultf.read()

#from blob for text to readable by the editor line by line
lines = data.split("\n")
key_value_ini = dict()
#len length
print(len(lines))
for line in lines:
    if "=" in line:
# Itterates line by line by line 
        fields = line.split("=")
        print(len(fields))
# Now create the dictionary
#takes lang, makes a key out of it, then moves to the next word to turn it into a key
        key_value_ini[fields[0]] = fields[1]
print(key_value_ini)
