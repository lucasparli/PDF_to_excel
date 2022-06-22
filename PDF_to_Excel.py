# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:03:11 2022

@author: lpa
"""

"""
THIS CODE LOOKS THROUGH ALL FOLDERS AND SEARCHES FOR PDF FILES TO BE CONVERTED INTO EXCEL FILES
"""
import os
from os import walk


#THIS PIECE OF CODE LISTS ALL FILES IN EACH FOLDER, SUBFOLDER, ETC.
path ="C:/Users\lpa\Desktop\Lehren"
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))

#print all the file names
#for name in filelist:
#    print(name)
    
#print(filelist)
    
    
# THIS PIECE OF CODE SORTS ALL FILES THAT CONTAIN "BOM" IN THEIR PATH

shortlist = []

for path in filelist:
    if "BOM" in path:
        shortlist.append(path)
        
for name in shortlist:
    print(name)
        
#print(shortlist)
