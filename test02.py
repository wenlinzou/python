#coding:utf-8
#数据类型
num1 = 123
print(type(num1))

num2 = 123.3
print(type(num2)) 

num3 = 123.3j
print(type(num3)) 

num4 = '123.3j'
print(type(num4)) 

# 字符串String
str1 = 'str1'
str2 = "str2"
print(str1)
print(str2)

say = 'let\'s go'
print(say)
say = "let's go"
print(say)
say = "\"let's go\""
print(say)

mail = 'tom: hello nice to meet u'
print(mail)
mail = '\ntom: \n\thello nice to meet u'
print(mail)

mail="""tom:
	i am jack
	goodbye"""
print(mail)	#也可以用单引号(保存格式化输入)

a = 'abcdefg'
print(a[0])
print(a[0]+a[1])

#切片 截取
print(a[1:3])#前包后不包
print(a[:4])
print(a[2:])

#每几个取一次
print(a[::1])
print(a[::2])
print(a[::3])

print(a[-1])
print(a[-4:-1])
print(a[1:4])
print(a[-2:-4:-1])

print(a[::-1])#倒叙
#序列
#() [] {}
print(a[1:4])
print(a[:])
print(a[::])
print(a[::2])

#len序列长度
print(len(a))

str1 = '12345'
str2 = 'abcdefg'
print(str1+str2)

#重复次数
print(str1*5)
print("#"*40)

print('c' in str2)
print('c' in str1)

print('a' not in str1)
print(str1 not in str2)

print(max(str1))
print(min(str1))

print(max(str2))
print(min(str2))

str3 = '12345'
print(str1==str3)

userinfo = "jack 30 male"
print(userinfo[:4])

#元祖 不可变
user = ("tom",23,"male")
print(user)
print(user[0])
print(user[1])
print(user[2])

iempty = ()
print(iempty)
iempty2 = (2,)
iempty3 = (3)
print(type(iempty3))
print(type(iempty2))


#变量接收
name,age,gender=user
print(name)
print(age)
print(gender)

a,b,c = (1,2,3)
print(a)


#第六节序列-列表
#() []

#列表[]
listmilo = []
print(type(listmilo))
list1 = [1,2,3,4,5,'张三']
t = ('milo',23,'male')

print(t[0])
print(list1[5])

print(list1[0::])

t3 = ('abc')
l3 = ['abc']
print(type(l3))

#列表操作
#取值 1切片和索引 2list[]
#添加 list.append()
#删除 del(list[]) list.remove(list[])
#修改 list[] = x
#查找 var in list

print(list1)
print(list1[0])

list1[0] = '厉害'
print(list1[0:])


boat = ('red',23,12)
print(boat)
print(id(boat))
boat = ('red',33,12)
print(id(boat))

#add
list1.append('i am last')
print(list1)

list1.remove(list1[6])
print(list1)

list1.remove(list1[3])
print(list1)
list1.remove(2)
print(list1)



#第七节 字典
table1 = ['name','age','gender']
table2 = ['jim',30,'male']
# print(zip(table1,table2))
dic={0:0,1:1,2:2}
print(dic[0])
print(dic[1])
print(dic[2])

dic1={'name':'jim','age':23,'gender':'male'}
print(dic1['name'])
print(dic1['age'])
print(dic1['gender'])

dic2={1:'123',name:23,'sex':'male'}
print(dic2[1])

dic3 = {a:'aaa','b':'bbb'}
print(a)
print(b)

print(dic3)
a = 123
b = 456
dic3 = {a:'aaa','b':'bbb'}
print(dic3[123])
print(dic3)

print help(dic3.keys)

for k in dic1:
	print(k)

for k in dic1:
	print(dic1[k])	

#字典更新删除update()可以将整个字典的内容拷贝到另一个字典中
#del dict1['a']	删除字典中


	


# img = cv2.imread('test.jpg',cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imwrite('PythonMethod.jpg', gray)


