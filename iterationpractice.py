from random import *

customers = []

for c in range(20):
	num = randrange(5, 51);
	customers.append(num);

print(customers)

accept_customer = 0;
index = 1;
for c in customers:
	if c >=5 and c <= 15:
		print("[O] {}번째 손님 (소요시간 : {}분)".format(str(index), str(c)))
		accept_customer += 1
	else:
		print("[ ] {}번째 손님 (소요시간 : {}분)".format(str(index), str(c)))

	index +=1;


###