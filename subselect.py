import numpy as np
import matplotlib.pylab as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.colors import LogNorm

#see https://github.com/pynbody/pynbody for installation
import pynbody
import pynbody.plot.sph as sph

#see https://bitbucket.org/yymao/helpers/src/master/ for installation
from helpers.SimulationAnalysis import readHlist

def subselect(cdm_halos, sidm_halos, f_cdm, f_short_cdm, f_sidm, f_short_sidm ):
   # snapshot=["%03d" % x for x in range(236)]
   # for i in range(236):
       # assert(np.argmax(cdm_halos[snapshot[i]]['mvir'])==0)
       # assert(np.argmax(sidm_halos[snapshot[i]]['Mvir'])==0)

    distance_cut=100.
    projection_thickness=2.
    Mpc_to_kpc=1000.

   
    
    for key in f_cdm.keys():
        print("subselecting " + key + " for cdm")
        xdist = f_cdm[key]['pos'][:,0]-cdm_halos[key][0]['x']
        ydist = f_cdm[key]['pos'][:,1]-cdm_halos[key][0]['y']
        zdist = f_cdm[key]['pos'][:,2]-cdm_halos[key][0]['z']
        dist = Mpc_to_kpc*np.sqrt(xdist**2+ydist**2+zdist**2)/f_cdm[key].properties['h']
        f_short_cdm[key] = f_cdm[key][(dist<distance_cut) & (np.abs(zdist)<projection_thickness)]

    for key in f_sidm.keys():
        print("subselecting " + key + " for sidm")
        xdist = f_sidm[key]['pos'][:,0]-sidm_halos[key][0]['x']
        ydist = f_sidm[key]['pos'][:,1]-sidm_halos[key][0]['y']
        zdist = f_sidm[key]['pos'][:,2]-sidm_halos[key][0]['z']
        dist = Mpc_to_kpc*np.sqrt(xdist**2+ydist**2+zdist**2)/f_sidm[key].properties['h']
        f_short_sidm[key] = f_sidm[key][(dist<distance_cut) & (np.abs(zdist)<projection_thickness)]

     

    