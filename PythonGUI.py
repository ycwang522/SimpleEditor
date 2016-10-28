#coding:utf-8
'''
Created on 2016��10��27��

@author: iPC
'''
from Tkconstants import VERTICAL
'''
import wx
app=wx.App()
win=wx.Frame(None,title="simple Editor",size=(410,335))
win.Show()
loadButton=wx.Button(win,label='Open',pos=(225,5),size=(80,25))
saveButton=wx.Button(win,label="Save",pos=(315,5),size=(80,25))
filename=wx.TextCtrl(win,pos=(5,5),size=(210,25))
context=wx.TextCtrl(win,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE | wx.HSCROLL)
app.MainLoop()
'''

import wx

def load(event):
    file=open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()
    
def save(event):
    file=open(filename.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()
    

app=wx.App()
win=wx.Frame(None,title='Siple Editor',size=(410,335))

bkg=wx.Panel(win)

loadButton = wx.Button(bkg,label='Open')
loadButton.Bind(wx.EVT_BUTTON,load)


SaveButton = wx.Button(bkg,label='Save')
SaveButton.Bind(wx.EVT_BUTTON,save)


filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)

hbox=wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(SaveButton,proportion=0,flag=wx.LEFT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()













