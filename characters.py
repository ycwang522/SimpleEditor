#coding: cp936
'''
Created on 2016��10��25��
@author: iPC
'''
print '---------------�ַ�����ʽ��-------------------'
format='Pi with three decimals: %.9f'
from math import pi
print format %pi

print '%010.3f' %pi
print '%10f' %pi
print '%.3f' %pi
print '%10.5s' %'string is a good tool'
print '---------------�ַ�����ʽ��join����-------------------'
seq1 = ['1','5','5','7']
sep1 = '+'
dr = sep1.join(seq1)
print dr


seq=['1','2','3','4','5']
sep='+'
sep.join(seq)

print 'This is a string'.replace('is','ezz')
print '1+2+3+4+5'.split('+')
print '                      International     '.strip()
