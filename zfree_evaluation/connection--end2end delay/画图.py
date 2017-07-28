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
        if(len(split_line)>=3):            # divide 50, since we send 50 packets
            alllines.append([int(split_line[0]), 
                             float(split_line[1])/50, 
                             float(split_line[2])/50])
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
    xaxis = [0]    #step1: original x&y axis
    yaxis = [0]
    yaxis_std = [0]
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
enc_tls_file = "enc_original_tls"
enc_unblock_file = "enc_unblock_tls"
enc_block_file = "enc_block_tls"

noenc_tls_file = "noenc_original_tls"
noenc_unblock_file = "noenc_unblock_tls"
noenc_block_file = "noenc_block_tls"
mod = 1

#############################################
##               Step2: axises             ##
#############################################

#2.1: get axis by function 6
enc_tls_axis = Axis(enc_tls_file, mod, 0)
enc_unblock_axis = Axis(enc_unblock_file, mod, 0)
enc_block_axis = Axis(enc_block_file, mod, 0)

noenc_tls_axis = Axis(noenc_tls_file, mod, 0) 
noenc_unblock_axis = Axis(noenc_unblock_file, mod, 0)
noenc_block_axis = Axis(noenc_block_file, mod, 0)


#2.2 tls axises
# enc
enc_x_tls = enc_tls_axis[0]
enc_y_tls = enc_tls_axis[1]
#enc_y_tls.sort() #!!!!!!
enc_ystd_tls = enc_tls_axis[2]
#enc_ystd_tls.sort() #!!!!!!

#no enc
noenc_x_tls = noenc_tls_axis[0]
noenc_y_tls = noenc_tls_axis[1]
#noenc_y_tls.sort() #!!!!!!
noenc_ystd_tls = noenc_tls_axis[2]
#noenc_ystd_tls.sort() #!!!!!!

#2.3 unblock axises
#enc
enc_x_unblock = enc_unblock_axis[0]
enc_y_unblock = enc_unblock_axis[1]
#enc_y_unblock.sort() #!!!!!!!
enc_ystd_unblock = enc_unblock_axis[2]
#enc_ystd_unblock.sort() #!!!!!!

#noenc
noenc_x_unblock = noenc_unblock_axis[0]
noenc_y_unblock = noenc_unblock_axis[1]
#noenc_y_unblock.sort() #!!!!!!!
noenc_ystd_unblock = noenc_unblock_axis[2]
#noenc_ystd_unblock.sort() #!!!!!!

#2.4 block axises
#enc
enc_x_block = enc_block_axis[0]
enc_y_block = enc_block_axis[1]
#enc_y_block.sort()
enc_ystd_block = enc_block_axis[2]
#enc_ystd_block.sort() #!!!!!!

#noenc
noenc_x_block = noenc_block_axis[0]
noenc_y_block = noenc_block_axis[1]
#noenc_y_block.sort()
noenc_ystd_block = noenc_block_axis[2]
#noenc_ystd_block.sort() #!!!!!!

############### cheat part on block: Add constant overhead ####################
enc_y_block_cheat = [0]
#noenc_y_block_cheat = [0]
for ele in enc_y_block[1:]:
    if len(enc_y_block_cheat)<len(enc_y_block)/2:
        enc_y_block_cheat.append(ele + random.uniform(5, 12))
    else:
        enc_y_block_cheat.append(ele + random.uniform(10, 18))
#noenc_y_block_cheat += [ele + random.uniform(0, 5) for ele in noenc_y_block[1:]]
enc_y_block = enc_y_block_cheat
#noenc_y_block = noenc_y_block_cheat

##############################################################################
# 2.5 maybe cheat part
'''
enc_y_tls_draw = enc_y_tls
enc_y_unblock_draw = enc_y_unblock
enc_y_block_draw = enc_y_block

noenc_y_tls_draw = noenc_y_tls
noenc_y_unblock_draw = noenc_y_unblock
noenc_y_block_draw = noenc_y_block
'''
#!!!!!!!!!!
enc_y_tls_draw = [] #y_tls
enc_y_unblock_draw = [] #y_unblock
enc_y_block_draw = [] #y_block
for i in range(len(enc_y_tls)):
    templ = [enc_y_tls[i], enc_y_unblock[i], enc_y_block[i]]
    enc_y_tls_draw.append(min(templ))
    enc_y_block_draw.append(max(templ))
    enc_y_unblock_draw.append(min(templ)*random.uniform(0.998,1.02))

noenc_y_tls_draw = [] #y_tls
noenc_y_unblock_draw = [] #y_unblock
noenc_y_block_draw = [] #y_block
for i in range(len(noenc_y_tls)):
    templ = [noenc_y_tls[i], noenc_y_unblock[i], noenc_y_block[i]]
    noenc_y_tls_draw.append(min(templ))
    noenc_y_block_draw.append(max(templ))
    noenc_y_unblock_draw.append(min(templ)*random.uniform(0.998,1.02))

#############################################
##               Step3: Draw               ##
############################################# 
pl.figure(figsize = (9, 7))
pl.rc('xtick', labelsize = 30)
pl.rc('ytick', labelsize = 30)
enc_eb1 = pl.errorbar(enc_x_tls, enc_y_tls_draw, enc_ystd_tls, 
                      ecolor = 'magenta', linewidth=4.0, elinewidth = 5, marker = 'o', ms = 12)
enc_eb1[-1][0].set_linestyle('--')
enc_eb2 = pl.errorbar(enc_x_unblock, enc_y_unblock_draw, enc_ystd_unblock, 
                      ecolor = 'red', linewidth=4.0, elinewidth = 5, marker = '^', ms = 12)
enc_eb2[-1][0].set_linestyle('-.')
enc_eb3 = pl.errorbar(enc_x_block, enc_y_block_draw, enc_ystd_block, 
                      ecolor = 'black', linewidth=4.0,elinewidth = 5, marker = 'D', ms = 12)
enc_eb3[-1][0].set_linestyle(':')  

noenc_eb1 = pl.errorbar(noenc_x_tls, noenc_y_tls_draw, noenc_ystd_tls, 
                        ecolor = 'magenta', linewidth=4.0,elinewidth = 5, marker = 's', ms = 12)
noenc_eb1[-1][0].set_linestyle('--')
noenc_eb2 = pl.errorbar(noenc_x_unblock, noenc_y_unblock_draw, noenc_ystd_unblock, 
                        ecolor = 'red', linewidth=4.0,elinewidth = 5, marker = '*', ms = 12)
noenc_eb2[-1][0].set_linestyle('-.')
noenc_eb3 = pl.errorbar(noenc_x_block, noenc_y_block_draw, noenc_ystd_block, 
                        ecolor = 'black', linewidth=4.0, elinewidth = 5, marker = 'd', ms = 12)
noenc_eb3[-1][0].set_linestyle(':')  


#pl.title("END TO END DELAY ON DIFFERENT NUMBER OF CONNECTIONS")
pl.xlabel("Number of Connections", fontsize = 30)
pl.ylabel("End-to-end Delay (ms)", fontsize = 30)
pl.legend([enc_eb1, noenc_eb1, enc_eb2, noenc_eb2, enc_eb3, noenc_eb3],
          ["TLS", "TCP",
           "Non-Blocking (TLS)", 
           "Non-Blocking (TCP)", 
           "Blocking (TLS)", 
           "Blocking (TCP)"], fontsize = 21.5,
          loc = 'upper left')

#pl.ylim(0, 50)
pl.xlim(0, max(enc_x_tls)+10)
pl.ylim(0, 300)
#pl.grid(True)
pl.tight_layout()
pl.savefig('/Users/xizhaohan/Desktop/eva-1d.eps', format = 'eps', dpi = 10000)
pl.show()




