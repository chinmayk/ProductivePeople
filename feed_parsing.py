#!/usr/bin/python
from BeautifulSoup import BeautifulSoup
import urllib2
import csv

class ProductivityParser:
	"""A feed parser for the Usesthis website. Dumps things people use to a repository."""
		
	def getFeed(self):
		self.feedText = urllib2.urlopen("http://usesthis.com/feed/")
		self.soup = BeautifulSoup(self.feedText)
	
	
	def getLinks(self):
		array_of_links = [];
		print "Trying to print links"
		with open("cool_objects.csv", 'w') as f:
			csvWriter = csv.writer(f)
			for entry in self.soup('entry'):
				person = (entry('title')[0].text)
				for link in entry('a'):
					link_text = (link.text)
					link_href = (link['href'])
					if link.has_key('title'):
						link_description = (link['title'].encode('utf-8'))
					else:
						link_description = 'NA'
					try:
						#print "'%s', '%s', '%s', '%s'" % (person, link_text, link_description, link_href)
						csvWriter.writerow([person, link_text, link_description, link_href])
					except Exception as e:
						print "'%s', '%s', '%s', '%s'" % ("Exception", "Exception", "Exception", link_href)
			

if __name__ == "__main__":
	parser = ProductivityParser()
	parser.getFeed()
	parser.getLinks()



