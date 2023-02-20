# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:45:26 2022

@author: muzi
"""

#In-row operation

#5nt to 9bit
from simic.jotating.dejotating import main as segment

#90nt to 5nt
def to5(dna2):
    list30 = []
    for i in dna2:
        list30.append(i[0:30])
        list30.append(i[30:60])
        list30.append(i[60:90])
        
    list5 = []
    for i in list30:
        list5.append(i[0:5])
        list5.append(i[5:10])
        list5.append(i[10:15])
        list5.append(i[15:20])
        list5.append(i[20:25])
        list5.append(i[25:30])
    
    return list5

#9bits list to 8bits list
def tobyte(bytelist9):
    
    listbit = []
    for i in bytelist9:
        b = bin(i)[2:]
        while len(b) < 9:
            b = '0' + b
        listbit.append(b)
    
    bit = ''
    for i in listbit:
        bit = bit + i 
    if bit[-1] == '0':
        while bit[-1]=='0':
            bit = bit[:-1]
    elif bit[-1] == '1':
        while bit[-1]=='1':
            bit = bit[:-1]
    while len(bit)%8!=0:
        bit = bit +'0'
    
    bitlist8 = []
    for i in range(0,len(bit),8):
        bitlist8.append(bit[i:i+8])
    
    bytelist = [int(i,2) for i in bitlist8]
    return bytelist

def main(dna2):
    list5 = to5(dna2)
    list9 = [segment(i) for i in list5]
    bytelist = tobyte(list9)
    return bytelist