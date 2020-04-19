from random import *

daylist = []

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