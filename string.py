import re

def splitStringBySpacesRespectQuotes(string):
    return [t.strip('"') for t in re.findall(r'[^\s"]+|"[^"]*"', string)]