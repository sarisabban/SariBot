#!/usr/bin/python3

'''
## DESCRIPTION:
This is a Twitter bot for myself which search Reddit for science articles and Tweets them, it also tweets GIFs inforgraphics video from respective files. Seperate scripts are used to auto generate these files: GIFs (GetGIF.py) inforgraphics (MediaGET.py) videos from instagram (InstaVideoGET.py).

## HOW TO USE:
1. Make sure you add the correct Twitter credentials under "Twitter Credentials".
2. Make sure you add the correct Reddit credentials under "Reddit Credentials".
3. Set times of day to start tweeting.
4. Change the SleepTime to control when different tweets come out.
5. Make sure there is a file called Quotes and it is full of tweei lines.
6. Under the bottom while loop you can change the information sources (websites) in the relevent positions.
7. Run with Python 3.
8. Instagram parsing takes a very long time, but only happens once.

## Tweeting A .mp4 Video:
find the tweepy module location: python3 -c 'import tweepy; print(tweepy.__file__)'
delete the api.py and binder.py scripts
wget in their place these modified scripts:
https://raw.githubusercontent.com/fitnr/tweepy/c130d708c3bda84666c2a5eef69d276cdeb17e86/tweepy/api.py
https://raw.githubusercontent.com/fitnr/tweepy/c130d708c3bda84666c2a5eef69d276cdeb17e86/tweepy/binder.py
use the following command to tweet an mp4 video:
media = api.upload_chunked('1.mp4')
api.update_status(status="Hello World!", media_ids=[media.media_id])
As A Backup (a different API): Replace Tweepy with Twython: https://twython.readthedocs.io/en/latest/
'''
#Imports		   These modules need to be downloaded --->  #       #
import time , datetime , urllib.request , requests , random , os , tweepy , praw

#Twitter:
consumer_key		= ''
consumer_secret		= ''
access_token		= ''
access_token_secret	= ''

#Reddit:
bot_id			= ''
secret			= ''

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
Article = Reddit('science' , 20) ; Tweet(Article[0] , Article[1] , '#علوم') ; time.sleep(SleepTime)

#2. GIFs:
#TweetMedia('Sari_GIFs' , '.gif' , '#علوم') ; time.sleep(SleepTime)

#3. Infographics:
#TweetMedia('Sari_Infographics' , '.jpg' , '#علوم') ; time.sleep(SleepTime)

#4. Videos:
TweetMedia('Sari_Videos' , '.mp4' , '#علوم')
print(Blue + '---------------------------------------------------------' + Cancel)
