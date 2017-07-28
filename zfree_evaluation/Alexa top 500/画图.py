import numpy as np
import matplotlib.pyplot as pl

def File2Axis(filename):
    x_old = list(np.loadtxt(filename))
    x = sorted([ele/1000 for ele in x_old])
    y = []
    cur = 1.0/(len(x))
    for i in range(len(x)):
        y.append(cur)
        cur = cur + (1.0/(len(x)))
    return [x_old, x, y]

x_tls_old = File2Axis('original_tls')[0]
x_unblock_old = File2Axis('unblock_tls')[0]
x_block_old = File2Axis('block_tls')[0]

x_tls = File2Axis('original_tls')[1]
x_unblock = File2Axis('unblock_tls')[1]
x_block = File2Axis('block_tls')[1]

print(len(x_tls), len(x_unblock), len(x_block))

y_tls = File2Axis('original_tls')[2]
y_unblock = File2Axis('unblock_tls')[2]
y_block = File2Axis('block_tls')[2] 

################### Section1: data ####################
block_overhead = []
unblock_overhead = []
for i in range(len(x_tls)):
    block_overhead.append((x_block_old[i]-x_tls_old[i])/x_tls_old[i])
    unblock_overhead.append((x_unblock_old[i]-x_tls_old[i])/(2*x_tls_old[i]))
    #print(x_block_old[i]-x_tls_old[i], '\t',x_unblock_old[i]-x_tls_old[i], '\t',  x_tls_old[i])
print("Block median overhead is: " ,np.median(block_overhead))
print("Unblock median overhead is: " ,np.median(unblock_overhead))

################### Section2: graph ####################

pl.figure(figsize=(9,7))
pl.rc('xtick', labelsize = 30) 
pl.rc('ytick', labelsize = 30) 
line1, = pl.plot(x_tls, y_tls, 'b--', linewidth=4.0)
line2, = pl.plot(x_unblock, y_unblock, 'g:', linewidth=5.0)
line3, = pl.plot(x_block, y_block, 'r-', linewidth=4.0)

#pl.title("ALEAX TOP 500 LOADING TIME DISTRIBUTION")
pl.xlabel("Loading Time (second)", fontsize = 30)
pl.ylabel("Cumulative Probability", fontsize = 30)

pl.legend([line1, line2, line3],["Normal Access", "Non-Blocking","Blocking"],
          loc = 'lower right',
          fontsize = 22)  

pl.ylim(0, 1.0)
pl.tight_layout()
pl.savefig('/Users/xizhaohan/Desktop/eva-1a.eps', format='eps', dpi=10000)    
pl.show()


