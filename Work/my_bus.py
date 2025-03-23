import urllib.request
from xml.etree.ElementTree import parse

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')

print(u.__dict__)
doc = parse(u)

for pt in doc.findall(".//pt"):
    print(pt.text)