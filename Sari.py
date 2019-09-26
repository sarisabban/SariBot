#!/usr/bin/python3

import os
import time
import praw
import random
import twython
import datetime
import requests
import urllib.request

#Twitter
key          = 'HyqyCA19leggETcAwMkNaCaUI'
secrets      = 'GN5MIC2cjHjdsKjo9RzWrOj7H1bxWzkW2X26QvrD2bdL6Aqr1p'
token        = '288988915-9UiDRFhSS7PXt30eR7wj8cjVKeNNbR3lzp2i14D0'
token_secret = 'FujeYfKLLqlcYk2XrNDyKJjvRQ6p7cSHNlpAkFuAmHHgc'

#Reddit
bot_id       = 'qGw_Fmua6S--BA'
secret       = 'UkDKfAsGRGmnDbuHh2zjOKZdYr4'

def Reddit(Topic, NumberOfTopics):
	''' Get a random article's URL and title from Reddit '''
	for attempt in range(10):
		try:
			connect = praw.Reddit(client_id=bot_id,
								client_secret=secret,
								user_agent='Science News Bot')
			reddit = connect.subreddit(Topic).hot(limit=NumberOfTopics)
			Alist = []
			for submission in reddit: Alist.append(submission)
			random.shuffle(Alist)
			title = Alist[0].title
			url = Alist[0].url
			return(title, url)
			break
		except Exception as TheError:
			print('\x1b[31m[-] ERROR: {}\x1b[0m'.format(Exception))
			continue

def Tweet(Text, URL, Hashtag):
	''' Tweets '''
	api = twython.Twython(key, secrets, token, token_secret)
	try:
		dateSTR = datetime.datetime.now().strftime('%d/%b/%Y %H:%M')
		TheTweet = '{}\n{}\n{}'.format(Text[:100], Hashtag, URL)
		api.update_status(status=TheTweet)
		print('\x1b[32m[+] Tweeted @ {}\x1b[0m'.format(dateSTR))
	except Exception as TheError:
		print('\x1b[31m[-] ERROR: {}\x1b[0m'.format(Exception))

def main():
	try:
		info = Reddit('science', 20)
		Tweet(info[0], info[1], '#Science')
	except Exception as TheError:
		print('\x1b[31m[-] ERROR: Did not tweet\x1b[0m')

if __name__ == '__main__': main()
