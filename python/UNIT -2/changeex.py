import os
import sys

mainex = input("enter extantion that you want to change :")
fromex = input("enter current files extantion :")
folder = './'
for filename in os.listdir(folder):
    if filename == "changeex.py":
        pass
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace(fromex, mainex)
    output = os.rename(infilename, newname)