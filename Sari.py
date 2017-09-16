#!/usr/bin/python3
			    #       #	<---These modules need to be downloaded
import time , datetime , tweepy , praw , urllib.request , requests , random , os

#Twitter And Reddit Credentials Are Found in the File Keys.py
from Keys import *

#Sleep Time (in seconds) Between Tweets:
SleepTime = 3600

#Terminal Text Colours:
Black 	= '\x1b[30m'
Red	= '\x1b[31m'
Green	= '\x1b[32m'
Yellow	= '\x1b[33m'
Blue	= '\x1b[34m'
Purple	= '\x1b[35m'
Cyan	= '\x1b[36m'
White	= '\x1b[37m'
Cancel	= '\x1b[0m'

#Logo Print
print(Green + '███████╗ █████╗ ██████╗ ██╗\n██╔════╝██╔══██╗██╔══██╗██║\n███████╗███████║██████╔╝██║\n╚════██║██╔══██║██╔══██╗██║' + Purple + '╔╦╗┬ ┬┬┌┬┐┌┬┐┌─┐┬─┐  ╔╗ ┌─┐┌┬┐\n' + Green + '███████║██║  ██║██║  ██║██║' + Purple + ' ║ ││││ │  │ ├┤ ├┬┘  ╠╩╗│ │ │ \n' + Green + '╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝' + Purple + ' ╩ └┴┘┴ ┴  ┴ └─┘┴└─  ╚═╝└─┘ ┴ ' + Cancel)
print(Blue + '---------------------------------------------------------' + Cancel)

#Connect to Twitter using the credentials:
auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)
api = tweepy.API(auth)
print(Yellow + '[+] Connected To Twitter' + Cancel)
#-------------------------------------------------------------------------------------------------------------------------------
def Reddit(Topic , NumberOfTopics):
	'''Uses the Reddit API (praw) to parse Reddit, goes to the spesified topic's page, get the top spesified number of articles and then gives back a random article's URL link and its title. Returns a tuple.'''
	while True:
		try:
			reddit = praw.Reddit(client_id=bot_id,client_secret=secret,user_agent='Science News Bot')
			Alist = list()
			for submission in reddit.subreddit(Topic).hot(limit=NumberOfTopics):
				Alist.append(submission)
			random.shuffle(Alist)
			title = Alist[0].title
			url = Alist[0].url
			return(title , url)
			break
		except Exception as TheError:
			print(Red + '[-] ERROR: Did not parse Reddit')
			print(TheError)
			print(Cancel)
			continue



def Tweet(Text , URL , Hashtag):
	'''Takes a text, a URL, and a hashtag and tweets it, then prints are tweet in the terminal. Does not return anything, only tweets and prints a confirmation in the terminal.'''
	try:
		dateSTR = datetime.datetime.now().strftime('%H:%M')
		TheTweet = Text[:100] + '\n' + Hashtag + '\n' + URL
		api.update_status(TheTweet)
		print(Blue + '[+] Tweet at ' + dateSTR + Cancel + '\n' + TheTweet + '\n')
	except Exception as TheError:
		print(Red + '[-] ERROR: Did not tweet')
		print(TheError)
		print(Cancel)



def TweetMedia(TheFile , Extention , Hashtag):
	'''Takes saved media urls (.mp4 or .jpg or .gif) from a text file and their titles, downloads the media and tweets them then deletes the link and the title for the file. Does not return anything, only tweets and prints a confirmation in the terminal.'''
	while True:
		try:
			dateSTR = datetime.datetime.now().strftime('%H:%M')

			#Getting The Tweet Title: 
			info = open(TheFile , 'r').read().splitlines(True)
			Title = info[0].strip('\n')
			open(TheFile , 'w').writelines(info[1:])

			#Downloading The Media:
			data = open(TheFile , 'r').read().splitlines(True)
			Media = data[0].strip('\n')
			open(TheFile , 'w').writelines(data[1:])
			media = open('MEDIA' + Extention , 'wb')
			media.write(requests.get(Media).content)
			statinfo = os.stat('MEDIA' + Extention)
			media.close()

			#Tweeting and Removing The Media File:
			TheTweet = Title[:100] + '\n' + Hashtag + '\n' + Media
			mediavid = api.upload_chunked('MEDIA' + Extention)
			api.update_status(status = TheTweet , media_ids=[mediavid.media_id])
			os.remove('MEDIA' + Extention)
			print(Blue + '[+] Tweet at ' + dateSTR + Cancel + '\n' + TheTweet + '\n')
			break
		except Exception as TheError:
			print(Red + '[-] ERROR: Did not tweet video')
			print(TheError)
			print(Cancel)
			continue
#-------------------------------------------------------------------------------------------------------------------------------
print(Yellow + '[+] Date:' , datetime.datetime.now().strftime('%d %B %Y @ %H:%M') + Cancel)

#1. Science Articles:
Article = Reddit('science' , 20)
Tweet(Article[0] , Article[1] , '#علوم')
time.sleep(SleepTime)

#2. GIFs:
TweetMedia('GIFs' , '.gif' , '#علوم')
time.sleep(SleepTime)

#3. Image:
TweetMedia('Infographics' , '.jpg' , '#علوم')
time.sleep(SleepTime)

#4. Videos:
TweetMedia('Videos' , '.mp4' , '#علوم')
print(Blue + '---------------------------------------------------------' + Cancel)
