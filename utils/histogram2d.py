# Example of making a 2-D histogram

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors

def plot(x,y,z):
    # Takes in arrays x,y,z
    # bins them

    # weights by z (for example, for mass-weighting)
    
    # 100 x bins, 101 y bins. The reason I like to keep x and y different is
    # so that the code yells at me when dimensions don't line up
    # which can help avoid subtle mistakes

    # normed=False makes it easier to scale the colorbar appropriate to show whatever units you prefer
    
    hist,xedges,yedges = np.histogram2d(x,y,bins=[100,101],normed=False,weights=z)

    # xedges and yedges are always longer than needed by 1,
    # since N cells have N+1 edges. That's why I truncate xedges[:-1].

    # hist.transpose() is needed to transpose the array. This is one downside of using pcolormesh.

    # norm=matplotlib.colors.LogNorm() normalizes the color in log scale
    
    plt.pcolormesh(xedges[:-1],yedges[:-1],hist.transpose(),norm=matplotlib.colors.LogNorm())
    plt.colorbar()
