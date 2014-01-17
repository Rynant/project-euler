# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:14:00 2013

@author: rgrant
"""
raise Exception('Not complete')

def answer():
    w = 2
    h = 2
    count = 0
    for i in range(w):
        for j in range(h):
            count += (w)*(h)//2
            
    return count

if __name__=='__main__':
    print(answer())