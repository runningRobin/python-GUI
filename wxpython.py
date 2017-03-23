# -*- coding:utf-8 -*-

import sys
import urllib2,re,random
import wx
reload(sys)
sys.setdefaultencoding( "utf-8" )


def start(event):
	headers = [
    'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
    'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
    'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)']
	header = {"User-Agent": random.choice(headers)}
	url = filename.GetValue()
	req = urllib2.Request(url, headers=header)
	html = urllib2.urlopen(req).read().decode('utf-8')

	reg = re.compile(r'<div class="content">\s+<span>(.*?)</span>\s+</div>')
	jokes = re.findall(reg, html)
	jokes_str = ''
	for joke in jokes:
		jokes_str += joke + '\n\n'
	print jokes_str
	contents.SetValue(jokes_str)


app = wx.App()
win = wx.Frame(None, title='Simpl Editor', size=(800, 600))
bkg = wx.Panel(win)

startButton = wx.Button(bkg, label='Start')
startButton.Bind(wx.EVT_BUTTON, start)
filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(startButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL , border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()
