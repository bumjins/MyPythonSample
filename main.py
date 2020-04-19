# class Person:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def say_hello(self, to_name):
# 		print("안녕 " + to_name + " 나는 " + self.name)

# 	def introduce(self):
# 		print("My name is " + self.name + " And I am " + str(self.age) + " years old")


# class Programmer(Person):
# 	def program(self, to_program):
# 		print("Next I Make "+ to_program);

# p = Programmer("Bumjin", 40)
# p.introduce()
# p.program("Rest Server");

from random import *

daylist = []

print(len(daylist))

# for i in range(4):
# 	day = randint(4, 28)

# 	if day not in daylist:
# 		print("리스트에 없는 날짜입니다")
# 		daylist.append(day)
# 	else:
# 		print("리스트에 이미 있는 날짜 입니다.")


while len(daylist) < 4:
	day = randint(4, 28)

	if day not in daylist:
		print("리스트에 없는 날짜입니다")
		daylist.append(day)
	else:
		print("리스트에 이미 있는 날짜 입니다.")

daylist.sort()
print("오프라인 모임날짜는 매월 " + str(daylist[3]) +"일로 선정되었습니다.")		
print(daylist)