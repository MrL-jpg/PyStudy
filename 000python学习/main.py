# 词典学习
# slang_ditc = {"想你的风别吹了":"对旅游地常见的“想你的风吹到了XXX”网红标语的调侃和讽刺",
#               "显眼包":"指一眼看过去，第一眼就会锁定的焦点",
#               "你人还怪好嘞":"指当代年轻人非常容易相信别人，却因此挨到社会痛捶的调侃。",
#               "精神状态良好":"形容自己精神状态良好的反讽，实际精神状态非常不稳定。",
#               "纯爱战士":"形容一群相信纯洁，美好剧情或爱情关系，不接受任何意义上的出轨的人。",
#               }
# print("当前网络流行语条数: "+str(len(slang_ditc)))
# judge = input("按1或0选择查询或添加流行语")
# if int(judge) == 1:
#     user_input = input("请输入要查询的网络流行语:")
#     if user_input in slang_ditc:
#         print(user_input+": \n\t"+slang_ditc[user_input])
#     else:
#         print("未查询到相关信息")
# else:
#     key = input("输入键: ")
#     key_value = input("输入值: ")
#     slang_ditc[key] = key_value
#     for i in slang_ditc:
#         print(slang_ditc[i])
#         print("\n")

# for循环
# 1>高温人员及人数统计
# employee_temperatures = {
#     'E0001': 37.2, 'E0002': 36.8, 'E0003': 37.5, 'E0004': 38.3, 'E0005': 36.9,
#     'E0006': 37.1, 'E0007': 38.5, 'E0008': 36.7, 'E0009': 37.8, 'E0010': 36.4,
#     'E0011': 37.3, 'E0012': 37.6, 'E0013': 36.5, 'E0014': 38.1, 'E0015': 37.0,
#     'E0016': 37.9, 'E0017': 37.4, 'E0018': 36.6, 'E0019': 37.7, 'E0020': 38.7,
#     'E0021': 36.3, 'E0022': 37.2, 'E0023': 37.1, 'E0024': 36.9, 'E0025': 38.4,
#     'E0026': 37.5, 'E0027': 37.8, 'E0028': 36.2, 'E0029': 37.6, 'E0030': 39.0,
#     'E0031': 36.7, 'E0032': 37.3, 'E0033': 37.4, 'E0034': 36.8, 'E0035': 38.9,
#     'E0036': 37.0, 'E0037': 36.1, 'E0038': 37.9, 'E0039': 38.2, 'E0040': 36.5,
#     'E0041': 37.7, 'E0042': 37.1, 'E0043': 36.3, 'E0044': 37.8, 'E0045': 38.6,
#     'E0046': 37.2, 'E0047': 37.4, 'E0048': 36.9, 'E0049': 37.5, 'E0050': 39.1,
#     'E0051': 36.6, 'E0052': 37.0, 'E0053': 37.6, 'E0054': 38.0, 'E0055': 36.8,
#     'E0056': 37.3, 'E0057': 38.5, 'E0058': 37.7, 'E0059': 36.4, 'E0060': 38.3,
#     'E0061': 37.1, 'E0062': 37.9, 'E0063': 37.2, 'E0064': 36.7, 'E0065': 39.3,
#     'E0066': 37.4, 'E0067': 37.5, 'E0068': 36.2, 'E0069': 37.6, 'E0070': 38.9,
#     'E0071': 37.0, 'E0072': 36.3, 'E0073': 37.8, 'E0074': 38.1, 'E0075': 36.9,
#     'E0076': 37.7, 'E0077': 39.2, 'E0078': 37.1, 'E0079': 36.5, 'E0080': 38.4,
#     'E0081': 37.3, 'E0082': 37.4, 'E0083': 38.7, 'E0084': 36.8, 'E0085': 37.9,
#     'E0086': 37.5, 'E0089': 36.4, 'E0090': 38.5,
#     'E0091': 37.2, 'E0092': 36.9, 'E0093': 37.8, 'E0094': 38.2, 'E0095': 36.1,
#     'E0096': 37.4, 'E0097': 39.0, 'E0098': 37.6, 'E0099': 38.3, 'E0100': 36.7
#     }
# i = 0
# for (worker_id,worker_temperature) in employee_temperatures.items():
#     if worker_temperature > 38:
#         i += 1
#         print(worker_id+":"+str(worker_temperature))
# print("总高温人数为:"+str(i))

# 2>range求和
# total = 0
# for i in range(1,101) :
#     total += i
# print(total)

# while循环
#
# sum = 0;
# count = 0;
# while 1:
#     count += 1
#     temp = input("Enter a number or enter q to quit: ")
#     if temp == "q":
#         break
#     else :
#         sum += int(temp)
# print("the average is", sum/count)

# 格式化字符串
# stu = {"xiaoming":20,
#        "xiaozhang":21,
#        "xiaowang":56
#        }
# for (name,num) in stu.items():
#     msg = f'''最终成绩单
#             姓名:{name}
#             成绩:{num}
#     '''
#     print(msg)
# print("sfrnesrgjnegbergb{0}ssfnlirfb{1}".format("sdjnc","anjda"))

# 面向对象
# 1>创建类
# class CuteCat:
#     def __init__(self,cat_name,cat_age,cat_food):
#         self.cat_name = cat_name
#         self.cat_age = cat_age
#         self.cat_food = cat_food
#     def show_cat(self):
#         print(self.cat_name, self.cat_age, self.cat_food)
#
# class Student:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#         self.grades = {"语文":0,"数学":0,"英语":0}
#     def set_grade(self,course,grade):
#         if course in self.grades:
#             self.grades[course] = grade
#     def show_grade(self):
#         for course in self.grades:
#             print(f"{course} : {self.grades[course]} ")
# zeng = Student("zw",1008)
# zeng.set_grade("语文",100)
# zeng.set_grade("数学",100)
# zeng.set_grade("英语",100)
# zeng.show_grade()
#
# class animal:
#     def __init__(self,specise,wgiht,high):
#         self.specise = specise
#         self.wgiht = wgiht
#         self.high = high
#     def animal_food(self,food):
#         print(f"{self.specise}吃{food}")
#
# pig = animal("猪",500,1)
#
# pig.animal_food("sao")

# 2>类的继承
# class employee:
#     def __init__(self, name, worker_id):
#         self.name = name
#         self.worker_id = worker_id
#
#     def print_info(self):
#         print(f"Name: {self.name}\nWorker ID: {self.worker_id}")
#
#
# class FullTimeEmployee(employee):
#     def __init__(self, name, worker_id, monthly_salary):
#         super().__init__(name, worker_id)
#         self.monthly_salary = monthly_salary
#
#     def calculate_salary(self):
#         print(f"{self.name}的月薪为: {self.monthly_salary}")
#
#
# class PartTimeEmployee(employee):
#     def __init__(self, name, worker_id, daily_salary, work_days):
#         super().__init__(name, worker_id)
#         self.daily_salary = daily_salary
#         self.work_days = work_days
#
#     def calculate_salary(self):
#         print(f"{self.name}的薪水为: {self.daily_salary * self.work_days}")
#
# zhang = FullTimeEmployee("zhang",1000,10000)
# wang = PartTimeEmployee("wang",1001,600,20)
#
# zhang.print_info()
# zhang.calculate_salary()
# wang.print_info()
# wang.calculate_salary()

# 文件操作

# 1>手动关闭文件
# f = open("../text.txt","r",encoding="utf-8")
# print(f.read())
# f.close()

# 2>自动关闭文件
# with open("../text.txt","r",encoding="utf-8") as f:
#     print(f.readline())
#
# with open("../text.txt","r+",encoding="utf-8") as f:
#     f.write("hello")

# 报错处理

# try :
#     f = float(input("Enter a number: "))
# except ValueError :
#     print("Invalid input")
# except :
#     print("Invalid input")
# finally:
#     print("Done")
###############################################################################################
#浅拷贝和深拷贝
# import copy
# alist = [1,2,3,4,[5,6,7]]
###############################################################################################
## 赋值-内外层数据完全共享且地址相同
# alist2 = alist
# alist.append(6)
# alist[4].append(8)
# print(f"alist:{alist}\nalist2:{alist2}")
# print(f"外层alist:{id(alist)}\n外层alist2:{id(alist2)}\n内层alist{id(alist[4])}\n内层alist2{id(alist2[4])}")
###############################################################################################
## 浅拷贝-内外数据不完全共享,外层地址相同内层地址不相同
# alist2 = copy.copy(alist)
# alist.append(6)
# alist[4].append(8)
# print(f"alist:{alist}\nalist2:{alist2}")
# print(f"外层alist:{id(alist)}\n外层alist2:{id(alist2)}\n内层alist:{id(alist[4])}\n内层alist2:{id(alist2[4])}")
###############################################################################################
## 深拷贝-内外数据完全不共享,内外层地址均不同
# alist2 = copy.deepcopy(alist)
# alist.append(6)
# alist[4].append(8)
# print(f"alist:{alist}\nalist2:{alist2}")
# print(f"外层alist:{id(alist)}\n外层alist2:{id(alist2)}\n内层alist:{id(alist[4])}\n内层alist2:{id(alist2[4])}")
##############################################################################################
# 异常捕获
##############################################################################################

# from random import choice

# for i in range(6):
#     x = choice(["abc",1,2,3,4,5]) #随机选择一项··
#     print(x)
##############################################################################################
# 类封装

## 1.普通属性或方法-可在任意地方使用
## 2.'__'开头，无法被外部直接访问，子类也无法继承,无法通过from XXX import 引用
## 3.'_'开头，声明私有属性或方法，内外可直接访问，但是无法通过from XXX import 引用

# class Persion:
#     name = "li"
#     __name = 'tang'
# li = Persion()
# Persion.name = 'zhang'
# print(li.name)
# print(Persion.name)
###############################################################################################
# 属性查看
# print(dir(object)) 
###############################################################################################

# 多继承

# class A(object):
#     def __init__(self):
#         print('Init_A')
#         pass
# class B(object):
#     def __init__(self):
#         print('Init_B')
#         pass

# class C(B,A):
#     def __init__(self):
#         super().__init__()
# c = C()

#############################################################################################

# 静态方法-使用@staticmethod修饰,静态方法没有self和cls参数的限制
#        -静态方法与类无关，可以被转换成函数使用
#        -静态方法既可以使用类访问，也可以使用对象访问

# class A(object):

#     @staticmethod
#     def method_A():
#         print('A')
# a = A()
# A.method_A()
# a.method_A()

# 类方法-使用@classmethod修饰,第一个参数必须是类对象，一般为cls
#        -类方法可以访问类属性或类的其他方法
#        -类方法一般配合类属性使用

# class A(object):
#     @classmethod
#     def method_A(cls):
#         print("cls",cls) # cls代表类本身,类本质上就是一个对象
#         print('A')

# print("A",A)
# A.method_A()

###########################################################################################

#__new()__ 由object基类提供的内置的静态方法
##作用:
    #1、在内存中为对象分配空间
    #2、返回对象的引用,传递给self

#对象的实例化步骤: __new__(cls)【创建对象】 --> __init__(slef)【初始化对象】 

# class A(object):
#     def __init__(self):
#         print('Init')
#     def __new__(cls):
#         new = super().__new__(cls) #静态方法必须要cls参数
#         return new  #重写__init__方法后必须有返回值,返回此实例化对象
###########################################################################################

#单例模式
    ##可以理解为一个特殊的类，这个类只存在一个对象，无论实例化多少个，都是那一个(内存地址都相同)
    ##优点:
        ###1、节省内存空间减少不必要的资源浪费
    ##缺点
        ###1、多线程访问容易引发线程安全的问题
##实现方法
    ###1、通过@classmethod实现
    ###2、通过装饰器实现
    ###3、通过重写__new__(cls)方法实现(常用)
    ###4\通过导入模块实现

##__new__()实现
##步骤
    ###1、定义一个类属性，初始值为None,用来记录对象的引用(地址)
    ###2、重写__new__(cls)方法
    ###3、判断类属性是否为None,如果是，就把__new__(cls)返回的对象引用保存进去
    ###4、返回类属性中记录的对象引用

# class A(object):

#     obj = None #用于保存对象 

#     def __new__(cls):
#         print('new')
#         if cls.obj == None:
#             cls.obj = super().__new__(cls)
#         return cls.obj
    
#     def __init__(self):
#         print('init')

# a1 = A()
# a2 = A()

# print('a1',a1)
# print('a2',a2)

#观察输出:a1和a2为同一对象

##导入模块实现
# from extra import test as te1
# from extra import test as te2

# print('te1',te1)
# print('te2',te2)
###########################################################################################