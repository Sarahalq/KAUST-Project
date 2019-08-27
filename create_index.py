#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:17:06 2017

@author: qabbaasa
"""
with open('index.txt','w') as f:
    for i in range(1,893):
        f.write('{0:04d}'.format(i)+'\n')