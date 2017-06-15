# SariBot
Tweets science articles, GIFs, infographic images, and videos



## DESCRIPTION:
This is a Twitter bot for myself which tweets science articles, GIFs, infographic images, and videos.



## HOW TO USE:
1. Install the tweepy and praw python 3 modules:

`sudo apt install python3-pip`

`sudo python3 -m pip install tweepy praw`

2. Setups to tweet an .mp4 video:
The Tweepy module cannot tweet .mp4 videos by default, it must be modified

	* Find the tweepy module location:
  
	`python3 -c 'import tweepy; print(tweepy.__file__)'`

	* cd to location

	* Remove default files and replace with modified files:
  
	`sudo rm api.py binder.py`
  
	`sudo wget https://raw.githubusercontent.com/fitnr/tweepy/c130d708c3bda84666c2a5eef69d276cdeb17e86/tweepy/api.py`
  
	`sudo wget https://raw.githubusercontent.com/fitnr/tweepy/c130d708c3bda84666c2a5eef69d276cdeb17e86/tweepy/binder.py`

Maybe in the future I will implement a different API: replace Tweepy with Twython: https://twython.readthedocs.io/en/latest/

3. Make sure you add the correct Twitter credentials in the Keys.py file.
4. Make sure you add the correct Reddit credentials in the Keys.py file.
5. Change the SleepTime in the Sari.py script to control when different tweets come out (default is 3600 or 1 hour between tweets).
6. Set time of day to start tweeting:
`crontab -e`
`00 15 * * * python3 Sari.py >> Twitter.log 2>&1`



## Generate Media Files
To get the links for videos, images, or GIFs from a website.

1. Run by using the following command:

`python3 Media.py [Web page] [Regular Expression of pages links] [Regular Expression of media link] [Filename to save output to]`

2. Output will be saved to the specified file. Name the output file as follows to direct the script to which media to tweet:
	* For videos filename should be: Videos
	* For GIFs filename should be: GIFs
	* For Inforgraphic images filename should be: Infographics
