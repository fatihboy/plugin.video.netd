import sys
import urllib
import urllib2
import urlparse
import xbmcgui
import xbmcplugin
import xbmcaddon
import CommonFunctions
import HTMLParser

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

common = CommonFunctions
common.plugin = "netd-1.0"
 
xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)
	
def buildMainMenu():
    url = build_url({'mode': 'diziler', 'link': WEB_PAGE_BASE + '/diziler?q=&a=&d=&f=&t=&s=&c=&sort=IxName+asc&skip=0&take=9999'})
    li = xbmcgui.ListItem('Diziler', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'muzikler', 'link': WEB_PAGE_BASE + '/muzik'})
    li = xbmcgui.ListItem('Muzikler', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'programlar', 'link': WEB_PAGE_BASE + '/programlar'})
    li = xbmcgui.ListItem('Programlar', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'cocuk', 'link': WEB_PAGE_BASE + '/cocuk'})
    li = xbmcgui.ListItem('Cocuk', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'filmler', 'link': WEB_PAGE_BASE + '/filmler'})
    li = xbmcgui.ListItem('Filmler', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
	
    xbmcplugin.endOfDirectory(addon_handle)
	
def buildDizilerMenu():
    url = build_url({'mode': 'diziler-tum', 'link': WEB_PAGE_BASE + '/muzik'})
    li = xbmcgui.ListItem('Tum Diziler', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'diziler-nostalji', 'link': WEB_PAGE_BASE + '/programlar'})
    li = xbmcgui.ListItem('Nostalji', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'diziler-ozel', 'link': WEB_PAGE_BASE + '/cocuk'})
    li = xbmcgui.ListItem('Internete Ozel', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
	
    xbmcplugin.endOfDirectory(addon_handle)

def buildTumDizilerMenu():
   result = common.fetchPage({"link": WEB_PAGE_BASE + '/diziler?q=&a=&d=&f=&t=&s=&c=&sort=IxName+asc&skip=0&take=9999'})
   if result["status"] == 200:
		diziListesiLi = common.parseDOM(result["content"], "li", attrs = { "class": "span3" })
		htmlParser = HTMLParser.HTMLParser()

		
		for i in range(0, len(diziListesiLi)):			
			baslikDiv = common.parseDOM(diziListesiLi[i], "div", attrs = { "class": "caption" })[0]
			
			diziIsmi = htmlParser.unescape(common.parseDOM(baslikDiv, "a")[0])
			diziAciklama = htmlParser.unescape(common.parseDOM(baslikDiv, "p")[0])
			link = common.parseDOM(baslikDiv, "a", ret = "href")[0]
			afis = "http:" + common.parseDOM(diziListesiLi[i], "img", attrs = { "class": "lazy" }, ret = "data-original")[0]
			
			url = build_url({'mode': 'dizi', 'link': link})
			
			li = xbmcgui.ListItem(diziIsmi, iconImage=afis, thumbnailImage=afis)
			li.setArt({'poster': afis, 'tvshow.poster': afis, 'season.poster': afis})		
			li.setInfo(type="Video", infoLabels={"Label": diziIsmi, "Title": diziIsmi, "Plot": diziAciklama})			
			
			xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
		

   xbmcplugin.endOfDirectory(addon_handle)
   
def buildDizilerNostaljiMenu():
   result = common.fetchPage({"link": WEB_PAGE_BASE + '/diziler?g=Nostalji&q=&a=&d=&f=&t=&s=&c=&sort=IxName+asc&skip=0&take=9999'})
   if result["status"] == 200:
		diziListesiLi = common.parseDOM(result["content"], "li", attrs = { "class": "span3" })
		htmlParser = HTMLParser.HTMLParser()

		
		for i in range(0, len(diziListesiLi)):
			url = build_url({'mode': 'dizi'})
			
			baslikDiv = common.parseDOM(diziListesiLi[i], "div", attrs = { "class": "caption" })[0]
			
			diziIsmi = htmlParser.unescape(common.parseDOM(baslikDiv, "a")[0])
			diziAciklama = htmlParser.unescape(common.parseDOM(baslikDiv, "p")[0])			
			afis = "http:" + common.parseDOM(diziListesiLi[i], "img", attrs = { "class": "lazy" }, ret = "data-original")[0]
			
			li = xbmcgui.ListItem(diziIsmi, iconImage=afis, thumbnailImage=afis)
			li.setArt({'poster': afis, 'tvshow.poster': afis, 'season.poster': afis})		
			li.setInfo(type="Video", infoLabels={"Label": diziIsmi, "Title": diziIsmi, "Plot": diziAciklama})			
			
			xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
		

   xbmcplugin.endOfDirectory(addon_handle)
   

   
def buildDizilerOzelMenu():
   result = common.fetchPage({"link": WEB_PAGE_BASE + '/netd-ozel'})
   if result["status"] == 200:
		diziListesiUl = common.parseDOM(result["content"], "ul", attrs = { "class": "thumbnails", "data-skip": "0" })
		
		diziListesiLi = common.parseDOM(diziListesiUl, "li")
		htmlParser = HTMLParser.HTMLParser()

		
		for i in range(0, len(diziListesiLi)):
			url = build_url({'mode': 'dizi'})
			
			baslikDiv = common.parseDOM(diziListesiLi[i], "div", attrs = { "class": "caption" })[0]
			
			diziIsmi = htmlParser.unescape(common.parseDOM(baslikDiv, "a")[0])
			diziAciklama = htmlParser.unescape(common.parseDOM(baslikDiv, "p")[0])			
			afis = "http:" + common.parseDOM(diziListesiLi[i], "img", attrs = { "class": "lazy" }, ret = "data-original")[0]
			
			li = xbmcgui.ListItem(diziIsmi, iconImage=afis, thumbnailImage=afis)
			li.setArt({'poster': afis, 'tvshow.poster': afis, 'season.poster': afis})		
			li.setInfo(type="Video", infoLabels={"Label": diziIsmi, "Title": diziIsmi, "Plot": diziAciklama})			
			
			xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)
		

   xbmcplugin.endOfDirectory(addon_handle)

def buildDiziMenu():
    url = build_url({'mode': 'bolumler', 'link': args['link'][0]})
    li = xbmcgui.ListItem(u'B\u00f6l\u00fcmler', iconImage=xbmc.translatePath('special://home/addons/' + ADDON_ID +'/bolumler.png'))
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'fragmanlar', 'link': args['link'][0]})
    li = xbmcgui.ListItem('Fragmanlar', iconImage=xbmc.translatePath('special://home/addons/' + ADDON_ID +'/fragman.png'))
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'klipler', 'link': args['link'][0]})
    li = xbmcgui.ListItem('Klipler', iconImage=xbmc.translatePath('special://home/addons/' + ADDON_ID +'/klip.png'))
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)
	
def buildBolumlerMenu():
	skip=0
	
	while( parseBolumler(skip) ):
		skip = skip + 10
		
	xbmcplugin.endOfDirectory(addon_handle)
	
def parseBolumler(skip):
	result = common.fetchPage({"link": WEB_PAGE_BASE + '/actions/control/episodes?path=' + urllib.quote(args['link'][0], safe='') + '%2F&mediaType=CatchUp&view=Controls%2FPartial%2F_ThumbnailList&skip=' + str(skip)})
	if result["status"] == 200 and result["content"]:
		diziListesiLi = common.parseDOM(result["content"], "li", attrs = { "class": "span3" })
		htmlParser = HTMLParser.HTMLParser()

		
		for i in range(0, len(diziListesiLi)):			
			baslikDiv = common.parseDOM(diziListesiLi[i], "div", attrs = { "class": "caption" })[0]
			
			diziIsmi = htmlParser.unescape(common.parseDOM(baslikDiv, "a")[0])
			diziLink = htmlParser.unescape(common.parseDOM(baslikDiv, "a", ret = "href")[0])
			diziAciklama = htmlParser.unescape(common.parseDOM(baslikDiv, "p")[0])			
			afis = "http:" + common.parseDOM(diziListesiLi[i], "img", attrs = { "class": "lazy" }, ret = "data-original")[0]
			
			url = build_url({'mode': 'videoOynat', 'title': diziIsmi.encode('utf-8', 'ignore'), 'link': diziLink})
			
			li = xbmcgui.ListItem(diziIsmi, iconImage=afis, thumbnailImage=afis)
			li.setArt({'poster': afis, 'tvshow.poster': afis, 'season.poster': afis})		
			li.setInfo(type="Video", infoLabels={"Label": diziIsmi, "Title": diziIsmi, "Plot": diziAciklama})			
			
			xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

		return True
	else:
		return False


def buildKliplerMenu():
	skip=0
	
	while( parseKlipler(skip) ):
		skip = skip + 10
		
	xbmcplugin.endOfDirectory(addon_handle)
	
def parseKlipler(skip):
	result = common.fetchPage({"link": WEB_PAGE_BASE + '/actions/control/clips?path=' + urllib.quote(args['link'][0], safe='') + '%2Fkisa-klipler%2F&view=Controls%2FPartial%2F_ThumbnailList&sort=StartDate%20desc&skip=' + str(skip)})
	if result["status"] == 200 and result["content"]:
		diziListesiLi = common.parseDOM(result["content"], "li", attrs = { "class": "span3" })
		htmlParser = HTMLParser.HTMLParser()

		
		for i in range(0, len(diziListesiLi)):			
			baslikDiv = common.parseDOM(diziListesiLi[i], "div", attrs = { "class": "caption" })[0]
			
			diziIsmi = htmlParser.unescape(common.parseDOM(baslikDiv, "a")[0])
			diziLink = htmlParser.unescape(common.parseDOM(baslikDiv, "a", ret = "href")[0])
			diziAciklama = htmlParser.unescape(common.parseDOM(baslikDiv, "p")[0])			
			afis = "http:" + common.parseDOM(diziListesiLi[i], "img", attrs = { "class": "lazy" }, ret = "data-original")[0]
			
			url = build_url({'mode': 'videoOynat', 'title': diziIsmi.encode('utf-8', 'ignore'), 'link': diziLink})
			
			li = xbmcgui.ListItem(diziIsmi, iconImage=afis, thumbnailImage=afis)
			li.setArt({'poster': afis, 'tvshow.poster': afis, 'season.poster': afis})		
			li.setInfo(type="Video", infoLabels={"Label": diziIsmi, "Title": diziIsmi, "Plot": diziAciklama})			
			
			xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

		return True
	else:
		return False
		


def buildFragmanlarMenu():
	skip=0
	
	while( parseFragmanlar(skip) ):
		skip = skip + 10
		
	xbmcplugin.endOfDirectory(addon_handle)
	
def parseFragmanlar(skip):
	result = common.fetchPage({"link": WEB_PAGE_BASE + '/actions/control/clips?path=' + urllib.quote(args['link'][0], safe='') + '%2Ffragmanlar%2F&view=Controls%2FPartial%2F_ThumbnailList&sort=StartDate%20desc&skip=' + str(skip)})
	if result["status"] == 200 and result["content"]:
		diziListesiLi = common.parseDOM(result["content"], "li", attrs = { "class": "span3" })
		htmlParser = HTMLParser.HTMLParser()

		
		for i in range(0, len(diziListesiLi)):			
			baslikDiv = common.parseDOM(diziListesiLi[i], "div", attrs = { "class": "caption" })[0]
			
			diziIsmi = htmlParser.unescape(common.parseDOM(baslikDiv, "a")[0])
			diziLink = htmlParser.unescape(common.parseDOM(baslikDiv, "a", ret = "href")[0])
			diziAciklama = htmlParser.unescape(common.parseDOM(baslikDiv, "p")[0])			
			afis = "http:" + common.parseDOM(diziListesiLi[i], "img", attrs = { "class": "lazy" }, ret = "data-original")[0]
			
			url = build_url({'mode': 'videoOynat', 'title': diziIsmi.encode('utf-8', 'ignore'), 'link': diziLink})
			
			li = xbmcgui.ListItem(diziIsmi, iconImage=afis, thumbnailImage=afis)
			li.setArt({'poster': afis, 'tvshow.poster': afis, 'season.poster': afis})		
			li.setInfo(type="Video", infoLabels={"Label": diziIsmi, "Title": diziIsmi, "Plot": diziAciklama})			
			
			xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

		return True
	else:
		return False

def videoOynat():
	result = common.fetchPage({"link": WEB_PAGE_BASE + args['link'][0]})
	
	if result["status"] == 200:
		playlistUrl = 'http://37.48.66.141' + extract(result["content"], 'meta itemprop="contentURL" content="', '"') + '?key=0dc84dcb744f331d6e1bf06b6f895890&app=com.dcom'
		
		response = urllib2.urlopen(playlistUrl)
		if response and response.getcode() == 200:
			content = response.read()
			playlistUrlRoot = extract(playlistUrl, 'http://', 'index.m3u8')
			thumbnail = extract(result["content"], 'meta itemprop="thumbnailUrl" content="', '"')
									
			videoUrl = 'http://' + playlistUrlRoot + extract(content, '#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1250000\r\n', '\r')
			
			showError(ADDON_ID, 'Video : %s ' % (videoUrl))
			li = xbmcgui.ListItem(args['title'][0], iconImage=thumbnail, thumbnailImage=thumbnail, path=videoUrl)
			li.setProperty("IsPlayable", "true")
			li.setInfo(type='Video', infoLabels={ "Title": args['title'][0], "Label" : args['title'][0]})
			xbmc.Player().play(item=videoUrl, listitem=li)
		else:
			showError(ADDON_ID, 'Video %s adresinde bulunamadi' % (playlistUrl))

def extract(text, startText, endText):
    start = text.find(startText, 0)
    if start != -1:
        start = start + startText.__len__()
        end = text.find(endText, start + 1)
        if end != -1:
            return text[start:end]
    return None

def showError(addonId, errorMessage):
    notify(addonId, errorMessage)
    xbmc.log(errorMessage, xbmc.LOGERROR)

def notify(addonId, message, timeShown=5000):
    addon = xbmcaddon.Addon(addonId)
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (addon.getAddonInfo('name'), message, timeShown, addon.getAddonInfo('icon')))

	
WEB_PAGE_BASE = 'http://www.netd.com'
ADDON_ID = 'plugin.video.netd'

mode = args.get('mode', None)

if mode is None:
	buildMainMenu()
	
elif mode[0] == 'diziler':
	buildDizilerMenu()
	
elif mode[0] == 'diziler-tum':
	buildTumDizilerMenu()
	
elif mode[0] == 'diziler-nostalji':
	buildDizilerNostaljiMenu()
	
elif mode[0] == 'diziler-ozel':
	buildDizilerOzelMenu()	
	
elif mode[0] == 'dizi':
	buildDiziMenu()

elif mode[0] == 'bolumler':
	buildBolumlerMenu()

elif mode[0] == 'klipler':
	buildKliplerMenu()

elif mode[0] == 'fragmanlar':
	buildFragmanlarMenu()
	
elif mode[0] == 'videoOynat':
	videoOynat()