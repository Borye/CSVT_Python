class MyClass(object):
	name = "test class"    
	__money = "500"        

	def myMethod(self):
		print self.name

	def __say(self):
		print "i have %s yuan" % self.__money

if __name__ == "__main__":
	inst1 = MyClass()
	print inst1.name