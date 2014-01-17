# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:07:18 2013

@author: rgrant
"""
def answer():
    count = 0
    for n in range(1,10):
        for p in range (1,30):
            if len(str(n**p)) == p:
                count += 1
                
    return count

if __name__=='__main__':
    print(answer())