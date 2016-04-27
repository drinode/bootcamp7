def hello(name ,age, class_=''):
	'''
	Explanation 
	'''
	if class_ != '':
		return "I am {}, and I am {} years old, and {} class".format(name, age, class_)
	return "I am {}, and I am {} years old".format(name,age)
people = [('Jayne',23 ),
           ('Brian',50, 'Low'),
           ('Emmah',19, 'High'),
           ('Betty',45)
           ]
 #use of unpacking
for person in people:
	print (hello(*person))

for i in people:
	print ('I am {}, and I am {} years old'.format(i[0],i[1]))
            
def super_sum(*args):
 	'''
 	Takes in variable number of items,
 	and returns the sum.
 	e.g. super_sum(10,20) =30
 	     super_sum(10,20,40) = 30
 	     super_sum(1,4,5,6,7)=23

 	'''
 	total = 0
 	for i in args:
 		total += i
 	return total

print (super_sum(10,20))
print (super_sum(1,4,5,7))
a = [10,40,60]
print (super_sum(*a))



def hello_again(**kwargs):

	return "I am {}, and I am {} years old".format(kwargs['name'],kwargs['age'])

print (hello_again(name='Joe', age='20'))
print (hello_again(age='20', name='Jane'))

other_people = [
			{'name': 'Joe', 'age': 70},
			{'name': 'Jane', 'age': 50},
			{'name': 'Emmah', 'age': 19}
				]
joe = {'name': 'Joe', 'age':98}

print (hello_again(**joe))
print (hello_again(name='Joe', age=98))