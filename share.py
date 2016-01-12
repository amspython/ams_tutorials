import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# the random data
x = np.random.randn(1000)
y = np.random.randn(1000)
# now determine nice limits by hand:
binwidth = 0.25
xymax = np.max([np.max(np.fabs(x)), np.max(np.fabs(y))])
lim = (int(xymax/binwidth) + 1)*binwidth
bins = np.arange(-lim, lim + binwidth, binwidth)

fig = plt.figure()

gs = gridspec.GridSpec(3,3)


axh = fig.add_subplot(gs[0,:2])
axh.hist(x, bins=bins)


axy = fig.add_subplot(gs[1:,2])
axy.hist(y, bins=bins, 
    orientation='horizontal')

ax = fig.add_subplot(gs[1:,:2], 
    sharex=axh, sharey=axy)
ax.scatter(x,y)

plt.show()