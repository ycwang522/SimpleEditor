# coding: cp936
# print '���Ĳ���'
# fourth = raw_input('Year: ')[3]
# print fourth
print '\n---------------��Ƭ-------------------'
tag = '<a href="http://www.python.org">Python Web Site </a>'
print tag[9:30]
print '\n---------------��ƬPlus-------------------'
numbers1 = [1,2,3,4,5,6,7,8,9,10]
# ���Ҫ�����������������Ԫ��ʱ������ʹ�����·���
print numbers1[-3:]
print numbers1[:3]
print numbers1
print numbers1[:]

print numbers1[0:10:2]
print '\n---------------�������-------------------'
print [1,2,3]+[4,5,6]
# print [1,2,3]+4
#print ['hello']+'world'
print [1,2,3]+['world']
print '\n---------------�������-------------------'
sequence = [None]*10
print sequence

print '\n---------------��Ա���-------------------'
permissions = 'rwct'
print 'w' in permissions

colors = ['blue','yellow','brown','red','black']
print 'blue' in colors
print 'white' in colors
print '\n---------------����+��С���ֵ-------------------'
numbers = [100,2,56]
print '����Ϊ��' ,len(numbers)
print '��СֵΪ��',min(numbers)
print '���ֵΪ��',max(numbers)



print '\n---------------����-------------------'
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

print '\n---------------�б�-------------------'
print list('python')
seq = ['I','am','a','teacher','a']
seq1 = ['You','are','a','student'] 
print seq
seq.append('student')
print seq
print seq.count('a')
seq.extend(seq1)
print seq

print '\n---------------�б�-------------------'
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
x.sort(key=len) #�Գ���lenΪ�ؼ��ʽ�������
print x

num=[5,3,5,72,1,4]
num.sort(reverse=True)    #�����ҷ�ת
print num