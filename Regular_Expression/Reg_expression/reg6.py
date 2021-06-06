import re,urllib
import urllib.request

sites = ['http://google.com','http://rediff.com']

for site in sites:
    print("searching sites",site)
    u = urllib.request.urlopen(site)
    txt = u.read()
    title = re.findall("<title>.*</title>",str(txt),re.I)
    print(title[0])