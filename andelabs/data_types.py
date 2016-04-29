def data_type(A):

	'''
	Takes in an argument.Compares and returns the result.
		-For string returns its length
		-For none return string  "no value"
		-For booleans return the boolean
		-For integers return a string showing how it compares to 100 
			if 67 return "less than 100" 
			for 400 return "more than 100" or "equal to 100"
		-For lists return 3rd item ,0r None if it doesnt exist
	'''
	
	if type(A) == str:
		return len(A)
	elif A == None:
		return "no value"
	elif type(A) == bool:
		return A
	elif type(A) == int:
			if A < 100:
				return "less than 100"
			elif A >= 100:
				return "more than 100"
			else:
				return "equal to 100"
	elif type(A) == list:
		if len(A) > 2:
			return A[2]
	else:
		return "Done!"

print (data_type("Emmah"))
print (data_type(""))
print (data_type(True))
print (data_type(False))
print (data_type(50))
print (data_type(100))
print (data_type(200))
print (data_type(['Emmah', 'Remy', 'Guylord']))