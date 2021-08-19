from urllib.request import urlopen
import xml.etree.ElementTree as et

url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
root = et.fromstring(text)
for vid in root.findall('{http://www.w3.org/2005/Atom}entry'):
    print(vid.find('{http://www.w3.org/2005/Atom}title').text)
