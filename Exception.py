# coding:cp936
'''
Created on 2016��10��25��

@author: iPC
'''
from wx.tools.Editra.src.ed_vim import Para
print '-----------�쳣------------'
# raise Exception
#raise Exception("Invalid code!")

import exceptions
print dir(exceptions)
import BeautifulSoup

print dir(BeautifulSoup)
print '\n-----------����------------'
# raise ArithmeticError("Test")
fibs=[0,1]
for i in range(8):
    fibs.append(fibs[-1]+fibs[-2])
print fibs

import math
print '%5.3f' %(math.sqrt(9))


print '\n-----------��������------------'
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
print '\n-----------�Ѽ�����------------'
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



print '\n-----------��ĳ�Ա����˽�л�------------'
class Private:
    def __inAccessible(self):
        print "This function can't used out class"
    
    def Accessible(self):
        print "This function can used out class"
        self.__inAccessible()

obj = Private()
obj.Accessible()
obj._Private__inAccessible()
print '\n-----------��ĳ�Ա����˽�л�end------------'
Exception           #�����쳣�Ļ���
AttributeError      #�������û�ֵʧ��ʱ����
IOError             #��ͼ�򿪲����ڵ��ļ�������
IndexError          #ʹ�������в����ڵ�����ʱ����
KeyError            #ʹ��ӳ���в����ڵļ�ʱ����
NameError           #�Ҳ������֣�������ʱ����
SyntaxError         #�ڴ���Ϊ������ʽʱ����
TypeError           #�ڽ��������ߺ���Ӧ�����ڴ������͵Ķ���ʱ����
ValueError          #���ڽ��������ߺ���Ӧ������ȷ���͵Ķ��󣬵��Ǹö���ʹ�ò����ʵ�ֵʱ����
ZeroDivisionError   #��������ģ�������ĵڶ�������Ϊ0ʱ����

# try:
#     x = input("Enter the first number: ")
#     y = input("Enter the second number: ")
#     print x/y
# 
# except(ZeroDivisionError,TypeError),e:
#     print e
    
    
print '\n-----------��------------'
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

print '\n-----------�쳣֮finally------------'
x = None
try:
    x = 1/0
finally:
    print 'cleaning up!'
    del x
