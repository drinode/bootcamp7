a = [10,40,50,30,20,90]
'''
for i in a:
	print (i)
'''
# print in reverse

i=len(a)

'''while i > 0:
	print (a[i - 1])
	i -= 1

for i in range(len(a) -1,-1,-1):
	print (a[i])
'''
b = [(2,4),(6,8),(2,6),(8,2)]

'''
x:2 , y: 4
x:5 , y: 10

'''
for x, y in b:
	print ('x:{}  y:{}'.format(x, y))

for i in b:
	print ('x: {} , y: {}'.format (i[0],i[1]))

f= [(10,20,30),]
	 