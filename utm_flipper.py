# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:35:19 2016

@author: u0084676
"""

import utm
import numpy
import sys
import os

year='2016'
extention='.csv'
filename=year+extention

idstore=[]
xstore=[]
ystore=[]
utmstore=[]
unew=[]
with open(filename, "rt") as f:
    next(f)
    for line in f:
#        [line.rstrip('\n') for line in f]
        idnum = line.split(',')[1]
        x = float(line.split(',')[2])
        y = float(line.split(',')[3])
        idstore.append(id)
        xstore.append(x)
        ystore.append(y) #http://stackoverflow.com/questions/5653533/indexerror-list-assignment-index-out-of-range
        u = utm.from_latlon(y,x)
        u=list(u[0:2])
        u.append(idnum)
        utmstore.append(u)

        
"""
writing the text file with ID, X_utm, Y_utm 
"""

fexp = open(year+'_utm_converted.txt', 'w')
for t in utmstore:
    line = ' '.join(str(x) for x in t)
    fexp.write(line + '\n')
fexp.close()