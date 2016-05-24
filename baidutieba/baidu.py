#!/usr/bin/env python
#coding:utf-8

import urllib
import urllib2
import re
import tools

class BDTB:
	def __init__(self, baseUrl, seelZ, floorTag):
		self.baseURL = baseUrl
		self.seeLZ = '?see_lz'+str(seeLZ)
		self.tool = tools.Tool()
		self.file = None
		self.floor = 1
		self.defaultTitle = 'bdtb'
		self.floorTag = floorTag

	def getPage(self, pageNum):
		try:
			url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
			request = urllib2.Request(url)
			response = urllib2.urlopen(request)
			return response.read().decode("utf-8")
		except urllib2.URLError, e:
			if hasattr(e, "reason"):
				print u"connect error ", e.reason
				return none
	def getTitle(self, page):
		pattern = re.complie('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
		result = re.search(pattern, page)
		if result:
			return result.group(1).strip()
		else:
			return None

	def getPageNum(self, page):
		pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
		result = re.search(pattern, page)
		if result:
			return result.group(1).strip()
		else:
			return None

	def getContent(self, page):
		pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
		items = re.findAll(pattern, page)
		contents = []
		for item in items:
			content = "\n" + self.tool.replace(item) + "\n"
			contents.append(content.encode('utf-8'))
		return contents

	def setFileTitle(self, title):
		if title is not None:
			self.file = open(title + ".txt", "w+")
		else:
			self.file = open(self.defaultTitle + ".txt", "w+")

	def writeData(self, contents):
		for item in contents:
			if self.floorTag == '1':
				floorLine = "\n" + str(self.floor) + u"----------------------------------------------\n"
				self.file.write(floorLine)
			self.file.write(item)
			self.floor += 1

	def start(self):
		indexPage = self.getPage(1)
		pageNum = self.getPageNum(indexPage)
		title = self.getTitle(title)
		if pageNum == None:
			print "url is invalid, please try again"
			return
		try:
			print "in total: " + str(pageNum) + 'page'
			for i in range(1, int(pageNum + 1)):
				print "writting  " + str(i) + " page data "
				page = self.getPage(i)
				contents = self.getContent(page)
				self.writeData(contents)
		except IOError, e:
			print "writting error, reason: " + e.message
		finally:
			print "writting data finished"

if __name__ == '__main__':
	print u'please input id'
	baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
	seeLZ = raw_input("is allowed floorer talk, yes input 1 and no input 0\n")
	floorTag = raw_input("is allowed write floor info, yes input 1 and no input 0\n")
	bdtb = BDTB(baseURL, seeLZ, floorTag)
	bdtb.start()
