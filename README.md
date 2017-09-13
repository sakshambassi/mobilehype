# mobilehype
Calculates hype percentage of different mobile brands based on polarity of tweets

brandscrape.py scrapes smartphone brands and put them into excel file and mobilehype.py calculates hype percent and appends to excel file.  

brandsrcape.py uses libraries like 
1. BeautifulSoup: to scrape data(names of smartphone makers) from the url given
2. urllib: to open URL 
3. pandas: to read and write to excel
and mobilehype.py uses libraries like
1. tweepy: to fetch tweets(data)
2. RegularExpressions: to ignore some characters from
3. TextBlob: for sentiment analysis of tweet text
4. pandas: to read and write to excel
