import math

# configuration of required Global Parameters

# configuration of Number of Phases Required
def AFE_config_numOfPhases(noOfPhases):
	AFE_modifyRegGlobal(dev1.Page0.REG_NUMPHASE_PPG,     noOfPhases-1)
	No_of_Phases_PerPhase[0] = noOfPhases
	
	
# Transmitter configurations
# filter set selection anf LED ON Time Selection
def AFE_config_FilterSetSel(PhNo,filter_Set_Select):
	# selecting which filter set to be used 
	# 0 for Set1 & 1 for Set2
	AFE_modifyRegPPM(PhNo, dev1.Page1.FILTER_SET_SEL, filter_Set_Select)

def AFE_config_LEDOnTime_width(PhNo,ledOnWidth,filterNo):
	#(REG_TWLED + 1)*tTE
	
	AFE_modifyRegPPM(PhNo, dev1.Page1.REG_TWLED, ledOnWidth-1)
	AFE_config_FilterSetSel(PhNo,filterNo)
	
# 		TXP Driver configuration
def AFE_config_Drv_TXP(PhNo,drv_txp):

	AFE_modifyRegPPM(PhNo, dev1.Page1.LED_DRV_TXP,       drv_txp)
	
#		TXN Driver 1 configuration
def AFE_config_Drv1_TXN(PhNo,drv_txn):

	AFE_modifyRegPPM(PhNo, dev1.Page1.LED_DRV1_TXN,      drv_txn)

# 		TXN Driver 2 configuration
def AFE_config_Drv2_TXN(PhNo,drv_txn):

	AFE_modifyRegPPM(PhNo, dev1.Page1.LED_DRV2_TXN,      drv_txn)
	
# 	LED Driver 1 configuration
def AFE_config_ILED_DRV1(PhNo,ledDrvCurr, fullScaleCurr):
	# sets the LED Driver 1 current
	maxCurr = fullScaleCurr
	
	oneLSBCurr = 0
	if fullScaleCurr == 25:
		oneLSBCurr = 0.098
	elif fullScaleCurr == 50:
		oneLSBCurr = 0.196
	elif fullScaleCurr == 100:
		oneLSBCurr = 0.392
	elif fullScaleCurr == 125:
		oneLSBCurr = 0.49
	elif fullScaleCurr == 167:
		oneLSBCurr = 0.655
	
	ILEDdrv_curr = ledDrvCurr/oneLSBCurr

	if ILEDdrv_curr < math.floor(ILEDdrv_curr)+oneLSBCurr:
		ILEDdrv_curr = math.floor(ILEDdrv_curr)
	else:
		ILEDdrv_curr = math.ceil(ILEDdrv_curr)
	
	if ILEDdrv_curr>255:
		AFE_modifyRegPPM(PhNo, dev1.Page1.ILED_DRV1, 0)
		return
		
	logWindow_wid.settingLogText(str(maxCurr)+'\n'+str(ledDrvCurr)+'\n'+str(oneLSBCurr)+'\n'+str(ILEDdrv_curr))
	AFE_modifyRegPPM(PhNo, dev1.Page1.ILED_DRV1, ILEDdrv_curr)


# 	LED Driver 2 configuration
def AFE_config_ILED_DRV2(PhNo,ledDrvCurr, fullScaleCurr):
	# sets the LED Driver 2 current
	maxCurr = fullScaleCurr
	
	oneLSBCurr = 0
	if fullScaleCurr == 25:
		oneLSBCurr = 0.098
	elif fullScaleCurr == 50:
		oneLSBCurr = 0.196
	elif fullScaleCurr == 100:
		oneLSBCurr = 0.392
	elif fullScaleCurr == 125:
		oneLSBCurr = 0.49
	elif fullScaleCurr == 167:
		oneLSBCurr = 0.655
	
	ILEDdrv_curr = ledDrvCurr/oneLSBCurr

	if ILEDdrv_curr < math.floor(ILEDdrv_curr)+oneLSBCurr:
		ILEDdrv_curr = math.floor(ILEDdrv_curr)
	else:
		ILEDdrv_curr = math.ceil(ILEDdrv_curr)
	
	if ILEDdrv_curr>255:
		AFE_modifyRegPPM(PhNo, dev1.Page1.ILED_DRV1, 0)
		return
		
	logWindow_wid.settingLogText(str(maxCurr)+'\n'+str(ledDrvCurr)+'\n'+str(oneLSBCurr)+'\n'+str(ILEDdrv_curr))
	AFE_modifyRegPPM(PhNo, dev1.Page1.ILED_DRV2, ILEDdrv_curr)
	
# 	configuration of Number of TIAs required
def AFE_config_noOfTIAs(PhNo,noOfTIAs):
	AFE_modifyRegPPM(PhNo, dev1.Page1.REG_NUM_TIA, noOfTIAs-1)
	
# 	configuration of Number of Averages in ADC
def AFE_config_NumOfAvg(PhNo,numOfAvgs):
	AFE_modifyRegPPM(PhNo, dev1.Page1.REG_NUMAV,     numOfAvgs-1)
	
# 	configuration of AACM scheme
def AFE_config_AACMtype(PhNo,ana_aacm,baseline_amb):
	AFE_modifyRegPPM(PhNo, dev1.Page1.USE_ANA_AACM, ana_aacm)
	AFE_modifyRegPPM(PhNo, dev1.Page1.UPDATE_BASELINE_AMB, baseline_amb)
	
# 	DRE Enable bit configuration
def AFE_config_EnableDRE(PhNo, dreEnable):
	AFE_modifyRegPPM(PhNo, dev1.Page1.ENABLE_DRE, dreEnable)
	
#  FIFO Controls


#  Masking Factor
def AFE_config_masking(PhNo,mask_mode):
	AFE_modifyRegPPM(PhNo, dev1.Page1.REG_PH_MASK_FACTOR, mask_mode)
	
# PPG Decimation Factor
def AFE_config_ppgDecimation(PhNo,noOfSamples):
	AFE_modifyRegPPM(PhNo, dev1.Page1.REG_DEC_FACTOR,    noOfSamples)
	
	
	
#  TIAn Configuration 
def AFE_config_IN_TIAx(PhNo, TIAx, PDx, val):
	IN_TIA = [dev1.Page1.IN_TIA1, dev1.Page1.IN_TIA2, dev1.Page1.IN_TIA3, dev1.Page1.IN_TIA4]
	
	temp = sigParameter()
	temp.address = IN_TIA[TIAx-1].address
	temp.lsb = IN_TIA[TIAx-1].lsb + PDx -1
	temp.msb = temp.lsb
	AFE_modifyRegPPM(PhNo, temp, val)
	
# 	TIA Gain or FeedBack Resistance
def AFE_config_TIAGain(PhNo, TIAx, Rf_val):
	RF_TIA = [dev1.Page1.RF_TIA1, dev1.Page1.RF_TIA2, dev1.Page1.RF_TIA3, dev1.Page1.RF_TIA4]

	AFE_modifyRegPPM(PhNo, RF_TIA[TIAx-1], Rf_val)
	
# 	TIA FeedBack Capacitance
def AFE_config_TIACf(PhNo, TIAx, Cf_val):
	CF_TIA = [dev1.Page1.CF_TIA1, dev1.Page1.CF_TIA2, dev1.Page1.CF_TIA3, dev1.Page1.CF_TIA4]

	AFE_modifyRegPPM(PhNo, CF_TIA[TIAx-1], Cf_val)
	
# 	IOFFDAC LED Current configuration
def AFE_config_IOFFDAC_LED(PhNo, TIAx, IOFFDAC_LED_curr):

	IOFFDAC_LED_TIA = [dev1.Page1.IOFFDAC_LED_TIA1, dev1.Page1.IOFFDAC_LED_TIA2, dev1.Page1.IOFFDAC_LED_TIA3, dev1.Page1.IOFFDAC_LED_TIA4]
	
	fullScaleCurr = 0.000063875
	oneLSBCurr = 0.125
	curr_led = IOFFDAC_LED_curr/oneLSBCurr

	if curr_led<math.floor(curr_led)+oneLSBCurr:
		curr_led = math.floor(curr_led)
	else:
		curr_led = math.ceil(curr_led)
	
	if curr_led>511:
		AFE_modifyRegPPM(PhNo, IOFFDAC_LED_TIA[TIAx-1], 0)
		return

	AFE_modifyRegPPM(PhNo, IOFFDAC_LED_TIA[TIAx-1], curr_led)

#  	LED DC Enabling
def AFE_config_LED_DC_Enable(PhNo, TIAx, LED_DC_EN):
	LED_DC = [dev1.Page1.LED_DC_EN_TIA1, dev1.Page1.LED_DC_EN_TIA2, dev1.Page1.LED_DC_EN_TIA3, dev1.Page1.LED_DC_EN_TIA4]

	AFE_modifyRegPPM(PhNo, LED_DC[TIAx-1], LED_DC_EN)
	
# 	Auto AMB Insert
def AFE_config_AutoAmbInsert(PhNo, val):
	AFE_modifyRegPPM(PhNo, dev1.Page1.AUTO_AMB_INSERT, val)

def AFE_config_Phase_n_Reset(PhNo):
	AFE_Phase_n_reset(PhNo)
	
def AFE_config_TIAn_Reset(PhNo,TIAn):
	AFE_TIA_n_reset(PhNo,TIAn)
