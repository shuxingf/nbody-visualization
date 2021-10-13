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

def plot_snapshot(snapshot, f_short_cdm, cdm_halos, cdm_subhalos, f_short_sidm, sidm_halos, sidm_subhalos):
    #snapshot=["%03d" % x for x in range(10)]
    for i in range(len(snapshot)):
        print("plotting i = " + snapshot[i])
        plt.figure(figsize=(12,12))

        plt.subplot(111)

        plt.scatter(f_short_cdm[snapshot[i]]['pos'][:,0],
                f_short_cdm[snapshot[i]]['pos'][:,1],s=0.01,alpha=0.1,c='k')

        mw = plt.scatter(cdm_halos[snapshot[i]][0]['x'], cdm_halos[snapshot[i]][0]['y'], 
                     s=100, marker='*',label=r'$\mathrm{MW}$',color='gold')
        try:
            lmc = plt.scatter(cdm_subhalos[snapshot[i]][0]['x'], cdm_subhalos[snapshot[i]][0]['y'],
                      s=100,marker='*',label=r'$\mathrm{LMC}$',color='magenta')
        except:
            pass

        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()

        plt.title(r'$\mathrm{CDM}$',fontsize=30)
        try:
            plt.legend(loc=2,handles=[mw,lmc],fontsize=20,frameon=False)
        except:
            pass

        plt.axis('off')

        plt.tight_layout()
    
        print("save cdm_visualization" + snapshot[i])
        plt.savefig("/home1/shuxingf/nbody-visualization/cdm_visualization/cdm_visualization" + snapshot[i] + ".png")

        plt.figure(figsize=(12,12))

        plt.subplot(111)

        plt.scatter(f_short_sidm[snapshot[i]]['pos'][:,0],
            f_short_sidm[snapshot[i]]['pos'][:,1],s=0.01,alpha=0.1,c='k')

        mw = plt.scatter(sidm_halos[snapshot[i]][0]['x'], sidm_halos[snapshot[i]][0]['y'], 
                 s=100, marker='*',label=r'$\mathrm{MW}$',color='gold')
        try:
            lmc = plt.scatter(sidm_subhalos[snapshot[i]][0]['x'], sidm_subhalos[snapshot[i]][0]['y'],
                  s=100,marker='*',label=r'$\mathrm{LMC}$',color='magenta')
        except:
            pass

        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()

        plt.title(r'$\mathrm{SIDM}$',color='dodgerblue',fontsize=30)
        try:
            plt.legend(loc=2,handles=[mw,lmc],fontsize=20,frameon=False)
        except:
            pass

        plt.axis('off')

        plt.tight_layout()
        print("save sidm_visualization" + snapshot[i])
        plt.savefig("/home1/shuxingf/nbody-visualization/sidm_visualization/sidm_visualization" + snapshot[i] + ".png")
    return
    
    