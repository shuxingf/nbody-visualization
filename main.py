import subselect
import subselect2
import load
import plot 
import sys
import densityplot

param =""
snapshot = []
start = ""
end = ""
if(len(sys.argv) == 4):
    param = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]
    snapshot=["%03d" % x for x in range(int(start),int(end)+1)]
if (len(sys.argv) == 3):
    param = sys.argv[1]
    start = int(sys.argv[2])
    snapshot = [str(start)]



f_cdm = {}
cdm_halos = {}
f_sidm = {}
sidm_halos = {}


#load
LMC_main, LMC_main_vi, MW_main, MW_main_vi = load.load(snapshot,f_cdm, cdm_halos,f_sidm, sidm_halos)

#subselect
f_short_cdm = {}
f_short_sidm = {}

    
if(param == "MW"):
    subselect.subselect(cdm_halos, sidm_halos, f_cdm, f_short_cdm, f_sidm, f_short_sidm)
    plot.plot_snapshot(snapshot, f_short_cdm, f_short_sidm, LMC_main, LMC_main_vi, MW_main, MW_main_vi, param)
if(param == "LMC"):
    subselect2.subselect(f_cdm, f_short_cdm, f_sidm, f_short_sidm ,LMC_main, LMC_main_vi)
    plot.plot_snapshot(snapshot, f_short_cdm, f_short_sidm, LMC_main, LMC_main_vi, MW_main, MW_main_vi, param)
if(param == "D"):
    densityplot.plot(snapshot, f_short_cdm,  f_short_sidm,  LMC_main, LMC_main_vi, f_cdm, f_sidm)

   
