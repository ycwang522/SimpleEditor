# coding: cp936
'''
Created on 2016年10月25日

@author: iPC
'''

print '-------------dict函数----------'
items={('Ruby','56'),('python','89')}
ite = dict(items)
print ite
print ite['Ruby']

d = dict(Ruby='56',python='89')
print d
print d['Ruby']
d.clear()
print d

print '-------------字典方法----------'
x={'username':'admin','machines':['foo','bar','baz']}
y=x.copy()
y['username']='wyc'
y['machines'].remove('foo')
print y

print {}.fromkeys(['name','age'])

names=['anne','jane','geogre','damon']
ages=[12,34,32,102]
print zip(names,ages)
for name,age in zip(names,ages):
    print name,'is',age,'years old!'
    


