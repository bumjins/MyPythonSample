class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def say_hello(self, to_name):
		print("안녕 " + to_name + " 나는 " + self.name)

	def introduce(self):
		print("My name is " + self.name + " And I am " + str(self.age) + " years old")


class Programmer(Person):
	def program(self, to_program):
		print("Next I Make "+ to_program);

p = Programmer("Bumjin", 40)
p.introduce()
p.program("Rest Server");