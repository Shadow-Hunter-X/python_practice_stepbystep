import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

#fig,axs=plt.subplots()

fig.set_figheight(7)
fig.set_figwidth(10)


x=np.linspace(-2, 2, 24)
y1=np.tan(x)
y2=-np.tan(x)
art_1=ax1.plot(x,y1,'b')
ax1.set_xlabel('X for both tan and -tan')
ax1.set_ylabel('Y values for tax')
ax11 = ax1.twinx() 
art_11=ax11.plot(x, y2, 'r')
ax11.set_xlim([0, np.e])
ax11.set_ylabel('Y values for -tan')


y = np.random.randn(1000)
art_2=ax2.hist(y,16)

a = np.arange(0, 5, 0.3)
b = np.exp(-a)
e1 = 0.1 * np.abs(np.random.randn(len(b)))
art_3=ax3.errorbar(a,b,yerr=e1, fmt='.-')

art_4=ax4.pie([45, 35, 20],labels=['seafood', 'drink', 'vegetables'])

plt.subplots_adjust(wspace=0.5,hspace=0.4)


import matplotlib
print isinstance(fig,  matplotlib.artist.Artist)
print isinstance(ax1,  matplotlib.artist.Artist)
print isinstance(art_3,matplotlib.artist.Artist)
print str(fig.get_contains)
print plt.gcf().get_axes()
print type(fig.artists.count)
print fig.bbox
plt.show()

