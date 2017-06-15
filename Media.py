#!/usr/bin/python3
					   #<-- Download Module
import urllib.request , re , time , sys , bs4

def GetPages(TheURL , RegularExpression):
	'''Finds all spesific URLs in a page, returns a list of URLs'''
	ListOfPages = list()
	page = urllib.request.urlopen(TheURL)
	data = bs4.BeautifulSoup(page , 'html5lib')
	for link in data.find_all('a'):
		PageLinks = link.get('href')
		if re.search(RegularExpression , str(PageLinks)):
			ListOfPages.append(PageLinks)
		else:
			continue
	return(ListOfPages)

def GetMedia(Page , RegularExpression):
	'''Finds the media URL and title in a page, returns a tuple with the first position as the title and the second position as the link'''
	page = urllib.request.urlopen(Page)
	data = bs4.BeautifulSoup(page , 'html5lib')
	Title = data.find('title')
	for link in data:
		TheLink = re.findall(RegularExpression , str(link))
		if TheLink == []:
			continue
		else:
			return(Title.text , TheLink[0])
#----------------------------------------------------------------------------------------------------------------------------------
Pages = GetPages(sys.argv[1] , sys.argv[2])
for page in Pages:
	OutPut = GetMedia(page , sys.argv[3])
	Title = OutPut[0] #<-- Optional: Adds a text string before each URL (can be used with a twitter bot to tweet the string as title and the link as the media)
	print(Title)
	URLs = OutPut[1]
	print(URLs)
	TheFile = open(sys.argv[4] , 'a')
	TheFile.write(Title + '\n') #<-- Optional: Adds a text string before each URL (can be used with a twitter bot to tweet the string as title and the link as the media)
	TheFile.write(URLs + '\n')
	TheFile.close()
