import requests as rq
from sys import argv
import re
from os import listdir

def correctURL(url):
	url = url.replace("https://","http://")
	if "http://" not in url:
	        url = "http://" + url
	return url.replace("///","//")

def expandURL(url, og):
	pass

def log(text):
	print(text)

URLVALIDATOR = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

LOCATORS = { 
"superhry.cz":"www.*\.swf",
"newgrounds.com":"https://uploads.ungrounded.net/.*\.swf",
"kongregate.com":"https://www.kongregate.com/flash/.*\.swf"
"y8.com":"https://img-hws.y8.com/cloud/y8-flash-game/.*\.swf"
}

# EXTENSION LOCATORS LOADING
for filename in listdir():
	if filename[-8:] == ".locator":
		with open(filename, "r") as f:
			content = f.read()
		for line in content.replace(" ","").split("\n")[:-1]:
			LOCATORS[line.split(":")[0]] = line.split(":")[1]
		log("Loaded extension: {}".format(filename))

# COLLECTING

original_page = correctURL(input("Enter superhry link:"))

log("Connecting to server...")
html = rq.get(original_page).text

# SFW SEARCHING
log("Loading .swf link..")

selected_locator = None
for locator in LOCATORS:
	if locator in original_page:
		selected_locator = LOCATORS[locator]

if selected_locator is None:
	raise BaseException("Could not find site locator. Try installing an extension.")

link = correctURL(re.findall(selected_locator, html)[0])
log("Loaded link: {}".format(link))

# SAVING
log("Opening target file...")
with open("game{}".format(link[-12:]).replace("/","_"), "wb") as f:
	log("Writing...")
	f.write(rq.get(link).content)
log("Done!")
