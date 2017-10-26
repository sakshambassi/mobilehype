import tweepy
import pandas
import numpy as np
import re
from textblob import TextBlob

consumer_key = 'n3x6zuWtTufJqbXR3Z33tEkee'
consumer_secret = 'YqSAHpLsKNCBssttFgXBOoLqRteSZwekzLCj6vtwZ2vz1VXEbr'

access_token = '1424811614-jMFO115CUxnBcwuNHtzZznZhkb3m52Q2rZVeVUm'
access_token_secret = 'ZDChujaMv6eTZnDw0kKqL00fFD0DqKp9XSlp1p8jsJ4ZO'

rd = pandas.read_excel('mobiles.xlsx')
df = pandas.read_excel('hyperesult.xlsx')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

searches= ['upcoming smartphone','upcoming mobile','upcoming mobile phone','smartphone','mobile phone']
companies = np.unique(rd['Brand'].values)

for search in searches:
	print('\n\n')
	public_tweets = api.search(search,count=100)
	for tweet in public_tweets:
		print(tweet.text)
		analysis = TextBlob(tweet.text)
		print(analysis.sentiment)
		tweet.text=re.sub('[!@#$]', '',tweet.text)
		words = tweet.text.split()
		for word in words:
			i=0
			for company in companies:
				if word == company:
					print(word, company)
					df.loc[i, 'Hype Value'] += (1+analysis.sentiment.polarity)*0.01
				i=i+1

hypes = df['Hype Value'].values
i=0
for hype in hypes:
	if sum(hypes)==0:
		hype = 0
	else:
		hype = (hype/sum(hypes))*100
	df.loc[i,'Hype Percent'] = hype
	i=i+1

df.to_excel('hyperesult.xlsx',index=False)