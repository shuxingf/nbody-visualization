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



cdm_hlist = ['0.05000', '0.05060', '0.05130', '0.05190', '0.05260', '0.05330', '0.05400', '0.05470',
       '0.05540', '0.05610', '0.05680', '0.05750', '0.05830', '0.05900', '0.05980', '0.06050',
       '0.06130', '0.06210', '0.06290', '0.06370', '0.06450', '0.06530', '0.06620', '0.06700',
       '0.06790', '0.06880', '0.06960', '0.07050', '0.07140', '0.07240', '0.07330', '0.07420',
       '0.07520', '0.07620', '0.07710', '0.07810', '0.07910', '0.08010', '0.08120', '0.08220',
       '0.08330', '0.08430', '0.08540', '0.08650', '0.08760', '0.08870', '0.08990', '0.09100',
       '0.09220', '0.09340', '0.09460', '0.09580', '0.09700', '0.09830', '0.09950', '0.10080',
       '0.10210', '0.10340', '0.10470', '0.10610', '0.10740', '0.10880', '0.11020', '0.11160',
       '0.11310', '0.11450', '0.11600', '0.11750', '0.11900', '0.12050', '0.12200', '0.12360',
       '0.12520', '0.12680', '0.12840', '0.13010', '0.13170', '0.13340', '0.13510', '0.13690',
       '0.13860', '0.14040', '0.14220', '0.14400', '0.14590', '0.14780', '0.14970', '0.15160',
       '0.15350', '0.15550', '0.15750', '0.15950', '0.16160', '0.16360', '0.16570', '0.16780',
       '0.17000', '0.17220', '0.17440', '0.17660', '0.17890', '0.18120', '0.18350', '0.18590',
       '0.18830', '0.19070', '0.19310', '0.19560', '0.19810', '0.20060', '0.20320', '0.20580',
       '0.20850', '0.21110', '0.21380', '0.21660', '0.21940', '0.22220', '0.22500', '0.22790',
       '0.23080', '0.23380', '0.23680', '0.23980', '0.24290', '0.24600', '0.24920', '0.25240',
       '0.25560', '0.25890', '0.26220', '0.26560', '0.26900', '0.27250', '0.27600', '0.27950',
       '0.28310', '0.28670', '0.29040', '0.29410', '0.29790', '0.30170', '0.30560', '0.30950',
       '0.31350', '0.31750', '0.32160', '0.32570', '0.32990', '0.33410', '0.33840', '0.34270',
       '0.34710', '0.35160', '0.35610', '0.36070', '0.36530', '0.37000', '0.37470', '0.37950',
       '0.38440', '0.38930', '0.39430', '0.39940', '0.40450', '0.40970', '0.41500', '0.42030',
       '0.42570', '0.43110', '0.43670', '0.44230', '0.44790', '0.45370', '0.45950', '0.46540',
       '0.47140', '0.47740', '0.48350', '0.48970', '0.49600', '0.50240', '0.50880', '0.51540',
       '0.52200', '0.52870', '0.53550', '0.54230', '0.54930', '0.55630', '0.56350', '0.57070',
       '0.57800', '0.58540', '0.59290', '0.60050', '0.60830', '0.61610', '0.62400', '0.63200',
       '0.64010', '0.64830', '0.65660', '0.66500', '0.67360', '0.68220', '0.69100', '0.69980',
       '0.70880', '0.71790', '0.72710', '0.73640', '0.74590', '0.75540', '0.76510', '0.77500',
       '0.78490', '0.79500', '0.80520', '0.81550', '0.82600', '0.83650', '0.84730', '0.85820',
       '0.86920', '0.88030', '0.89160', '0.90300', '0.91460', '0.92640', '0.93830', '0.95030',
       '0.96250', '0.97480', '0.98730', '1.00000']

sidm_hlist = ['0.05000', '0.05064', '0.05129', '0.05195', '0.05262', '0.05329', '0.05397', '0.05467',
       '0.05537', '0.05608', '0.05680', '0.05753', '0.05827', '0.05901', '0.05977', '0.06054',
       '0.06131', '0.06210', '0.06290', '0.06370', '0.06452', '0.06535', '0.06619', '0.06704',
       '0.06790', '0.06877', '0.06965', '0.07054', '0.07145', '0.07236', '0.07329', '0.07423',
       '0.07519', '0.07615', '0.07713', '0.07812', '0.07912', '0.08013', '0.08116', '0.08220',
       '0.08326', '0.08433', '0.08541', '0.08650', '0.08761', '0.08874', '0.08987', '0.09103',
       '0.09220', '0.09338', '0.09458', '0.09579', '0.09702', '0.09826', '0.09952', '0.10080',
       '0.10210', '0.10340', '0.10473', '0.10607', '0.10744', '0.10881', '0.11021', '0.11162',
       '0.11306', '0.11451', '0.11597', '0.11746', '0.11897', '0.12050', '0.12204', '0.12361',
       '0.12519', '0.12680', '0.12843', '0.13007', '0.13174', '0.13343', '0.13514', '0.13688',
       '0.13863', '0.14041', '0.14221', '0.14404', '0.14589', '0.14776', '0.14965', '0.15157',
       '0.15352', '0.15549', '0.15748', '0.15950', '0.16155', '0.16362', '0.16572', '0.16785',
       '0.17000', '0.17218', '0.17439', '0.17663', '0.17890', '0.18119', '0.18351', '0.18587',
       '0.18825', '0.19067', '0.19312', '0.19559', '0.19810', '0.20064', '0.20322', '0.20583',
       '0.20847', '0.21114', '0.21385', '0.21659', '0.21937', '0.22219', '0.22504', '0.22792',
       '0.23085', '0.23381', '0.23681', '0.23985', '0.24292', '0.24604', '0.24920', '0.25240',
       '0.25563', '0.25891', '0.26223', '0.26560', '0.26901', '0.27246', '0.27595', '0.27949',
       '0.28308', '0.28671', '0.29039', '0.29411', '0.29789', '0.30171', '0.30558', '0.30950',
       '0.31347', '0.31749', '0.32157', '0.32569', '0.32987', '0.33410', '0.33839', '0.34273',
       '0.34713', '0.35158', '0.35609', '0.36066', '0.36529', '0.36997', '0.37472', '0.37953',
       '0.38440', '0.38933', '0.39432', '0.39938', '0.40450', '0.40969', '0.41495', '0.42027',
       '0.42566', '0.43113', '0.43666', '0.44226', '0.44793', '0.45368', '0.45950', '0.46540',
       '0.47137', '0.47741', '0.48354', '0.48974', '0.49602', '0.50239', '0.50883', '0.51536',
       '0.52197', '0.52867', '0.53545', '0.54232', '0.54928', '0.55633', '0.56346', '0.57069',
       '0.57802', '0.58543', '0.59294', '0.60055', '0.60825', '0.61606', '0.62396', '0.63197',
       '0.64007', '0.64828', '0.65660', '0.66503', '0.67356', '0.68220', '0.69095', '0.69982',
       '0.70879', '0.71789', '0.72710', '0.73643', '0.74587', '0.75544', '0.76513', '0.77495',
       '0.78489', '0.79496', '0.80516', '0.81549', '0.82595', '0.83655', '0.84728', '0.85815',
       '0.86916', '0.88031', '0.89161', '0.90305', '0.91463', '0.92637', '0.93825', '0.95029',
       '0.96248', '0.97483', '0.98733', '1.00000']



#for i,r in enumerate(r_bins):
#    find total number of particles in subselected array with distance < r
#    multiply by particle mass to get enclosed mass
#    rho_enclosed[i] = enclosed mass divided by volume

def plot(snapshot, f_short_cdm,  f_short_sidm,  LMC_main, LMC_main_vi, f_cdm, f_sidm):
    r_bins = np.linspace(10.,100.,10)
    rho_enclosed_cdm = np.zeros(len(r_bins))
    rho_enclosed_sidm = np.zeros(len(r_bins))

    distance_cut=100.
    projection_thickness=2.
    Mpc_to_kpc=1000.
    

    LMC_main = LMC_main[::-1]
    LMC_main_vi = LMC_main_vi[::-1]


#calculate density for cdm

    dist = {}
    f_short_cdm ={}

    
    
    for key in f_cdm.keys():
        print("subselecting " + key + " for cdm")
        mass = np.min(f_cdm[key]['mass'][:])
        scale = float(cdm_hlist[int(key)])
        lmc_ind = np.argmin(np.abs(LMC_main['scale']-scale))
        xdist = f_cdm[key]['pos'][:,0]- LMC_main[lmc_ind]['x']
        ydist = f_cdm[key]['pos'][:,1]- LMC_main[lmc_ind]['y']
        zdist = f_cdm[key]['pos'][:,2]- LMC_main[lmc_ind]['z']
        dist = Mpc_to_kpc*np.sqrt(xdist**2+ydist**2+zdist**2)/f_cdm[key].properties['h']
        for i,r in enumerate(r_bins):
            particles = len(f_cdm[key]['pos'][:,0][(dist<r)])
            total_mass = mass * particles
            print("cdm tm is " + total_mass)
            volume = 4/3 * 3.1415926 * r**3
            rho_enclosed_cdm[i] = total_mass/volume


        mass = np.min(f_sidm[key]['mass'][:])
        scale = float(sidm_hlist[int(key)])
        lmc_ind = np.argmin(np.abs(LMC_main_vi['scale']-scale))
        xdist = f_sidm[key]['pos'][:,0]- LMC_main_vi[lmc_ind]['x']
        ydist = f_sidm[key]['pos'][:,1]- LMC_main_vi[lmc_ind]['y']
        zdist = f_sidm[key]['pos'][:,2]- LMC_main_vi[lmc_ind]['z']
        dist = Mpc_to_kpc*np.sqrt(xdist**2+ydist**2+zdist**2)/f_sidm[key].properties['h']
        for i,r in enumerate(r_bins):
            particles = len(f_sidm[key]['pos'][:,0][(dist<r)])
            total_mass = mass * particles
            print("sidm tm is " + total_mass)
            volume = 4/3 * 3.1415926 * r**3
            rho_enclosed_sidm[i] = total_mass/volume

        plt.subplot(121)
        plt.loglog(r_bins,rho_enclosed_cdm)
        plt.subplot(122)
        plt.loglog(r_bins,rho_enclosed_sidm)

        plt.savefig("/home1/shuxingf/nbody-visualization/density/cdm_density" + key + ".png")

   



 
       

            
  #solar masses/ 
