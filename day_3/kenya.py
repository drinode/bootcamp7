from person import Person

class Kenyan(Person):
	corrupt = False
	def probe(self, corrupt):
		self.corrupt = corrupt

	def is_corrupt(self):
		if self.corrupt:
			return "Yes"
		return "No"
		
#for now do later in other files.

k = Kenyan('Anita Waiguru', 30)
k.probe(True)

print ("Is {} corrupt? {}".format(k.name, k.is_corrupt()))	
print (k.say_hello())		