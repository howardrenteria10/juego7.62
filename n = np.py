import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0,10)
signal1 = np.array([0, 1, 2, 3 , 4, 6,7,8,9,10])
signal2 = np.array([-3,-2,-1,2,3,4,5,6,7,8])
fig, axs = plt.subplots(3,1,figsize=(7,7))
axs[0].stem(n,signal1)
axs[0].grid(True)

axs[1].stem(n,signal2)
axs[1].grid(True)

conv = np.convolve(signal1,signal2)
n_adap = np.arange(0,19)

axs[2].stem(n_adap,conv)
axs[2].grid(True)
plt.tight_layout()
