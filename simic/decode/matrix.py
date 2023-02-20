# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 15:12:15 2022

@author: muzi
"""

#Matrix operation based on the in-row operation

from simic.decode.line import main as line

def matrix(dna2list):
    list_byte = []
    for k in dna2list:
        list_byte.append(line(k))
    return list_byte

#check if list_decode is illegal
def matrix_check(list_byte):
    len_list = []
    for i in list_byte:
        len_list.append(len(i))
    lenmax = max(len_list)
    for i in list_byte:
        while len(i) != lenmax:
            i.append(0)
    return

def main(dna2list):
    list_byte = matrix(dna2list)
    matrix_check(list_byte)
    return list_byte