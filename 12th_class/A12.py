# Open a webpage using the urllib library.

import urllib.request as req

url = "https://www.google.com"
with req.urlopen(url) as response:
    html = response.read()
print(html)

## Uncomment Below Code to save the reponse html in to a html file

# file = open("index.html","w+")
# file.write(str(html))