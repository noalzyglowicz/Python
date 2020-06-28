import urllib.request
import re
base_url = '''https://forecast.weather.gov/zipcity.php?inputstring='''

location = input("what location's weather? ")

url = base_url + location

page = urllib.request.urlopen(url)
text = page.read().decode('utf-8')

wind_speed = re.compile(r'''.*<b>Wind Speed</b></td>[^<]*<td>(.+) ([0-9]+) mph</td>''')

for m in wind_speed.finditer(text):
    print(m.groups())