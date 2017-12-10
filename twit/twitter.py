#!/usr/bin/env python
# python 2.7.12
from HTMLParser import HTMLParser
from httplib import HTTPSConnection
from datetime import datetime
from sys import argv

class TweetParser(HTMLParser):
	# parse html stuff
	tweet_list = []	# (time,tweet,creator)
	index = 0
	is_time = False
	is_data = False
	is_creator = False
	creator = ""
	
	def handle_starttag(self,tag,attrs):
		# handle
		if tag=='p':
			for (a,b) in attrs:
				if a=='class' and b.find("tweet-text") != -1:
					self.is_data = True
		if tag=='span':
			for (a,b) in attrs:
				if a=='data-time':
					self.tweet_list.append([int(b),"",""])
		if tag=='b':
			for (a,b) in attrs:
				if a=='class' and b=='u-linkComplex-target':
					self.is_creator = True
	
	def handle_endtag(self,tag):
		if tag == 'p' and self.is_data:
			self.is_data = False
			self.index+=1
	
	def handle_data(self,data):
		if self.is_data:
			# add to list
			self.tweet_list[self.index][1] += data
			self.tweet_list[self.index][2] = (self.creator+'.')[:-1]
		if self.is_creator:
			self.creator = '@'+data
			self.is_creator = False


def int_to_time(time):
	date = datetime.fromtimestamp(time * 1000 / 1e3)
	ret = "%d-%d-%d %d:%d" % (date.year,date.month,date.day,date.hour,date.minute)
	return ret

def main(path):
	subf = open(path)
	subs = subf.readlines()
	subf.close()
	conn = HTTPSConnection("twitter.com")
	parser = TweetParser()
	for sub in subs:
		if sub=='':
			break
		sub = sub[:-1]
		conn.request("GET","/"+sub)
		resp = conn.getresponse()
		if resp.status != 200:
			print resp.reason
			continue
		buf1 = resp.read()
		buf2 = buf1.decode("UTF-8")
		parser.feed(buf2)
	tweets = parser.tweet_list
	
# order tweets by time
	while len(tweets) > 0:
		m = 10000000000
		i = 0
		for j in range(len(tweets)):
			if tweets[j][0] < m:
				m = tweets[j][0]
				i = j
		(t,d,c) = tweets.pop(i)
		print c,int_to_time(t)
		print d
		print "----------------------"


if __name__=='__main__':
	if len(argv) != 2:
		print "Usage: " + argv[0] + " <subs file>"
	else:
		main(argv[1])

