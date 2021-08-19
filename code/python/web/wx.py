import urllib.request, re
import requests, json

def get_page_text(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    page_bytes = response.read()
    page_text = page_bytes.decode()
    return page_text

def get_wind_regex(page_text):
    """Get the current wind using a regular expression"""
    wind = re.findall(r'<td>Wind</td><td id="weather-widget-wind">(.+?)</td>',
                      page_text, re.S)[0]
    return wind

def get_wind_bs4(page_text):
    """Get the current wind using BeautifulSoup"""

    import bs4
    soup = bs4.BeautifulSoup(page_text, 'html.parser')
    wind = soup.body.find('div', attrs={'class': 'weather-widget'})\
                    .find('tbody')\
                    .find('tr')\
                    .find_all('td')[1].text
    return wind

def get_wind_web_service():
    """Get the current wind using web service API"""
    # Also note use of requests library, generally better than urllib
    weather_api = 'http://api.openweathermap.org/data/2.5/weather'
    resp = requests.get(weather_api,
                        params={'zip': '57000,FR',
                                'appid': 'a651281e59ca31678a3c3407b8530bf5'})
    #print(resp)
    json_data = resp.json()
    #print(json_data)
    return json_data['wind']

def main(args):
    # 2994160 is the city code for Metz, FR
    wx_page_text = get_page_text("http://www.openweathermap.com/city/2994160")
    #print("Wind using regex: {}".format(get_wind_regex(wx_page_text)))
    print("Wind using BS4: {}".format(get_wind_bs4(wx_page_text)))
    print("Wind using web service: {}".format(get_wind_web_service()))

if __name__=='__main__':
    import sys
    main(sys.argv)
