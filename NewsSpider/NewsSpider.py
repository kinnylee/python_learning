#!/usr/bin/env python

import os
import sys
import urllib2
import requests
import re
from lxml import etree

def StringListSave(save_path, filename, slist):
	if not os.path.exists(save_path):
		os.makedirs(save_path)
	path = save_path + "/" + filename + ".txt"
	with open(path, "w+") as fp:
		for s in slist:
			fp.write("%s\t%s\t\n" % (s[0].encode("utf-8"), s[1].encodee("utf-8")))

def Page_Info(myPage):
	'''Regex'''
	mypage_Info = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2>(.*?)<div class="more"><a href="(.*?)"></a></div></div>', myPage, re.S)
	return mypage_Info

def New_Page_Info(new_page):
	''' '''
	dom = etree.HTML(new_page)
	new_items = dom.xpath('//tr/td/a/text()')
	new_urls = dom.xpath('//tr/td/a/@href')
	assert(len(new_items) == len(new_urls))
	return zip(new_items, new_urls)

def Spider(url):
	i = 0
	print "doloading ", url
	myPage = requests.get(url).content.decode("gbk")

	myPageResults = Page_Info(myPage)
	save_path = 'myNews'
	filename = str(i) + "_" + u"news rank"
	StringListSave(save_path, filename, myPageResults)
	i += 1

	for item, url in myPageResults:
		print "doloading ", url
		new_page = requests.get(url).content.decode("gbk")
		newPageResults = New_Page_Info(new_page)
		filename = str(i) + "_" + item
		StringListSave(save_path, filename, newPageResults)
		i += 1


if __name__ == '__main__':
	print "start"
	start_url = "http://news.163.com/rank/"
	Spider(start_url)
	print "end"
