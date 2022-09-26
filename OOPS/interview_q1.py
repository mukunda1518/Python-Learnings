class A:
	def __init__(self):
		self.x = 5

	def mul(self):
		return self.x * 2

	def add(self):
		return self.x + 5

class B(A):
	def __init__(self):
  		self.x = 10

	def mul(self):
		return self.x * 2

def main():
	b = B()
	print(b.mul()) #20
	print(b.add()) #15
main()