#coding:utf-8
#三个人吃饭,分摊35.27美元饭费,他们还想留15美分的小费,怎么分
launch = (35.27-15)/3
print launch

#计算12.5m X 16.7m的房间面积和周长
acreage = 12.5 * 16.7
print(acreage)
perimeter = (12.5+16.7)*2
print(perimeter)

#写一个程序,把华氏温度转化为摄氏温度.公式:C=5/9*(F-32)
F = 260
C = 5/9*(F-32)
print(C)

#写一个小程序运算以80km/h的速度行驶200km需要的时间,并显示答案
needTime =  200 / 80
print(needTime)
print("--------------------------华丽的分割线-----------------------")
#四则运算
bool = True
while bool:
	print("1求和 - 2求差 - 3求积 - 4求商 - 5求余 - 0退出")
	info1 = "输入第一个数"
	info2 = "输入第二个数"
	content = input("选择运算类型")
	choose = int(content)
	if choose == 0:
		bool = False
		break
	sumInfo1 = int(input(info1))
	sumInfo2 = int(input(info2))

	if choose == 1:
		# sumInfo1 = int(input(info1))
		# sumInfo2 = int(input(info2))
		print(sumInfo1+sumInfo2)
	elif choose == 2:
		# sumInfo1 = int(input(info1))
		# sumInfo2 = int(input(info2))
		print(sumInfo1-sumInfo2)
	elif choose == 3:
		# sumInfo1 = int(input(info1))
		# sumInfo2 = int(input(info2))
		print(sumInfo1*sumInfo2)
	elif choose == 4:
		# sumInfo1 = int(input(info1))
		# sumInfo2 = int(input(info2))
		print(sumInfo1/sumInfo2)
	elif choose == 5:
		# sumInfo1 = int(input(info1))
		# sumInfo2 = int(input(info2))
		print(sumInfo1%sumInfo2)	
	# elif choose == 0:
	# 	bool = False		
print("is over")