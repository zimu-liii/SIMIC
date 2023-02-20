# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:51:40 2023

@author: muzi
"""

import json
import matplotlib.pyplot as plt

from simic.encode.main import main as encode
from simic.decode.main import main as decode

#StrandIndependentMatrixImageCoding
class SIMIC:
     
     #encode&decode function and receive input of python datatype
     def encode(self,img):
         return encode(img)
     
     def decode(self,sequences):
         return decode(sequences)
     
     #encode&decode function but receive input of a file
     def encode_file(self,file):
         return encode(getdata(file,'encode'))
      
     def decode_file(self,file):
         return decode(getdata(file,'decode')) 
     
     #show the decoded image
     def show(self,list_byte):
         plt.imshow(list_byte,cmap='gray')
         return
     
     #save the decoded image
     def save(self,list_byte,filename):
         plt.imsave(filename,list_byte,cmap='gray')
         return

#file-preprocessing: expecting option == 'encode' or 'decode'
def getdata(file_path,option):
    
    def img_file(file_path): #excepting an img file in any format
        return plt.imread(file_path)

    def sequence_file(file_path): #excepting a .json format
        with open(file_path,'r') as f:
            return json.load(f)
        
    if option == 'encode':
        return img_file(file_path)
    if option == 'decode':
        return sequence_file(file_path)
    else:
        raise Exception('Illegal option: please choose encode or decode')
