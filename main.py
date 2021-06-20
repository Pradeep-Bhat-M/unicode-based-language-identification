import re

blocks = []
languages_dict = {}

def parseInput():
    input_file = open("200.txt",encoding="utf8")
    data = input_file.read()
    data = re.sub(' +', ' ', data)                  # Removing redundant multiple spaces
    data = re.sub('\n+','\n',data)                  # Removing extra lines
    return(data.split(' '))


def addInDictionary(language):
    if language in languages_dict:
        languages_dict.get(language).append(word)
    else:
        languages_dict[language] = [word]

def block(unicode):
    for start, end, name in blocks:
        if start <= unicode <= end:
            return (start, end, name)

def makeBlocks(code_file):                          # Loading all the unicode ranges

    file = open(code_file)
    text = file.read()

    pattern = re.compile(r'([0-9A-F]+)\.\.([0-9A-F]+);\ (\S.*\S)')
    for line in text.splitlines():
        m = pattern.match(line)
        if m:
            start, end, name = m.groups()
            blocks.append((int(start, 16), int(end, 16), name))    # Converting hexString to Integer


makeBlocks("unicodes.txt")
past_lang = (65, 122, 'English')

dataByWOrds = parseInput()

for word in dataByWOrds:
    unicode = ord(word[0])                          # Fetching the unicode of the character
    if past_lang[0] <= unicode <= past_lang[1]:
        language = past_lang[2]
    else: 
        past_lang = block(unicode)
        language = past_lang[2]

    addInDictionary(language)

print(languages_dict)




