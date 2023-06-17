import datetime
DOB=input(' enter your date of birth()')
 # print(DOB)
DOBsplit=DOB.split('/')
 # print(DOBsplit)
age=0
DOBday=int(DOBsplit[0])
DOBmonth=int(DOBsplit[1])
DOByear=int(DOBsplit[2])
# print(DOBday,DOBmonth,DOByear)
todayDate= datetime.datetime.now()
currentMonth=int(todayDate.strftime("%m"))
currentDay=int(todayDate.strftime("%d"))
currentYear=int(todayDate.strftime("%Y"))
if ((currentMonth==DOBmonth)and(currentDay>=DOBday))or((currentMonth>DOBmonth)):
    age=currentYear-DOByear
else:
    age=currentYear-DOByear-1
print('Hiii !!! Your current age is ',age)