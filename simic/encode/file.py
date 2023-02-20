# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 09:16:43 2022

@author: muzi
"""

'''
    This module is for file preprocessing:
    regroup an image matrix of 8bits into 9bits.
'''

#regroup: 8bit to 9bit
def regroup(img):
    bitlist = []
    for i in img:
        
        bits = ''
        for j in i:
            bit = bin(j)[2:]
            while len(bit) < 8:
                bit = '0' + bit
            bits = bits + bit
        if len(bits)%162 != 0:
            if bits[-1] == '1':
                while len(bits)%162 != 0:
                    bits = bits + '0'
            elif bits[-1] == '0':
                while len(bits)%162 != 0:
                    bits = bits + '1'
        
        bitl = [bits[i:i+9] for i in range(0,len(bits),9)]
        
        bitlist.append(bitl)
    return bitlist
