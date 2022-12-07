
import numpy as np
from astropy.io import fits

imglist = ['fits/rosat_pspc_rdf2_3_im2.fits', 'fits/rosat_pspc_rdf2_3_bk1.fits', 'fits/rosat_pspc_rdf2_3_bk1.fits']
data = []
for img in imglist:
    hdulist = fits.open(img)
    data.append(hdulist[0].data)
data = np.array(data)
data = np.dstack(data)

