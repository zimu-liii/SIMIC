# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 09:54:25 2022

@author: muzi
"""

#import os
#os.chdir('../..')

from simic.decode.sort import main as sort
from simic.decode.matrix import main as matrix

def main(seqlist141):
    dna2list = sort(seqlist141)
    list_byte = matrix(dna2list)
    return list_byte
