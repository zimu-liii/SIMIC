# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:51:22 2022

@author: muzi
"""

'''
    This module is to build 141nt DNA strands 
    by merging 18×5nt, index and adaptor.
'''

from simic.jotating.jotating import main as segment

#18×5nt=90nt
def merge_nt(seqlist5):
    
    seqlist30 = []
    for i in range(0,len(seqlist5),6):
        seqlist30.append(seqlist5[i]+seqlist5[i+1]+seqlist5[i+2]+seqlist5[i+3]+seqlist5[i+4]+seqlist5[i+5])
    
    seqlist90 = []
    for i in range(0,len(seqlist30),3):
        seqlist90.append(seqlist30[i]+seqlist30[i+1]+seqlist30[i+2])
    
    return seqlist90

#add index
def add_index(seqlist90,row):
    
    ##Index is composed of both row index and column index
    def index(i,j):
        
            i2 = bin(i)[2:]
            while len(i2) < 9:
                i2 = '0' + i2
            ri2 = segment(i2)
            
            j2 = bin(j)[2:]
            while len(j2) < 9:
                j2 = '0' + j2
            rj2 = segment(j2)
            
            return ri2+rj2
    
    seqlist100 = []
    for i in range(len(seqlist90)):
        seqlist100.append(seqlist90[i]+index(row,i))
  
    return seqlist100

#add adaptor
def add_adaptor(seqlist105):
    
    adaptor1 = 'ACACGACGCTCTTCCGATCT' #20nt
    adaptor2 = 'AGATCGGAAGAGCACACGTCT' #21nt
    
    seqlist141 = [adaptor1+i+adaptor2 for i in seqlist105] 
    return seqlist141

def main(seqlist5,row):
    seqlist90 = merge_nt(seqlist5)
    seqlist100 = add_index(seqlist90,row)
    seqlist141 = add_adaptor(seqlist100)
    return seqlist141

