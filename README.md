# mobilehype
Calculates hype percentage of different mobile brands based on polarity of tweets

brandscrape.py scrapes smartphone brands and put them into excel file and mobilehype.py calculates hype percent and appends to excel file.  
Both files uses Python3 version

brandsrcape.py uses libraries like 
- BeautifulSoup: to scrape data(names of smartphone makers) from the url given
- urllib: to open URL 
- pandas: to read and write to excel

and mobilehype.py uses libraries like
- tweepy: to fetch tweets(data)
- RegularExpressions: to ignore some characters from
- TextBlob: for sentiment analysis of tweet text
- pandas: to read and write to excel