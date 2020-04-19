jumin = "800101-1234567"

print("성별 : " + jumin[7])
print("태어난 년도 : " + jumin[0:2])
print("태어난 달 : " + jumin[2:4])
print("태어난 날짜 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])


#문자열 처리함수 
python = "Python is Amazing"
print(python.upper())
print(len(python))
print(python.replace("Python", "C++"))

#find와 index의 차이 
#find는 -1을 출력하고 이후 나오는 것을을 실행하지만 index는 에러처리되서 안됨

print("{}, {}".format("blue", "red"))
print("{0}, {1}".format("blue", "red"))
print("{1}, {0}".format("blue", "red"))


print("{age}, {color}".format(age = 20, color = "red"))

age = 40
color = "black";

print(f"{age}, {color}")

#URL로 사이트 비밀번호를 만드는 프로그램
#role1. http://부분은 제외
#role2. 처음 만나는 .은 제외
#role3. 남은 글자중 처음 세자리 + 글자 개수 + 글자내 'e' 개수 + !

# from parse import *
# siteurl = "http://naver.com"

# role1 = parse("http://{}", siteurl)
#위의 Parse를 사용해도 되지만 더간단하게
siteurl = "http://naver.com"
role1 = siteurl.replace("http://", "")
print(role1)

role2 = role1.split('.')
print(role2)

newpasswd = role2[0][:3] + str(len(role2[0])) + str(role2[0].count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(siteurl, newpasswd))