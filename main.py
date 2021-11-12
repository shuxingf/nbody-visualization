import subselect
import load
import plot 

f_cdm = {}
cdm_halos = {}
f_sidm = {}
sidm_halos = {}

#snapshot = ['235']
snapshot=["%03d" % x for x in range(230,236)]

#load
LMC_main, LMC_main_vi, MW_main, MW_main_vi = load.load(snapshot,f_cdm, cdm_halos,f_sidm, sidm_halos)
#subselect
f_short_cdm = {}
f_short_sidm = {}
subselect.subselect(cdm_halos, sidm_halos, f_cdm, f_short_cdm, f_sidm, f_short_sidm)
#plot
plot.plot_snapshot(snapshot, f_short_cdm, f_short_sidm, LMC_main, LMC_main_vi, MW_main, MW_main_vi)
