#coding:utf8
'''
下载网站的图片

1 把网页的源代码拿过来
2 把图片的地址过滤出来
3 用下载工具下载下来
'''

import urllib, re

def getHtml(url):
	'''
	read 整个网页的源代码
	'''
	page = urllib.urlopen(url)
	html = page.read()
	page.close()
	return html

def getImg(html):
	'''
	找出图片的地址并下载
	'''
	reg = r' src="(.*?.jpg)" width'   # .*?. 0个以上的任意符号
	imgre = re.compile(reg)
	imgList = imgre.findall(html)
	i = 0
	for imgurl in imgList:
		print imgurl
		urllib.urlretrieve(imgurl, "$d.jpg"%(i,))
		i += 1

ht = getHtml(r"")
print ht 
print "############################"
print getImg(ht)

