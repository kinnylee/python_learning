#!usr/bin/python

import urllib
import urllib2
import re

class Spider(object):
	"""docstring for Spider"""
	def __init__(self):
		super(Spider, self).__init__()
		self.siteUrl = 'http://mm.taobao.com/json/request_top_list.htm'

	def getPage(self, pageIndex):
		url = self.siteUrl + "?page=" + str(pageIndex)
		print url
		request = urllib2.Request()
		response = urllib2.urlopen(request)
		return response.read().decode("gbk")

	def getContent(self, pageIndex):
		page = self.getPage(pageIndex)
		pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
		items = re.findall(pattern, page)
		for item in items:
			print item[0], item[1], item[2], item[3], item[4]

	def saveToFile(self, filename, contents):
		f = open(filename, 'wb')
		f.write(contents)
		f.close

spider = Spider()
html = spider.getContent(1)
spider.saveToFile('save.html', html)
print html
