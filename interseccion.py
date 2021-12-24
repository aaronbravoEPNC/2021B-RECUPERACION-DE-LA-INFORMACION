# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 11:15:35 2021

@author: Aaron
"""

def opAnd(t1, t2, index):
    res = []
    p1 = None
    p2 = None
    for i in index:
        if(i==t1):
            p1=index[i]
        if(i==t2):
            p2=index[i]
        
    if(p1 != None and p2!= None):                   
        for i in range(1,len(p1)):        
            for j in range(1,len(p2)):            
                if p1[i][0] == p2[j][0]:                    
                    res.append(p1[i][0])
                
    return res

def opOr(t1, t2, index):
    res = []
    p1 = None
    p2 = None
    for i in index:
        if(i==t1):
            p1=index[i]
        if(i==t2):
            p2=index[i]
            
    if(p1 != None):
        for i in range(1,len(p1)):
            res.append(p1[i][0])
    if(p2 != None):
        for i in range(1,len(p2)):
            res.append(p2[i][0])
            
    res = list(set(res))
            
    return res

def opNot(t1, index):
    res = []
    res1 = []
    res2 = []
      
    for i in index:        
        if(i==t1):
            for j in range(1,len(index[i])):
                res1.append(index[i][j][0])
                
        if(i!=t1):
            for j in range(1,len(index[i])):
                res2.append(index[i][j][0])
    
    if(len(res1) <= len(res2)):
        res = list(set(res1)-set(res2))
    else:
        res = list(set(res2)-set(res1))
    
    
    return res

            
            

indice = {"casa": [3, (1,2,[2,16]), (2,5,[1,6,7,20,35]), (4,5,[90,110,209])],
          "la": [2, (1,2,[10,15]), (4,3,[89,109,201])],
          "perro": [2,(1,1,[14]), (4,7,[100,112,211,300,305,406,588])],
          "roja": [2, (1,2,[7,17]), (2,3,[8,28,80]), (4,3,[91,111,120])],
          "verde": [1, (4,5,[101,113,212,301,409])]}


print("AND\n", opAnd("casa", "perro", indice))

print("OR\n", opOr("casa", "perro", indice))

print("NOT\n", opNot("roja", indice))




            
    
    
    
    
    