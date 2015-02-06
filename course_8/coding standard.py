#coding:utf8

'''
代码规范：

文件头
注释：模块，语句，函数，类
编码：缩进，空格，空行，断行
命名：常量，变量，函数，类，模块包，缩写，特定命令
语句
赋值
判断与循环
注释标签的编写规范

PEP8 
'''

# 文件头

#!/usr/bin/env/ python
#coding=utf8
# Copyright(c) 2015 - borye<boli.89123@gmail.com>
'''
After title is the content of ...
'''

# 注释原则：
# 对不存在技术难点的代码坚持不注释
# 对存在技术难点的代码必须注释
# 对每一个包，模块，类，函数（方法）写'''注释，除非极度简单

# 导入库放在最前边

# 编码风格：

# 折行，断行
# 一行代码长度最大不要超过79个
# 在括号里面直接折行
# 没有括号的断行，可以使用\

x = 1
if x == 1 or x == 2 \
or x == 3 or x == 4:
	print x

# 空行
# 增加可读性
# 在类，函数的定义之间加空行
# 在import不同种类的模块间加空行
# 在函数中的逻辑段落间加空行

# 空格
# 缩进一定要空格
# 非缩进空格： 运算符之间，特殊符号中间，逗号等标点之间

# 命名
# 不论类成员变量还是全局变量，都不适用m或g前缀
# 私有类成员使用单一下划线前缀，多定义公开成员，少定义私有
# 变量名不应带有类型信息 iValue, names_list, dict_obj都是不好的命名

# 常量一般都是大写

WHITE = Oxffffffff
THIS_IS_A_CONSTANT = 1

# 变量是小写

color = WHITE
this_is_a_variable = 1

# 函数
# 如果多单词，首字母大学

# 类
# 全部首字母大写， 不使用下划线

# 模块
# 模块名全部小写，对于包内模块，可以加下划线前缀

# 缩写
# 常用的缩写： class XmlParser(object): 
# 命名中有长单词， 这时候应使用约定俗称的缩写方式，如
# 去除元音，包含辅音的首字符等方式，例如
# function-fn, text-txt, object-obj, count-cnt, number-num

# 条件表达式
# if var != None: do something 是不对的
# if var: do something  直接if var 就可以，只要var非空，他就是True







