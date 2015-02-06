class MyClass(object):
	name = "test class"

	def myMethod(self, x):
		print x

	def myMethod2(sef):
		print name

	def myMethod3(self):
		print self.name            


inst1 = MyClass()
print inst1.name         # print feature
inst1.myMethod('hello')        # use method "myMethod"
# inst1.myMethod2()  # this will cause error, it can be local variable
inst1.myMethod3()