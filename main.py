import re

blocks = []

def block(ch):
    unicode = ord(ch)
    for start, end, name in blocks:
        if start <= unicode <= end:
            return name


def initBlocks(code_file):

    file = open(code_file)
    text = file.read()

    pattern = re.compile(r'([0-9A-F]+)\.\.([0-9A-F]+);\ (\S.*\S)')
    for line in text.splitlines():
        m = pattern.match(line)
        if m:
            start, end, name = m.groups()
            blocks.append((int(start, 16), int(end, 16), name))

initBlocks("unicodes.txt")



input_file = open("input.txt",encoding="utf8")
data = input_file.read()

data_by_words = data.split(' ')
languages_found = set()

for word in data_by_words:
    language = block(word[0])
    languages_found.add(language)

print(languages_found)
