import subselect
import load
import plot 

f_cdm = {}
cdm_halos = {}
cdm_subhalos = {}
f_sidm = {}
sidm_halos = {}
sidm_subhalos = {}
snapshot = ['234']
#snapshot=["%03d" % x for x in range(10)]



#load
load.load(snapshot,f_cdm, cdm_halos, cdm_subhalos, f_sidm, sidm_halos, sidm_subhalos)
#subselect
f_short_cdm = {}
f_short_sidm = {}
subselect.subselect(cdm_halos, sidm_halos, f_cdm, f_short_cdm, f_sidm, f_short_sidm)
#plot
plot.plot_snapshot(snapshot, f_short_cdm, cdm_halos, cdm_subhalos, f_short_sidm, sidm_halos, sidm_subhalos)
