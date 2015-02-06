#coding:utf8
'''
use open or file
file_handler = open(filename, mode)

mode:
r   只读
r+  读写
w   写入  删除原文件 重新写入
w+  读写

a   写入
a+  读写  在文件末尾追加内容，如果文件不存在，创建之
b   打开二进制文件  与 r w a + 组合使用
U   支持所有换行符号 \r  \n  \r\n 
'''

fobj = open('123.txt')
print fobj.read()
fobj.close()

fobj = open('456.txt', 'w')
fobj.close()

fobj = open('789.txt', 'w')  # w, if there are no file in that directory, it will create a new one 

fobj = open('123.txt', 'a')  # continue write
fobj.write('borye\n')
fobj.close()

fobj = open('123.txt', 'r+')
# fobj.read()
# fobj.read()
# read twice, no data
# fobj.write('new line\n')
# fobj.flush() 刷新
# fobj.seek(0, 0) 指针回到文件开头
'''
fileobj.seek(偏移量，选项)

选项=0 时， 表示将文件指针指向从文件头部到偏移量字节处
选项=1 时， 表示将文件指针指向从文件的当前位置，向后移动到偏移量子字节处
选项=2 时， 表示将文件执着呢指向从文件的尾部 向前移动偏移量字节
'''
# print by line

for line in open('123.txt', 'r'):
	print line

# read from one file and write to another file

f_in = open('111.txt')
f_out = open('222.txt', 'w')

contents = f_in.read()
f_out.write(contents)

f_in.close()
f_out.close()