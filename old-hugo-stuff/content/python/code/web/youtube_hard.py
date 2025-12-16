from urllib.request import urlopen
import re

# Most Popular
url = "http://www.youtube.com/playlist?list=PLrEnWoR732-BHrPp_Pm8_VleD68f9s14-"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
for title in re.findall(r'<a class="pl-video-title-link.+?">(.+?)</a>', text, re.S):
    print(title.strip())
