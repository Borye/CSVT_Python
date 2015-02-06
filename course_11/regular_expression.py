#coding:utf8
import re, urllib
'''
正则表达式（re）

1 可以为想要匹配的相应字符串集制定规则
2 该字符串可能包含英文语句，email地址，命令或任何想搞定的东西
3 可以问诸如“这个字符串匹配该模式吗？”
4 “在这个字符串中是否有部分匹配该模式呢？”
5 你也可以使用RE以各种方式来修改或分割字符串

正则表达式语句相对小型和受限
并非所有字符串处理都能用正则表达式完成
'''

reg_test = "abc"

s = "abc hello abc"

print re.findall(reg_test, s)

# compile re

abcRe = re.compile('abc')
print abcRe.findall(s)


'''
元字符
. ^ $ * + ? [] \ | ()
'''
# . 代表任意字符
# find t + random + p 

ss = "tip top tgp aaa ggg ttt toop"   # toop will not be find
print re.findall('t.p', ss)

# ^ $ 表示以什么开头 以什么结尾

print re.findall('^tip', ss)
print re.findall('op$', ss)

# [] 放中间需要匹配的元素

ss1 = "waw wbw wcw wxw wyw wzw"
print re.findall('w.w', ss1)
print re.findall('w[abc]w', ss1)
print re.findall('w[a-z]w', ss1)
print re.findall('w[a-z123]w', ss1)

# {} 规则重复

tel1 = '12345678'
tel2 = '678'

rTel = re.compile('[0-9]{8}')   # {}means multiply 8 times

print rTel.findall(tel1)
print rTel.findall(tel2)

# , 或者

rTel = re.compile('[0-9]{3,4}[0-9]{8}')  # , means multiply 3 - 4 times
print rTel.findall('01012345678')
print rTel.findall('075512345678')

print rTel.findall('0755123456789')   # problem is when the value is more, it still output first several numbers

rTel = re.compile('^[0-9]{3,4}[0-9]{8}$')
print rTel.findall('0755123456789')

# ? 中间有可有可无的

rTel = re.compile('^[0-9]{3,4}-?[0-9]{8}$')

print rTel.findall('075512345678')
print rTel.findall('0755-12345678')

# 重复0次以上 * 重复1次以上 +

# \ 如果符号里有元字符，则前面加上\可以使其变为普通符号
# \d represent 0-9
# \D 匹配非数字字符
# \s 匹配任何空白字符    [ \t\n\r\t\v]
# \S 匹配任何非空白字符
# \w 匹配任何字母数字字符  【a-zA-Z0-0_】
# \W 匹配任何非字母数字字符 【^a-zA-Z0-0_】 集合内部^表示除了。。。

rTel = re.compile('^\d{3,4}-?\d{8}$')

print rTel.findall('075512345678')

# 定义正则表达式 前面加一个r
# 表示反斜杠不会被任何特殊方式处理

rTel = re.compile(r'^\d{3,4}-?\d{8}$') # add r in front

print rTel.findall('075512345678')

# match, find from the front 

t = r'hello'

s = "hello world"
s2 = "world hello"

print re.match(t, s)
o = re.match(t, s)
print o.group()
print re.match(t, s2)

# search

print re.search(t, s2)

# don't care 大小写
# re.I

s = 'hello Hello HELLO'
rh = r"hello"

print re.findall(rh, s)
print re.findall(rh, s, re.I)  # re.I: IGNORECASE

# | 或者

w = "www.123.com"
ww = "www.123.cn"

rr = r"www.123.(cn|com)" 

print re.findall(rr, w)
print re.findall(rr, ww)  

# application on website url

s = """src='http://123.com/1.jpg'
<br>
src='http://123.com/6.jpg wii'
src='http://123.com/8.jpg'
"""

r = r"src='.+\.jpg'"

print re.findall(r, s)

r1 = r"src='.*\.jpg'"

print re.findall(r1, s)

r2 = r"src='(.*\.jpg)'"    # only return url inside the ()

print re.findall(r2, s)