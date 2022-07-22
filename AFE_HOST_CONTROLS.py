page_sel = [0]
def AFE_explicitPageSel(val):
	if val:
		page_sel[0] = 256
	else:
		page_sel[0] = 0


def AFE_readReg(registerAddress):
	val = 0
	for i in range(24):
		val = val + (reg_drv[registerAddress + page_sel[0]][i] * pow(2,(23-i)))
	return val

def AFE_writeReg(registerAddress,value):
	i = 23
	logWindow_wid.settingLogText(str(value))
	while(value>0):
		reg_drv[registerAddress+page_sel[0]][i] = value%2
		value = value//2
		i = i-1
	
	while i>=0:
		reg_drv[registerAddress+page_sel[0]][i] = 0
		i = i-1
	
# 	val = AFE_readReg(registerAddress)
	
