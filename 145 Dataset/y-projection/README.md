# Average Spectra (y-projection)

## Overview
This notebook shows the average spectra for each cloud in the data set, "146.h5". These are created by rays projected in the y-direction and moving in the x and z-directions for a number of iterations. The resolution for the spectra is set manually to d&lambda; = 0.01. 

## Projection and Slice Plots
Before plotting the spectra, an yz projection plot is displayed. The grey X indicates the positions where the initial rays are projected and the black X shows where the final rays are located.

Similarly, the positions of the rays through each cloud are depicted by slice plots in the xy and yz planes. The yz plot may look wrong (two very thin lines), but it was determined that this is due to where yt slices the plot. Yt slices its plots down the middle of the domain, in this case, down the x-direction. However, there is a scarce amount of gas at x = 0 kpc (middle of the domain) as shown in the xz projection plot, which results in a yz slice plot composed of two thin lines as opposed to two circular clouds.

## Average Spectra
Next, the average spectra of each cloud for C IV, Ly &alpha;, O I 1302, Si II 1304, C II 1335, Si IV 1393, Al III 1854, Fe II 2600, and Mg II 2796 are plotted. The two uppermost plots for each line present the resulting spectra for each iteration (i.e, each ray) and are topped by a thick black line representing the average of all the spectra shown. The bottom plot compares the average spectrum of the top/right cloud to that of the bottom/left cloud.

## "Weird" Lines
Fe II 2600, Mg II 2796, Si II 1304 (top cloud), C II 1335(top cloud), Si IV 1393, and C IV have iterations that differ significantly from one another.

