## syntax: python3 md_scraper.py
## This will scrape links from each md or json file it finds in
## all subdirectories and test them via the Requests package.

import requests
import re
from pathlib import Path

def findLinksMore(textOfFile):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', textOfFile)
    return url

def md_scraper(fileToWork):
    mdHandler = open(fileToWork)
    urlList = []
    errors = []
    for line in mdHandler:
        urlsFound = findLinksMore(line)
        if len(urlsFound) != 0:
            urlList.append(re.sub('[\>\)\"\'\?\[\]\*]','',str(urlsFound)))

    print('Scraping: ',fileToWork)

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
            errors.append({ 
                "url": element,
                "file": fileToWork,
                "code": md_response.status_code
            })
        #print(element,verboseResponse)
    
    return { 
        "errors": errors,
        "total_links": len(urlList)
    }

pathlist = Path('.').glob('**/*.md')
total_errors = []
total_links = 0
for path in pathlist:
    pathStrings = str(path)
    result = md_scraper(pathStrings)
    total_errors = total_errors + result["errors"]
    total_links = total_links + result["total_links"]

pathlist = Path('.').glob('**/*.json')
for path in pathlist:
    pathStrings = str(path)
    result = md_scraper(pathStrings)
    total_errors = total_errors + result["errors"]
    total_links = total_links + result["total_links"]
    
if len(total_errors) > 0:
    print(str(len(total_errors)) + " errors where found.")
    for error in total_errors:
        print(error["file"]+": "+str(error["code"])+ " -> " +error["url"])
    exit(1)
else:
    print("SUCCESS: No errors were found in "+ str(total_links) + " files")
    exit(0)