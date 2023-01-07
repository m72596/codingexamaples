# Python3 program to
#creating class in python 

class Loan:

	# A simple class
	# attribute
	attr1 = "debit"
	attr2 = "credit"

	# A sample method
	def fun(self):
		print("Balance", self.attr1)
		print("Balance", self.attr2)


# Driver code
# Object instantiation
var = Loan()

# Accessing class attributes
# and method through objects
print(var.attr1)
var.fun()
