from person import Person
from kenya import Kenyan
#ASIDE
#PEP8
#
#Instance vs class variables
#class methods (advanced topic)



#end of class
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


k = Kenyan('Anita Waiguru', 30)
k.probe(True)

print ("Is {} corrupt? {}".format(k.name, k.is_corrupt()))	
print (k.say_hello())
