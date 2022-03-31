#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

filename=str(sys.argv[1])
old_force=str('{: >4}'.format(sys.argv[2]))
new_force=str('{: >4}'.format(sys.argv[3]))
print ('A total of 3 parameters are required. The first parameter is the file name to be modified; the second parameter is the original restrain force; the third parameter is the new restrain force.')


if (int(old_force) == 0):
   if (int(new_force) != 1000):
      print('Something is wrong for parameters')
      sys.exit()
else:
   if (int(old_force) == 10):   
      if (int(old_force)/(int(new_force)+1) !=10):
         print('Something is wrong for parameters')
         sys.exit() 
   else:
      if (int(old_force)/int(new_force) !=10):
         print('Something is wrong for parameters')
         sys.exit()

if os.path.exists("rzp.itp"):
   os.remove("rzp.itp")

f = open(filename, 'r')
constra=f.read()
con_list=constra.split('\n')
for line in range(0,len(con_list)-1):
    #print(con_list[line])
    f2 = open("rzp.itp", "a")
    f2.write(con_list[line]+"\n")
    f2.close()
    if ('; atom' in con_list[line]): 
        start=line+1
        break


for line in range(start,len(con_list)-1): 
    con_row=con_list[line].split('     ')
    if (len(con_row)==3):
       con_row[2]=con_row[2].replace(old_force,new_force)
       f2 = open("rzp.itp", "a")
       f2.write("     "+con_row[0]+con_row[1]+"     "+con_row[2]+"\n")
       f2.close()
    if (len(con_row)==5):
       con_row[2]=con_row[2].replace(str(int(old_force)),new_force)
       con_row[3]=con_row[3].replace(str(int(old_force)),new_force)
       con_row[4]=con_row[4].replace(str(int(old_force)),new_force)
       f2 = open("rzp.itp", "a")
       f2.write(con_row[0]+"     "+con_row[1]+"  "+con_row[2]+"  "+con_row[3]+"  "+con_row[4]+"\n")
       f2.close()    
    if (len(con_row)==6):
       con_row[3]=con_row[3].replace(str(int(old_force)),new_force)
       con_row[4]=con_row[4].replace(str(int(old_force)),new_force)
       con_row[5]=con_row[5].replace(str(int(old_force)),new_force)
       f2 = open("rzp.itp", "a")
       f2.write("     "+con_row[1]+"     "+con_row[2]+"  "+con_row[3]+"  "+con_row[4]+"  "+con_row[5]+"\n")
       f2.close()   
    if (len(con_row)==2):
       con_row[1]=con_row[1].replace(old_force,new_force)
       f2 = open("rzp.itp", "a")
       f2.write(con_row[0]+"     "+con_row[1]+"\n")
       f2.close()


os.remove(filename)
os.rename("rzp.itp",filename)


