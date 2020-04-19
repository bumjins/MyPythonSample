def std_weigth(height, gender):
	result = 0
	if gender == "Male":
		result = (height / 100) *(height / 100) * 22
	else:
		result = (height / 100) *(height / 100) * 21

	return result

height = 175
gender = "Male"
weight =round(std_weigth(height , gender),2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다." \
.format(height, gender, weight) )