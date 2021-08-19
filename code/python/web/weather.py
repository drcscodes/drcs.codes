import urllib.request, re

# 2994160 is the city code for Metz, FR
request = urllib.request.Request("http://www.openweathermap.com/city/2994160")
response = urllib.request.urlopen(request)
page_bytes = response.read()
page_text = page_bytes.decode()

# Get the current wind using a regular expression
wind = re.findall(r'<td>Wind</td><td>(.+?)</td>', page_text.replace("\n",""))[0]
print(wind)

# Get the current wind using BeautifulSoup
import bs4
soup = bs4.BeautifulSoup(page_text, 'html.parser')
wind = soup.body.find('div', attrs={'class': 'weather-widget'})\
                .find('tbody')\
                .find('tr')\
                .find_all('td')[1].text
print(wind)

# Get the current wind using web service API
