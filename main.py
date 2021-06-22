import re

blocks = []
languages_dict = {}
prevLang = (65, 122, 'English')


def parseInput(inputFile):
    inFile = open(inputFile, 'r', encoding="utf8")
    data = inFile.read()
    data = re.sub(' +', ' ', data)                  # Removing redundant multiple spaces
    data = re.sub('\n+',' ', data)                 # Removing extra lines
    data = re.sub('/+','',data)
    data = re.sub(',+','',data)
    data = re.sub('\.+','',data)



    return data.split(' ')


def addInDictionary(language):  # Adding words into a dictionary
    if language in languages_dict:
        languages_dict.get(language).append(word)
    else:
        languages_dict[language] = [word]


def block(unicode):  # Comparing Unicode ranges to find the script
    for start, end, name in blocks:
        if start <= unicode <= end:
            return start, end, name
    return 0, 0, "No Such Script Can be Identified"


def makeBlocks(code_file):  # Loading all the Unicode ranges

    file = open(code_file)
    text = file.read()

    pattern = re.compile(r'([0-9A-F]+)\.\.([0-9A-F]+);\ (\S.*\S)')
    for line in text.splitlines():
        m = pattern.match(line)
        if m:
            start, end, name = m.groups()
            blocks.append((int(start, 16), int(end, 16), name))  # Converting hexString to Integer


makeBlocks("unicodes.txt")
dataByWOrds = parseInput("input.txt")

for word in dataByWOrds:
    # word = re.sub('\W+', '', word)  # Removing Special Characters
    # word = re.sub('[0-9]+', '', word)  # Removing Numbers (Arabic)
    if not word:
        continue
    unicode = ord(word[0])  # Fetching the unicode of the character
    if prevLang[0] <= unicode <= prevLang[1]:
        language = prevLang[2]
    else:
        prevLang = block(unicode)  # Updating prevLang, so that we need not search the whole unicode block again.
        language = prevLang[2]


    addInDictionary(language)

print(languages_dict)
