# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 10:51:52 2022

@author: muzi
"""

'''
    This module is the main function for the encode package.
    It is used for encoding an image file into a list of 141nt DNA sequences.
'''

#import os
#os.chdir('../..')

from simic.encode.file import regroup
from simic.jotating.jotating import main as segment
from simic.encode.merge import main as merge


def main(img):
    
    bitlist = regroup(img)
    
    ntlist = []
    for i in bitlist:
        ntlist.append([segment(j) for j in i])
    
    seqlist_whole = []
    for i in range(len(ntlist)):
        seqlist141 = merge(ntlist[i],i)
        for j in seqlist141:
            seqlist_whole.append(j)
    
    return seqlist_whole
