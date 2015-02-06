#!/usr/bin/env python
#coding:utf8

import time

hero = raw_input('please input your name: ')
#if hero == "":
#    hero = "player1"
#    print "use default name player1"

while hero == "" or hero == "123":
	hero = raw_input('please input your name: ')
	if hero == "123":
		print 'hello!!!!!!!!'
		continue
		print 'after'
else:
	print "use name: %s" % hero

time.sleep(1)
print "hi %s, welcome to hero game" % hero   # %s is formatting strings
time.sleep(1)
print "room1 blood -10"
