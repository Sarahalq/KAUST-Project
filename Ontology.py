#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:47:13 2017

@author: qabbaasa
"""
#%%
import pronto as pro
ont =pro.Ontology('/home/qabbaasa/Documents/summer_project/data/hp.obo')

#for term in ont:
    #if term.children:
        #print(term)
        
#for term in ont:
  
     
    #print(term)

print(ont['HP:0100744'].children.children)