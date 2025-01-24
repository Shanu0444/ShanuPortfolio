import requests
import bs4

res = requests.get('https://32a848cd-a4bd-4b5c-a521-19023513bb87-00-57oar4dzfoeg.picard.repl.co/')

#print(res.raise_for_status())

parseSoup = bs4.BeautifulSoup(res.text,'html.parser')

elements= parseSoup.select('p')
print(elements)

