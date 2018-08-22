# this is a Python script that takes in binary output from TRACMASS,
# reads it, and spits out its contents

# NOTE: COMMENTED OUT CURSOR LINES IN BACKEND FILE: 
# /opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/matplotlib/backends/backend_agg.py  
# OTHERWISE WON'T SAVE GIF ANIMATION

import pytraj
import pandas
import numpy as np

#~~~~~~~~REPLACE FILENAME HERE~~~~~~~#
outdatadir = '/Users/elizabethdrenkard/external_data/analytical_tracmass/analytical/20100101-1200/'
filename = 'test_analytical_run.bin'
#(CASENAME, PROJECTNAME) :: Initiates pytraj
tr = pytraj.Trm('analytical','analytical')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
referencefile = str(outdatadir + filename)

#Load the file(s) 
data1 = pandas.DataFrame(tr.readfile(referencefile))

print type(data1)

#Adjust columns in the dataframes
data1 = data1.loc[:,['ntrac','ints','x','y']]


print data1

#Change to numpy array
data2 = pandas.DataFrame.as_matrix(data1)
print data2.shape
print 'NPART=',np.max(data2[:,0])
print 'First day=', np.min(data2[:,1])

print np.where(data2[:,0]==1)[0]

# TESTING SPECIFIC TRACERS

#for j in range(data2.shape[0]):
#    print data2[j,1], data2[j,2], data2[j,3]


#Determine number of steps and which particles they contain
data_dif = np.diff(data2[:,0])
istep = (np.where(data_dif<1)[0])+1
istep = np.append([0],istep)
nstep = len(istep)
print 'NSTEP =', nstep



# NOTE: The ini.bin file contains the initial date (ints) and 
#        location of all seeded particles
# 	

# NOTE: The kll.bin file contains the positions and dates when
#       where/when particles are killed (i.e., hit boundaries
#       or time limit. At least one of the coordinates recorded
#       is the boundary that is that of the killzone
