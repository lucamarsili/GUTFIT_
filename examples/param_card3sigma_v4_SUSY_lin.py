#Parameter card used for the scan
#1 column: fixed parameter
#2 columns: free parameter
#5 columns: measured èarameter with 3sigma uncertainties
#MSUSY = 10^7, MGUT = 10^16, TanBeta10
# Model of 2209.00021 parameters. Parameters with prefix "data_"
# are measured and can vary within a range. Parameters with prefix "model4_"
# are model parameters. Data from PDG + nuFIT. Note that angles are
# given in radians and mass squared differences of neutrinos are in GeV^2.
# all masses are in GeV. Here we can in log10(mass [GeV]), also log10(r1),log10(r2),  log10(ce) and log10(cnu)
#r1,r2 has to be linear due to proton decay dim 5 operator!!

sign_parameter         0 1
generic_quark_phase_a1 0 6.28
generic_quark_phase_a2 0 6.28
data_quark_th12        0.225003 
data_quark_th13        0.00372912
data_quark_th23        0.0422637
data_quark_delta       1.144
data_quark_yu          2.96877e-6
data_quark_yc          0.00145577
data_quark_yt          0.494057
data_quark_yd          5.61938e-6
data_quark_ys          0.00011298
data_quark_yb          0.00593357
data_lepton_ye         2.28598e-6 
data_lepton_ymu        4.82589e-4 
data_lepton_ytau       8.235e-3 
model4_mR              -15    -10
model4_r1              -0.03      0.03   
model4_r2              -1        4    
model4_cnu             3      20
model4_ce              0      1.5
data_neutrino_deltamsq21bf 7.42e-5 
data_neutrino_deltamsq31bf 2.510e-3 
data_neutrino_th23  0.734411111 
data_neutrino_th12  0.583516667 
data_neutrino_th13  0.150371111
data_neutrino_delta 3.4033920413889400    3.857177646907470      1.5533430342749500    3.857177646907470      1.5533430342749500
sigma_lepton_ye 0.114299e-6
sigma_lepton_ymu 0.00002419
sigma_lepton_ytau  0.00041175
sigma_neutrino_th12  0.013432222
sigma_neutrino_th13  0.002093333
sigma_neutrino_th23  0.019188889
sigma_dm21  0.21e-5
sigma_dm31  0.028e-3


