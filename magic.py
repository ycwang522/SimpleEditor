#coding:cp936
'''
Created on 2016年10月26日

@author: iPC
'''
from re import match, search
__metaclass__=type      #声明为新型class
print '--------------魔法方法------------'

class FooBar:
    def __init__(self):
        self.name=52

f=FooBar()
print f.name



print '--------------类的继承------------'

class A:
    def printHello(self):
        print 'hell0 A()!'
        
class B(A):
    def printHello(self):
        print 'hello B()'
        
func = B()
func.printHello()

print '--------------Bird类------------'
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'add food'
            self.hungry = False #进食完成，不饿
        else:
            print 'No,Thanks!'
             
class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()
        self.sound = 'Squawk'
    def sing(self):
        print self.sound
 
#调用子类的sing()方法很容易
sb = SongBird()
sb.sing()        
 
#尝试调用父类的eat()方法
sb.eat()
       
print '--------------静态方法和类方法------------'
__metaclass__=type

class Myclass:
    @staticmethod
    def smeth():
        print 'This is a static method!'
        
    @classmethod
    def cmeth(cls):
        print 'This is a class method!',cls
        
Myclass.cmeth()
Myclass.smeth()

import hello
hello.hello()
hello.test()
print '\n--------------模块------------'
import copy
print [n for n in dir(copy) if n.startswith('_')]
 
print copy.__all__

print help(copy.copy)

print copy.copy.__doc__

print range.__doc__

print copy.__file__
print '\n--------------__dict__------------'
print copy.__dict__
print '\n--------------__name__------------'
print copy.__name__

import sys
print dir(sys)
print [n for n in dir(sys) if not n.startswith('_')]

print sys.path
print sys.platform
print '\n----------------time-------------'
import time
print time.gmtime()
print time.time()
print time.accept2dyear

print time.asctime()
print time.localtime()


print '\n-----------random-------------'
import random
print random.randint(2,10)


print '\n-----------regex-------------'


import re

print match('p','python')
print search('t','python')
print re.match('p', 'python')

some_text = 'alpha,beta,,,gamma delta'
print re.split('[,]',some_text)
print re.split('[, ]+',some_text)
print re.split('[,]*',some_text)

pat='[a-zA-Z]+'
text = '"Hm...Err -- are you sure?" he said, sounding insecure'
print re.findall(pat, text)
pat1='[aeiou]'
print re.findall(pat1, text)


pat2 = '{name}'
text='Dear {name}...'
print re.sub(pat2, 'Mr.Wang', text)

print re.escape('https://www.python.org')
print re.escape('But where is the am?')

print '-----------File Operator-------------'
'''
f=open('test.txt','w')
f.write('hello, python,')
f.write(' I Love It!')
f.close()
 
 
 
f=open('test.txt','w')
f.write(' It is very useful!')
f.close()
 
f1=open('test.txt','r')
print f1.read()
f1.close()
'''

f0=open(r'test.txt')
print f0.read()
f0.close()


f00=open(r'test.txt')
for i in range(4):
    print i,':',f00.readline()

f00.close()


import pprint
pprint.pprint(open(r'test.txt').readlines())


f01=open(r'test.txt')
for i1 in range(3):
    print str(i1)+':'+f01.readline()
    
f01.close()




