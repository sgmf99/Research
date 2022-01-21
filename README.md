# Average Spectra (x-projection)

## Overview
This notebook shows the average spectra for each cloud in the data set, "146.h5". These are created by rays projected in the x-direction and moving in the y and z-directions for a number of iterations. The resolution for the spectra is set manually to d&lambda; = 0.01. 

## Projection and Slice Plots
Before plotting the spectra, an yz projection plot is displayed. The grey X's indicate the positions where the initial rays are projected and the black X's show where the final rays are located.

Similarly, the positions of the rays through each cloud are depicted by slice plots in the xy and xz planes.

## Average Spectra
Next, the average spectra of each cloud for C IV, Ly &alpha;, O I 1302, Si II 1304, C II 1335, Si IV 1393, Al III 1854, Fe II 2600, and Mg II 2796 are plotted. The two uppermost plots for each line present the resulting spectra for each iteration (i.e, each ray) and are topped by a thick black line representing the average of all the spectra shown. The bottom plot compares the average spectrum of the top/right cloud to that of the bottom/left cloud.

## "Weird" Lines
Fe II 2600, Mg II 2796, O I 1302, and C IV have iterations that differ significantly from one another.
