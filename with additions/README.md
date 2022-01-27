# Average Spectra With Additions (x-projection)
These notebooks calculate the average spectra from an array of rays projected in the x-direction and add things such as redshift, Gaussian noise, 
Milky Way foreground, and quasar foreground.

#### Average Spectra COS cleaner.ipynb
The spectra in this notebook are made using Cosmic Origins Spectrograph (COS) instruments. Therefore, the wavelength range is confined to that of the instrument, limiting the overall field of view. This presents problems when plotting spectra at big redshifts.

#### Average Spectra with additions.ipynb
This notebook performs the same calculations on C IV as the ones in the previous one, but the wavelength range and resolution are set manually. This allows for a better analysis of the different functions Trident provides. It is found that redshifting a ray flips the shape of the spectral line. Adding an observing redshift on the other hand, keeps the same overall shape of the line, but blueshifts it instead.

Some plots contain a manual offset. This is made for comparing the shape of a line to the shape of the same spectrum redshifted. It is a way of 'zooming in' while keeping both lines in the same plot.
