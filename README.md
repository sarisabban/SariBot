# SariBot
Tweets science articles, GIFs, infographic images, and videos

## DESCRIPTION:
This is a Twitter bot for myself which tweets science articles, GIFs, infographic images, and videos.

## HOW TO USE:
1. Install the tweepy and praw python 3 modules:

`sudo apt install python3-pip`

`sudo pip3 install twython praw`

Maybe in the future I will implement a different API: replace Tweepy with Twython: https://twython.readthedocs.io/en/latest/

2. Make sure you add the correct Twitter credentials in the Keys.py file.
3. Make sure you add the correct Reddit credentials in the Keys.py file.
4. Set time of day to start tweeting:

`crontab -e`

`00 19 * * * python3 Sari.py >> Sari_Log 2>&1`

## Generate Media Files
To get the links for videos, images, or GIFs from a website.

1. Run by using the following command:

`python3 Media.py [Web page] [Regular Expression of pages links] [Regular Expression of media link] [Filename to save output to]`

2. Output will be saved to the specified file. Name the output file as follows to direct the script to which media to tweet:
	* For videos filename should be: Videos
	* For GIFs filename should be: GIFs
	* For Inforgraphic images filename should be: Infographics
