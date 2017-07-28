# graph (a): machine capability--download time

import numpy as np
import matplotlib.pyplot as pl
import random

#Function1: count median:
def median(L):
    L.sort()
    if(len(L)%2==1): return float(L[int(len(L)/2)])
    else:
        first = L[int(len(L)/2)-1]
        second = L[int(len(L)/2)]
        return float(first+second)/2

    
#Function2: count average
def ave(l):
    newl = []
    for ele in l:
        newl.append(ele)
    newl.remove(max(newl))
    newl.remove(min(newl))
    if len(newl)==0:
        return np.mean(l)
    else:
        return np.mean(newl)


#Function3: standard deviation
def stanDev(l):
    newl = []
    for ele in l:
        newl.append(ele)
    newl.remove(max(newl))
    if len(newl)>0:
        newl.remove(min(newl))
    
    if len(newl)==0:
        return np.std(l)
    else:
        return np.std(newl)

#Function4: read file and get dict, return as dict = {key:[median(or ave), std, max, min]} 
def File2Dict(filename):
    #read a file, store all its value
    #step1: read original lines
    file = open(filename)
    alllines = []
    while True:
        line = file.readline()
        split_line = line.strip().split(" ")
        if(len(split_line)>=3):            
            alllines.append([int(split_line[0]), 
                             float(split_line[1])/1000, 
                             float(split_line[2])/1000])
        if not line:
            break
    file.close()
    #for line in alllines: print(line)

    #step2: separate by first value
    grouplines = {}
    for ele in alllines:
        if(ele[0] not in grouplines):
            grouplines[ele[0]] = []
            grouplines[ele[0]].append(ele[2])
        else:
            grouplines[ele[0]].append(ele[2])
    #print(grouplines)

    #step3: get median
    out = {}
    for key in grouplines:
        out[key] = [float(median(grouplines[key])),
                    float(np.std(grouplines[key]))]
    return out
    

#Function5: count axis, return as res = [[xaxis],[yaxis],
#                                        [yaxis_std]]

def Axis(filename, mod, increment):
    outDict = File2Dict(filename)
    xaxis = []    #step1: original x&y axis
    yaxis = []
    yaxis_std = []
    sortkeys = sorted(outDict.keys())
    for k in sortkeys: xaxis.append(k)
    for x in xaxis: 
        if x>0: yaxis.append(outDict[x][0])
        if x>0: yaxis_std.append(outDict[x][1])
    
    xaxis_new = []  #step2: use mod filter axises, use less axises
    yaxis_new = []
    yaxis_std_new = []
    for i in range(len(xaxis)):
        if i%mod==0: 
            if i==0: xaxis_new.append(xaxis[i])
            else: xaxis_new.append(xaxis[i]+increment)
            yaxis_new.append(yaxis[i])
            yaxis_std_new.append(yaxis_std[i])          
    res = [xaxis_new, yaxis_new, yaxis_std_new]
    
    return res

#############################################
##             Step1: file name            ##
#############################################
#Matplotlib: Draw the line
enc_block_file = "cap"
mod = 1

#############################################
##               Step2: axises             ##
#############################################

#2.1: get axis 
enc_block_axis = Axis(enc_block_file, mod, 0)

#2.2 block axises
#enc
enc_x_block = enc_block_axis[0]
enc_y_block = enc_block_axis[1]
#enc_y_block.sort()
enc_ystd_block = enc_block_axis[2]
#enc_ystd_block.sort() #!!!!!!

# 2.3
enc_y_block_draw = enc_y_block
print(enc_ystd_block)

#############################################
##               Step3: Draw               ##
#############################################  
pl.figure(figsize = (9, 7))
pl.rc('xtick', labelsize = 30)
pl.rc('ytick', labelsize = 30)
enc_eb3 = pl.errorbar(enc_x_block, enc_y_block_draw, enc_ystd_block, 
                      ecolor = 'black', linewidth=4.0, elinewidth = 2, marker = 'D', ms = 12)
enc_eb3[-1][0].set_linestyle(':')  



#pl.title("END TO END DELAY ON DIFFERENT NUMBER OF CONNECTIONS")
pl.xlabel("CPU Capability", fontsize = 30)
pl.ylabel("Download Time (second)", fontsize = 30)
#pl.legend([enc_eb3],["ZFree -- Blocking Mode (Encrypted)"],loc = 'upper right')

pl.xticks(enc_x_block, ['40%', '50%', '60%', '70%', '80%', '90%', '100%'])
pl.xlim(35, 105)
pl.ylim(10.5)
#pl.grid(True)
pl.tight_layout()
pl.savefig('/Users/xizhaohan/Desktop/eva-1c.eps', format = 'eps', dpi = 10000)
pl.show()








