def sum_digits(A):

	'''
	Takes a list A, and returns the sum of all the 
	digits in the list
	e.g. [10,30,45] should return 1+0+3+0+4+5=13
	'''
	
	int_i == 0
	str_i == 0
  
    for i in A:
  	   str_i = str(int_i)
  	    for char_i in str_i:
  	        int_i += int(char_i)
	print int_i

sum_digits(10,30,45)


