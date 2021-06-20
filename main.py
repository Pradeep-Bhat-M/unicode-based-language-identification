import re

_blocks = []

def block(ch):
    #assert isinstance(ch, str) and len(ch) == 1, repr(ch)
    cp = ord(ch)
    for start, end, name in _blocks:
        if start <= cp <= end:
            return name


def _initBlocks(code_file):

    file = open(code_file)
    text = file.read()

    pattern = re.compile(r'([0-9A-F]+)\.\.([0-9A-F]+);\ (\S.*\S)')
    for line in text.splitlines():
        m = pattern.match(line)
        if m:
            start, end, name = m.groups()
            _blocks.append((int(start, 16), int(end, 16), name)) #converting hex string to integer

_initBlocks("unicodes.txt")


input_file = open("input.txt",encoding="utf8")
data = input_file.read()
data = re.sub(' +', ' ', data) #removing redundant multiple spaces
data = re.sub('\n+','\n',data) #removing extra lines


data_by_words = data.split(' ')
languages_dict = {}


for word in data_by_words:
    language = block(word[0])
    if language in languages_dict:
        languages_dict.get(language).append(word)
    else:
        languages_dict[language] = [word]

print(languages_dict)
