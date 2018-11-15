import re

def disemvowel(s):
    return re.sub(re.compile('a|A|e|E|i|I|o|O|u|U'), '', s)

    