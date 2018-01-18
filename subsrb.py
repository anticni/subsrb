 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from Tkinter import Tk
from tkFileDialog import askopenfilename
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
file = askopenfilename() # show an "Open" dialog box and return the path to the selected file

f = open(file, 'r')
linelist = f.readlines()
f.close

f2 = open(file, 'w')
for line in linelist:
    line = line.replace('č', 'c').replace('ć','c').replace('ž','z').replace('š','s').replace('đ','dj').replace('Š','S').replace('Č','C').replace('Ć','C').replace('Đ','DJ').replace('Ž','Z').replace('\xc3\x90','Dj').replace('\xc3\xb0','dj').replace('\xc3\xa8','c').replace('\xc3\x88','C').replace('\xc3\xa6','c').replace('\xc3\x86','C')
    f2.write(line)
f2.close()


