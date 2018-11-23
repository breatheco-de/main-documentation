import requests
import re
from pathlib import Path

def findLinksMore(textOfFile):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', textOfFile)
    return url

def md_scraper(fileToWork):
    mdHandler = open(fileToWork)
    urlList = []
    for line in mdHandler:
        #if len(findLinksMore(line)) > 3:
        urlsFound = findLinksMore(line)
        if len(urlsFound) != 0:
            urlList.append(re.sub('[\>\)\"\'\?\[\]\*]','',str(urlsFound)))

    print('\n**results of scraping',fileToWork+'**\n')

    for element in urlList:
        while element.find(',') != -1:
            urlStringLong = element.split(",")
            element = urlStringLong[0]

        while element.find(" ") != -1:
                urlStringLong = element.split(" ")
                element = urlStringLong[0]

        md_response = requests.get(str(element).strip())
        if md_response.status_code == 200:
            verboseResponse = '200 : OK'
        else:
            verboseResponse = str(md_response.status_code) + ' : Bad'
        print(element,verboseResponse)

pathlist = Path('.').glob('**/*.md')
for path in pathlist:
    pathStrings = str(path)
    md_scraper(pathStrings)
