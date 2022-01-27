# Overview
Here, I present some side tasks related to my current research in analyzing the dataset '146.h5'. These include making slice plots of the data using matplotlib, 
phase plots with yt, and animations of multiplot figures.

## Matplotlib Slice Plots
I wrote my own slice plot functions in response to limitations in yt's version. Although yt has the option of plotting the density of a specific 
ion as opposed to the whole gas, it only works if the ion density has all non-zero values, otherwise it presents an error due to the logarithmic fashion of 
the colors. This introduces a problem in heavier ions such as Si IV where it is not present all throughout the domain. Matplotlib ignores any log(0) values, 
thus getting rid of the error. Each function may plot a single slice plot of the density of one ion (or of all gas) or multiple slice plots of a given list 
of ions all scaled equally for comparison.

Yt automatically slices the data down the center of the domain and I could not find a way to specify where I want the slice to be. This is a problem when making a 
yz-plot of 146.h5 because most of the gas in the x-direction is found at the extremes and the amount of gas in the middle is scarce. My functions corresponding 
to making xz and yz plots allow me to specify where I want the slice to be. The xy-plot function slices down the middle of the domain by default just as 
it does in yt since this location does not present any issues for this dataset.

#### plt sliceplots functions.ipynb
This notebook creates functions for xy, xz, and yz slice plots and displays examples for various ions.

#### plt sliceplots with ray.ipynb
This notebook creates functions for xy, xz, and yz slice plots and can annotate up to 4 rays through the figure.

#### Matplotlib vs yt.ipynb
In this notebook, I use my own function to create a yz-plot of the density of all gas. I slice it down the middle of the domain and compare the resulting
plot to that drawn by yt to ensure the issue with the plot corresponds to where it is being sliced and not because of a bug in yt.

## Phase Plots
#### yt Phase Plots.ipynb
The goal of this task was for me to learn how to create and customize phase plots using yt. I made rho-temperature phase plots for H I, C IV, and O I. 
The plots on the left, plot all gas and shade the density of a single ion. The plots on the right, plot all gas and shade the mass probability density of 
that specific ion. There are a couple of bugs that need to be resolved. The first being the fact that the title of each subplot assumes the last one given
('O I' in this case). Additionally, the default colorbar label looks a bit awkward. For example, instead of it saying 'H I Density', it displays
'H P0 Density'. I attempted to fix this error, but each subplot assumed 'O I Density' or 'O I Mass Probability Density' regardless of what the represented
ion was.

## Animations
This is what I am currently working on. The goal of this task is to create an animation that shows how the spectra for 146.h5 changes per cell for each ray that 
is projected through the data. This will aid in seeing how and where the spectra changes drastically in certain ions as seen in the Average Specra notebooks.

#### Animation Project II.ipynb and project2.mp4
This is a test animation and its corresponding code. The top panel shows a slice plot of 146.h5 with rays ranging across it and the bottom plot displays 
the function, y = x. The goal of this task was for me to learn how to create an animation with two subplots and how to clear a ray and redrawing a new one
without clearing the whole figure. Therefore, the location of each ray and the function plotted in the bottom plot have no physical significance.
