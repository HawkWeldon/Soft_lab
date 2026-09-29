import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
bulleted = ""

for line in range(len(lines)):
    print(lines[line])
    lines[line] = '*' + lines[line]
    bulleted += lines[line] + '\n'

pyperclip.copy(bulleted)