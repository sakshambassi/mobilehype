import bs4
import urllib
import pandas
from pandas import DataFrame

url = "https://www.gsmarena.com/makers.php3"
htmlfile = urllib.request.urlopen(url)
l = ['ID', 'Company Name']
i=0
df = pandas.DataFrame(columns=l)
soup = bs4.BeautifulSoup(htmlfile, "html.parser")
div=soup.find('div',class_="st-text")
for company in div.find_all('td'):
	i = i + 1
	df.loc[i,'ID']=i
	df.loc[i,'Company Name'] = company.find_next('a').contents[0]
	# if company.get_text() == "Vertu":
	# 	break

df.to_excel('mobiles3.xlsx',index=False)