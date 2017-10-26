import bs4
import urllib
import pandas
from pandas import DataFrame

url = "https://www.gsmarena.com/makers.php3"
htmlfile = urllib.request.urlopen(url)
l = ['ID', 'Brand','Phone']
i=0
df = pandas.DataFrame(columns=l)
soup = bs4.BeautifulSoup(htmlfile, "html.parser")
prefix = 'https://www.gsmarena.com/'
div=soup.find('div',class_="st-text")
for brand in div.find_all('td'):
	url2 = brand.find_next('a')['href']
	url2 = prefix+url2
	html2 = urllib.request.urlopen(url2)
	soup2 = bs4.BeautifulSoup(html2, "html.parser")
	div2=soup2.find('div',class_="makers")
	for phone in div2.find_all('span'):
		i = i + 1
		df.loc[i,'ID']=i
		df.loc[i,'Brand'] = brand.find_next('a').contents[0]
		df.loc[i,'Phone'] = phone.contents[0]

df.to_excel('mobiles.xlsx',index=False)