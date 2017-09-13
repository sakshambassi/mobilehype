import bs4
import urllib
import pandas
from pandas import DataFrame

url = "https://en.wikipedia.org/wiki/List_of_mobile_phone_makers_by_country"
htmlfile = urllib.request.urlopen(url)
l = ['ID', 'Company Name']
i=0
df = pandas.DataFrame(columns=l)
soup = bs4.BeautifulSoup(htmlfile, "html.parser")
for company in soup.find_all('a'):
	if company.get_text() == "":
		continue
	i = i + 1
	if i < 4:
		continue
	df.loc[i,'ID'] = int(i-3)
	df.loc[i,'Company Name'] = company.get_text()
	if company.get_text() == "Vertu":
		break

df.to_excel('mobiles3.xlsx',index=False)