#coding:utf8
'''
模块是python组织代码的基本方式
python的脚本都是.py文件
一个脚本可以单独运行，也可以导入另一个脚本运行
当脚本被导入运行时，我们称其为模块
模块名就是脚本的文件名
item.py ------- import item

包
创建一个包的步骤：
1 建立一个名字为包名字的文件夹
2 在该文件夹创建一个__init__.py文件
3 根据需要在该文件夹下存放脚本文件，已编扩展及子包
import pack.m1, pack.m2, pack.m3

起文件名的时候不要跟以有模块重复

导模块会先从当前目录导，如果当前没有，就去c://python27/lib 里面找

.py 脚本文件
.pyc 编译之后的文件
.pyo 优化之后的文件 
'''

import mymod
'''
mymod.jia(1, 2)
'''

import c1

t = c1.MyClass()
t.myMethod()

from c1 import MyClass     # 从模块c1里面导入类MyClass

t = MyClass()
t.myMethod()