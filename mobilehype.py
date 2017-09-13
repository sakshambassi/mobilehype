import tweepy
import pandas
import re
from textblob import TextBlob

consumer_key = 'n3x6zuWtTufJqbXR3Z33tEkee'
consumer_secret = 'YqSAHpLsKNCBssttFgXBOoLqRteSZwekzLCj6vtwZ2vz1VXEbr'

access_token = '1424811614-jMFO115CUxnBcwuNHtzZznZhkb3m52Q2rZVeVUm'
access_token_secret = 'ZDChujaMv6eTZnDw0kKqL00fFD0DqKp9XSlp1p8jsJ4ZO'

rd = pandas.read_excel('mobiles.xlsx')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

searches= ['upcoming smartphone','upcoming mobile','upcoming mobile phone','smartphone','mobile phone']
companies = rd['Company Name'].values
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
					rd.loc[i, 'Hype Value'] += (1+analysis.sentiment.polarity)*0.01
				i=i+1

i=0
hypes = rd['Hype Value'].values
for hype in hypes:
	hype = (hype/sum(hypes))*100
	rd.loc[i,'Hype Percent'] = hype
	i=i+1

rd.to_excel('mobiles.xlsx',index=False)