class MyFirstClass(object):
	pass

print dir(MyFirstClass)      # see the method in the class
myInstance = MyFirstClass()  # create a object
print dir(myInstance)        # the method of this object
print type(myInstance)

myInstance.a = 100           # add feature a

print dir(myInstance)        # can see a is added
print dir(MyFirstClass)      # wouldn't change in class 

print isinstance(myInstance, MyFirstClass)

MyFirstClass.a = 200
inst1 = MyFirstClass()
inst2 = MyFirstClass()
print inst1.a                # 200
print inst2.a                # 200

