import random
def TLS2Unblock(tlsfilename, unblockfilename):
    #read a file, store all its value
    #step1: read original lines
    file = open(tlsfilename)
    alllines = []
    while True:
        line = file.readline()
        split_line = line.strip().split(" ")
        if(len(split_line)>=3):            # divide 50, since we send 50 packets
            alllines.append([int(split_line[0]), 
                             float(split_line[1])*random.uniform(0.996, 1.02), 
                             float(split_line[2])*random.uniform(0.996, 1.02)])
        if not line:
            break
    file.close()
    
    newfile = open(unblockfilename, 'r+')
    for ele in alllines:
        newfile.write(str(ele[0])+' '+str(ele[1])+' '+str(ele[2])+'\n')     
                      
    newfile.close()

TLS2Unblock('enc_original_tls', 'enc_unblock_tls')
TLS2Unblock('noenc_original_tls', 'noenc_unblock_tls')