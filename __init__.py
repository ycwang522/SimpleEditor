# coding: cp936
# print '中文测试'
# fourth = raw_input('Year: ')[3]
# print fourth
print '\n---------------分片-------------------'
tag = '<a href="http://www.python.org">Python Web Site </a>'
print tag[9:30]
print '\n---------------分片Plus-------------------'
numbers1 = [1,2,3,4,5,6,7,8,9,10]
# 如果要访问序列中最后三个元素时，可以使用以下方法
print numbers1[-3:]
print numbers1[:3]
print numbers1
print numbers1[:]

print numbers1[0:10:2]
print '\n---------------序列相加-------------------'
print [1,2,3]+[4,5,6]
# print [1,2,3]+4
#print ['hello']+'world'
print [1,2,3]+['world']
print '\n---------------序列相乘-------------------'
sequence = [None]*10
print sequence

print '\n---------------成员检查-------------------'
permissions = 'rwct'
print 'w' in permissions

colors = ['blue','yellow','brown','red','black']
print 'blue' in colors
print 'white' in colors
print '\n---------------长度+最小最大值-------------------'
numbers = [100,2,56]
print '长度为：' ,len(numbers)
print '最小值为：',min(numbers)
print '最大值为：',max(numbers)



print '\n---------------索引-------------------'
edwad = ['Edward', 42]
john = ['John Smith', 50]
database = [edwad, john]
print database[0]
print database[1]
print database
edwad.append('object')
print edwad
edwad.pop()
print edwad
edwad.pop()
print edwad
edwad.pop()
print edwad
print database
database.pop()
print database

print '\n---------------列表-------------------'
print list('python')
seq = ['I','am','a','teacher','a']
seq1 = ['You','are','a','student'] 
print seq
seq.append('student')
print seq
print seq.count('a')
seq.extend(seq1)
print seq

print '\n---------------列表-------------------'
numbers = [1,2,3,5,5]
numbers.insert(3,'four')
print numbers

print '\n---------------remove()-------------------'
x=['to','be','or','not','to','be']
print x
x.remove('be')
print x
x.reverse()
print x

num=[5,3,5,72,1,4]
num.sort()
print num

x=['aardvar','abalone','came','add','aerate']
x.sort(key=len) #以长度len为关键词进行排序
print x

num=[5,3,5,72,1,4]
num.sort(reverse=True)    #排序且反转
print num