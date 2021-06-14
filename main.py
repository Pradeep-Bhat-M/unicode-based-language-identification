import re

def block(ch):
    assert isinstance(ch, str) and len(ch) == 1, repr(ch)
    cp = ord(ch)
    for start, end, name in _blocks:
        if start <= cp <= end:
            return name


def _initBlocks(code_file):

    file = open(code_file)
    text = file.read()

    global _blocks
    _blocks = []

    pattern = re.compile(r'([0-9A-F]+)\.\.([0-9A-F]+);\ (\S.*\S)')
    for line in text.splitlines():
        m = pattern.match(line)
        if m:
            start, end, name = m.groups()
            _blocks.append((int(start, 16), int(end, 16), name))

_initBlocks("unicodes.txt")

data = input(" Enter The text to for Language Identification : ")
language = "Invalid Identification"
for ch in data:
    language = block(ch)



print("\n The Entered Text is identified to be in " + language + " Script!!")