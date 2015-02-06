class Staff(object):

	def __init__(self, id = '', name = '', gender = ''):
		'''
		initialize
		''' 
		self.id = id
		self.name = name
		self.gender = gender

	def update(self, id = '', name = '', gender = ''):
		if id:
			self.id = id
		if name:
			self.name = name
		if gender:
			self.gender = gender

	def __str__(self):
		'''
		for print object
		'''
		return "id: %s, name: %s, gender: %s" \
		  % (self.id, self.name, self.gender)


borye = Staff()
borye.update(0, 'borye', 'male')
print borye.id, borye.name, borye.gender

zou = Staff(1, 'zouqixian', 'male')

print zou.id

print zou
