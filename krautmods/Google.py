import os, urllib3, urlparse3
from bs4 import BeautifulSoup

class Google:

	gURL = "http://google.com/search?q="

	def __init__(self,query):
		super(Google, self).__init__()
		http = urllib3.PoolManager()
		if(isinstance(query, list)):
			query = self.LstToQuery(query)
		elif(isinstance(query, str)):
			query = self.StrToQuery(query)
		req = http.request('GET', self.gURL+query)
		soup = BeautifulSoup(str(req.data))
		data = ""
		for a in soup.select(".r a"):
			data += str(a)
		sp = BeautifulSoup(str(data))
		self.dumpToFile(sp.prettify().encode("iso-8859-1"))
	def LstToQuery(self, lst):
		buff = ""
		for entry in lst:
			buff += str(entry)+"+"
		return buff[0:-1]
	def StrToQuery(self, string):
		buff = ""
		for entry in string.split(" "):
			buff += str(entry)+"+"
		return buff[0:-1]

	def dumpToFile(self, data):
		fo = open("dumpFile.html", "wb")
		fo.write(data)
		fo.close

g = Google("Dayvi Schuster")