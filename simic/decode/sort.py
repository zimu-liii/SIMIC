# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:30:36 2022

@author: muzi
"""

'''
    When you get the sequencing results (input a list of DNA sequences)
    you can use this mudule to recover the order of sequences in the origin matrix,
    and a single cell in the matrix contains a 90nt DNA (removing adaptor and index from 141nt DNA).
'''

from simic.jotating.dejotating import main as segment

#The adaptor-removing process is not necessary according to whether
#your sequencing results contains the adaptor part or not.
#Normally, the sequencing result from companies are adaptor-free, 
#thus this function is more used when testing the encoding program with the adaptor-adding process.
def remove_adaptor(seqlist141):
    dna = [i[20:-21] for i in seqlist141]
    return dna

#Sort by the index
def sort(dna):
    dna2 = {}
    for i in dna:
        index1 = segment(i[-10:-5])
        if index1 not in dna2:
            dna2[index1] = [i[:-10]+i[-5:]]
        if index1 in dna2:
            dna2[index1].append(i[:-10]+i[-5:])
    
    for j in dna2:
        dna1 = {}
        for k in dna2[j]:
            index2 = segment(k[-5:])
            dna1[index2] = k[:-5]   
        #fill the missing part to ensure the legality of the recovered matrix
        for n in range(max(dna1)+1):
            if n not in dna1:
                dna1[n] = 'ACAAC'*18
        dna2[j] = dna1
    
    return dna2

#dict to list    
def tolist(dna2):   
    dna2list = []
    for i in range(len(dna2)):
        dna2list_row = []
        for j in range(len(dna2[i])):
            dna2list_row.append(dna2[i][j])
        dna2list.append(dna2list_row)
    
    return dna2list

def main(seqlist141):
    '''dna = remove_adaptor(seqlist141)
    dna2 = sort(dna)'''
    dna2 = sort(seqlist141)
    dna2list = tolist(dna2)
    return dna2list