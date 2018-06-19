import numpy as np
import netCDF4 as nc



fil_dir = '/Users/elizabethdrenkard/external_data/analytical_tracmass/'
fil_bas = 'test_2010_01-'

vel_val = 0.014

for nt in range(10):
    ncfil = fil_dir + fil_bas + str(nt+1).zfill(2) + '.nc'
    fid = nc.Dataset(ncfil,'a')
    if ((nt > 1) & (nt < 4)):
       fid.variables['u'][:] = 0.
       fid.variables['v'][:] = vel_val
    elif ((nt > 3) & (nt < 6)):
       fid.variables['u'][:] = -1*vel_val
       fid.variables['v'][:] = 0.
    elif ((nt > 5) & (nt < 8)):
       fid.variables['u'][:] = 0
       fid.variables['v'][:] = -1*vel_val
       if nt == 7:
          ncfil2 = fil_dir + 'test_2009_12-31.nc'
          fid2   = nc.Dataset(ncfil2,'a')
          fid2.variables['u'][:] = 0. 
          fid2.variables['v'][:] = -1*vel_val
    else:
        u = fid.variables['u'][:] = vel_val
        v = fid.variables['v'][:] = 0.

    fid.close
    print 'MEEP', nt



