# coding:cp936
'''
Created on 2016年10月25日

@author: iPC
'''
from wx.tools.Editra.src.ed_vim import Para
print '-----------异常------------'
# raise Exception
#raise Exception("Invalid code!")

import exceptions
print dir(exceptions)
import BeautifulSoup

print dir(BeautifulSoup)
print '\n-----------抽象------------'
# raise ArithmeticError("Test")
fibs=[0,1]
for i in range(8):
    fibs.append(fibs[-1]+fibs[-2])
print fibs

import math
print '%5.3f' %(math.sqrt(9))


print '\n-----------函数定义------------'
def hello(name):
    'the interpretation of hello function'
    return 'hello '+name+'!'
print hello.__doc__
print hello('Wang')
print help(hello)

def hello_1(name,greeting):
    print '%s,%s' %(name,greeting)
    
hello_1('hello', 'world')
hello_1(name='hello', greeting='world')    
print '\n-----------搜集参数------------'
def print_sort(*para):
    print para

print_sort('a','b','c','d')    
print_sort()

def print_sor(title,*para):
    print title,para 
print_sor('ycwang',18,56,89,25,36)   

def func4(x,y,z=3,*par1,**par2):
    print x,y,z
    print par1
    print par2
    
func4(1,3,4,5,6,7,8,9,0,a=1,b=2)     


def print_length_of_function(x):
    print "the length of ",repr(x),'is',len(x)
    
print_length_of_function('fnord') 
print_length_of_function([1,2,3])  



print '\n-----------类的成员函数私有化------------'
class Private:
    def __inAccessible(self):
        print "This function can't used out class"
    
    def Accessible(self):
        print "This function can used out class"
        self.__inAccessible()

obj = Private()
obj.Accessible()
obj._Private__inAccessible()
print '\n-----------类的成员函数私有化end------------'
Exception           #所有异常的基类
AttributeError      #特性引用或赋值失败时引发
IOError             #试图打开不存在的文件是引发
IndexError          #使用序列中不存在的索引时引发
KeyError            #使用映射中不存在的键时引发
NameError           #找不到名字（变量）时引发
SyntaxError         #在代码为错误形式时引发
TypeError           #内建操作或者函数应当用于错误类型的对象时引发
ValueError          #在内建操作或者函数应用于正确类型的对象，但是该对象使用不合适的值时引发
ZeroDivisionError   #除法或者模除操作的第二个参数为0时引发

# try:
#     x = input("Enter the first number: ")
#     y = input("Enter the second number: ")
#     print x/y
# 
# except(ZeroDivisionError,TypeError),e:
#     print e
    
    
print '\n-----------类------------'
class Person:
    
    def setName(self,name):
        self.name=name
    
    def setAge(self,age):
        self.age=age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def greet(self):
        print "hello,I'm %s" %self.name
        
object1=Person()
object1.setName('ycwang')
object1.setAge(23)
print object1.getAge()
print object1.getName()
print object1.name
print object1.age
object1.greet()

print '\n-----------异常之finally------------'
x = None
try:
    x = 1/0
finally:
    print 'cleaning up!'
    del x
