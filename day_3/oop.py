#PEP8
#
#Instance vs class variables
class Person:
	#class variables
	people_count = 0
	def __init__(self, name, age):
		#instance variiables
		self.name = name
		self.age = age
		Person.people_count += 1
		
	def __repr__(self):
		return "<object: {}, {}>".format(self.name, self.age)

	def say_hello(self):
		return "Hello I'm {} and I'm {} years old".format(self.name, self.age)

p = Person('Emmah',19)
p2 = Person('Joe', 25)
p3 = Person('Loulou',35)
print (p.say_hello())

a = [('Jane', 23),('Joe',50),('Jacob',20),('Jee',24),('Josh', 60)]
'''
b = []
for name , age in a:
	person = Person(name,age)
	b.append(person)
'''
b = [Person(name, age) for name, age in a]
for person in b:
	print (person.say_hello())


print (p.name)
print (p.age)
print (p.people_count)
print (b)

