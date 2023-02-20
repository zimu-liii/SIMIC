import os
os.chdir('../..')

from siics import simu

ss = simu.SIICS_Simulation()

for i in [0,0.0001,0.001,0.005,0.01,0.05,0.1,0.2,0.3,0.4,0.5,0.75,1]:
	for j in range(3):
		eb = ss.error_pollute(1,i)
		ss.save(eb, 'output/'+str(i)+'-'+str(j)+'.tiff')
		print(i,j,ss.similarity(eb))