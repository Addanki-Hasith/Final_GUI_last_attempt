import numpy as np

reg_drv = np.zeros((512,24),dtype = 'int8')

def driver_reset():
	for i in range(512):
		for j in range(24):
			reg_drv[i][j]=0
