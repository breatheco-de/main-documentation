import requests
import re

def findLinksMore(textOfFile):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', textOfFile)
    return url

longText = requests.get('https://raw.githubusercontent.com/breatheco-de/main-documentation/master/README.md').text
#print(longText)
print(findLinksMore(longText))
