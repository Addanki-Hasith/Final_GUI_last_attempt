import math

# configuration of required Global Parameters

# configuration of Phase Timing Scheme
def AFE_config_phaseTimingScheme(phTmgScheme):
	phaseTiming_mode[0] = phTmgScheme
	if phTmgScheme == STAGGER_mode:
		AFE_modifyRegGlobal(dev1.Page0.HIGH_PRF_MODE,    			  	False)
		AFE_modifyRegGlobal(dev1.Page0.MAX_AMB_REJ,  					False)
		AFE_modifyRegGlobal(dev1.Page0.DIS_POST_AMB_MAX_AMB_REJ,     	False)
		logWindow_wid.settingLogText("STAGGER Mode is Selected")
		
	elif phTmgScheme == HIGH_PRF_MODE_mode:
		AFE_modifyRegGlobal(dev1.Page0.HIGH_PRF_MODE,    				True)
		AFE_modifyRegGlobal(dev1.Page0.MAX_AMB_REJ,  					False)
		AFE_modifyRegGlobal(dev1.Page0.DIS_POST_AMB_MAX_AMB_REJ,     	False)
		logWindow_wid.settingLogText("HIGH PRF Mode is Selected")
		
		# set the DIS_DEEP_SLEEP bit to '1' to disable the entry into deep sleep
# 		AFE_modifyRegGlobal(dev1.Page0.DIS_DEEP_SLEEP,					1)
# 		
# 		# set the EN_ALWAYS_ACTIVE bit to '1' to keep the device inactive state throughout the PRF cycle
# 		AFE_modifyRegGlobal(dev1.Page0.EN_ALWAYS_ACTIVE,				1)
# 		
# 		# Set REG_TDEEP_SLEEP_PWRUP and REG_TACTIVE_PWRUP registers to 0 to minimize these timing
# 		# overheads and utilize the PRF cycle more efficiently for accommodating the PPG phase
# 		AFE_modifyRegGlobal(dev1.Page0.REG_TDEEP_SLEEP_PWRUP,    		0)
# 		AFE_modifyRegGlobal(dev1.Page0.REG_TACTIVE_PWRUP,   			0)
# 		
		
	elif phTmgScheme == MAX_AMB_REJ_mode:
		AFE_modifyRegGlobal(dev1.Page0.HIGH_PRF_MODE,    				False)
		AFE_modifyRegGlobal(dev1.Page0.MAX_AMB_REJ,  					True)
		AFE_modifyRegGlobal(dev1.Page0.DIS_POST_AMB_MAX_AMB_REJ,     	False)
		logWindow_wid.settingLogText("Maximum Ambient Rejection Mode is Selected")
		
	elif phTmgScheme == DIS_POST_AMB_MAX_AMB_REJ_mode:
		AFE_modifyRegGlobal(dev1.Page0.HIGH_PRF_MODE,    				False)
		AFE_modifyRegGlobal(dev1.Page0.MAX_AMB_REJ,  					False)
		AFE_modifyRegGlobal(dev1.Page0.DIS_POST_AMB_MAX_AMB_REJ,     	True)
		logWindow_wid.settingLogText('Disable Post Ambient Maximum Ambient Rejection Mode is Selected')

# 
# configuration of External Clock Decimation Factor
def AFE_config_extClkDecimation(decVal):
	if decVal == external_clk_NoDecimation:
		AFE_modifyRegGlobal(dev1.Page0.DIV_CLK_EXT, 	external_clk_NoDecimation)
	elif decVal == external_clk_Decimation_2:
		AFE_modifyRegGlobal(dev1.Page0.DIV_CLK_EXT, 	external_clk_Decimation_2)
	elif decVal == external_clk_Decimation_4:
		AFE_modifyRegGlobal(dev1.Page0.DIV_CLK_EXT, 	external_clk_Decimation_4)


# configuration of all the default parameters
def AFE_config_defaultTimings():
	# configuring Timing parameters associated with the various timing windows
	activePowUp = 24        # (REG_TACTIVE_PWRUP + 1) * tTE
	activePowDn = 1         # (REG_TACTIVE_PWDN + 2) * tTE
	deepSleepPowUp = 71     # (REG_TDEEP_SLEEP_PWRUP + 4.5) * tTE
	deepSleepPowDn = 5      # (REG_TDEEP_SLEEP_PWDN + 1) * tTE
	activeDataRdy = 3       # (REG_TACTIVE_DATA_RDY + 1) * tTE
	widthDataRdy = 0        # (REG_TW_DATA_RDY + 1) * tTE 
	tsep = 0                # REG_TSEP * tTE
	sampSep = 1             # samp window separation 1*tTE
	sepConvStart = 1        # 1*tTE
	
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TACTIVE_PWRUP,    	activePowUp)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TACTIVE_PWDN,     	activePowDn)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TDEEP_SLEEP_PWRUP,    deepSleepPowUp)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TDEEP_SLEEP_PWDN,     deepSleepPowDn)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TACTIVE_DATA_RDY,     activeDataRdy)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TW_DATA_RDY,     		widthDataRdy)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TSEP,     			tsep) #Separation between successive windows
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TSAMP_SEP, 			sampSep)
	AFE_RegMap.AFE_modifyRegGlobal(dev1.Page0.REG_TSEP_CONV_START, 		sepConvStart)


# configuration of Clocking Mode
def AFE_config_clockingMode(clkMode):
	
	if clkMode == CLK_MODE_INT:
		# Setting all the default values
		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_TE,     			False)

		AFE_modifyRegGlobal(dev1.Page0.OSCL_DIS,        			False)

		AFE_modifyRegGlobal(dev1.Page0.PDN_OSCL_IN_DEEP_SLEEP,   	False)
		
		AFE_modifyRegGlobal(dev1.Page0.EN_PRF_RESET,    			False)

		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_PRF,    			False)

		AFE_modifyRegGlobal(dev1.Page0.EN_INT_IN_SINGLE_SHOT,    	False)

		AFE_modifyRegGlobal(dev1.Page0.SPLIT_CLK_FOR_TE_PRF,     	False)

		AFE_modifyRegGlobal(dev1.Page0.EN_CLK_MODE_MIX,      		False)
		
# 		AFE_config_extClkDecimation(external_clk_NoDecimation)

		logWindow_wid.settingLogText('Internal Clock Mode is selected')
		
	elif clkMode == CLK_MODE_EXT:
		
		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_TE,     			True)

		AFE_modifyRegGlobal(dev1.Page0.OSCL_DIS,        			True)

		AFE_modifyRegGlobal(dev1.Page0.PDN_OSCL_IN_DEEP_SLEEP,   	False)
		
		AFE_modifyRegGlobal(dev1.Page0.EN_PRF_RESET,    			False)

		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_PRF,    			False)

		AFE_modifyRegGlobal(dev1.Page0.EN_INT_IN_SINGLE_SHOT,    	False)

		AFE_modifyRegGlobal(dev1.Page0.SPLIT_CLK_FOR_TE_PRF,     	False)

		AFE_modifyRegGlobal(dev1.Page0.EN_CLK_MODE_MIX,      		False)
		
		AFE_config_extClkDecimation(external_clk_NoDecimation)
		
		logWindow_wid.settingLogText('External Clock Mode is selected')
		
	elif clkMode == CLK_MODE_SS:
		
		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_TE,     			False)

		AFE_modifyRegGlobal(dev1.Page0.OSCL_DIS,        			False)

		AFE_modifyRegGlobal(dev1.Page0.PDN_OSCL_IN_DEEP_SLEEP,   	True)
		
		AFE_modifyRegGlobal(dev1.Page0.EN_PRF_RESET,    			True)

		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_PRF,    			False)

		AFE_modifyRegGlobal(dev1.Page0.EN_INT_IN_SINGLE_SHOT,    	True)

		AFE_modifyRegGlobal(dev1.Page0.SPLIT_CLK_FOR_TE_PRF,     	True)

		AFE_modifyRegGlobal(dev1.Page0.EN_CLK_MODE_MIX,      		False)
		
# 		AFE_config_extClkDecimation(external_clk_NoDecimation)

		logWindow_wid.settingLogText('Single Shot Clock Mode is selected')
		
	elif clkMode == CLK_MODE_MIX:
		
		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_TE,     			False)

		AFE_modifyRegGlobal(dev1.Page0.OSCL_DIS,        			False)

		AFE_modifyRegGlobal(dev1.Page0.PDN_OSCL_IN_DEEP_SLEEP,   	True)
		
		AFE_modifyRegGlobal(dev1.Page0.EN_PRF_RESET,    			False)

		AFE_modifyRegGlobal(dev1.Page0.SEL1_CLK_PRF,    			True)

		AFE_modifyRegGlobal(dev1.Page0.EN_INT_IN_SINGLE_SHOT,    	False)

		AFE_modifyRegGlobal(dev1.Page0.SPLIT_CLK_FOR_TE_PRF,     	True)

		AFE_modifyRegGlobal(dev1.Page0.EN_CLK_MODE_MIX,      		True)
		
# 		AFE_config_extClkDecimation(external_clk_NoDecimation)

		logWindow_wid.settingLogText('Mixed Clock Mode is selected with an external clock of 32.768 KHz')
		
		
	# enabling the timers
# 	AFE_modifyRegGlobal(dev1.Page0.PRF_COUNTER_ENABLE,				True)
# 	AFE_modifyRegGlobal(dev1.Page0.TIMER_ENABLE,				True)
# 	setting all the default timings
	AFE_config_defaultTimings()
	

# configuration of PRF freq and Step Count ( PRPCT parameter )

# default step count is 1

def AFE_config_stepcount(StepCount):
	# STEP_COUNT is derived from the register REG_STEP_COUNT as (REG_STEP_COUNT + 1)
	AFE_modifyRegGlobal(dev1.Page0.REG_STEP_COUNT, 		StepCount-1)
	
def AFE_config_prpct(prf_freq):

	setPRPCT = math.ceil(256000/prf_freq)
	
	# deriving PRPCT based on required PRF frequency
	AFE_modifyRegGlobal(dev1.Page0.PRPCT, 				setPRPCT)
	
	ValuesAssigned = [setPRPCT , 256000/setPRPCT]
	
	return ValuesAssigned
	
def AFE_config_ReConvThre(setReConvThreLEDdc):
	maxVol = 1.2
	oneLSB = maxVol/(pow(2, 21)-1)
	Conv_Thr_LED_DC = setReConvThreLEDdc/oneLSB
	Conv_Thr_LED_DC = Conv_Thr_LED_DC/pow(2,13)
	
	if Conv_Thr_LED_DC< (math.floor(Conv_Thr_LED_DC)+oneLSB):
		Conv_Thr_LED_DC = math.floor(Conv_Thr_LED_DC)
	else:
		Conv_Thr_LED_DC = math.ceil(Conv_Thr_LED_DC)

	AFE_modifyRegGlobal(dev1.Page0.REG_RECONV_THR_LED_DC,     Conv_Thr_LED_DC)
	
	return Conv_Thr_LED_DC
	
	
def AFE_config_maxNoOfTIAs(maxNoTIAs):
	# global parameter NUM_TIA_MAX equal to the maximum number of TIAs active across all phases
	
	Maximum_no_of_TIAs_global.setCurrentIndex(maxNoTIAs)
	AFE_modifyRegGlobal(dev1.Page0.REG_NUM_TIA_MAX,      maxNoTIAs-1)
	logWindow_wid.settingLogText('Maximum of '+str(maxNoTIAs)+ ' TIAs are selected')
	
	
def AFE_config_RF_ANA_AACMcontrols():
	
	
	RF_ANA_AACM_START = [dev1.Page0.RF_ANA_AACM_START_TIA1, dev1.Page0.RF_ANA_AACM_START_TIA2, dev1.Page0.RF_ANA_AACM_START_TIA3, dev1.Page0.RF_ANA_AACM_START_TIA4]

	if Full_Scale_AMB_DAC_global[0] == AMB_DAC_mode1x or Full_Scale_AMB_DAC_global[0] == AMB_DAC_mode2x:
		for TIAx in range(4):
			AFE_modifyRegGlobal(RF_ANA_AACM_START[TIAx],6)
		
		AFE_modifyRegGlobal(dev1.Page0.RF_ANA_AACM_END, 10)
	else:
		for TIAx in range(4):
			AFE_modifyRegGlobal(RF_ANA_AACM_START[TIAx],0)

		AFE_modifyRegGlobal(dev1.Page0.RF_ANA_AACM_END, 5)
		
# 	logWindow_wid.settingLogText('AACM Controls are configured successfully')


def AFE_config_fullScaleAMBDAC(IFS_AMB_OFFDAC_mode):
	
	IFS_AMB_OFFDAC_TIA = [dev1.Page0.IFS_AMB_OFFDAC_TIA1, dev1.Page0.IFS_AMB_OFFDAC_TIA2, dev1.Page0.IFS_AMB_OFFDAC_TIA3, dev1.Page0.IFS_AMB_OFFDAC_TIA4]
	
# 	if TIAn == 5:
	for i in range(Maximum_no_of_TIAs_global.currentIndex()):
		AFE_modifyRegGlobal(IFS_AMB_OFFDAC_TIA[i],IFS_AMB_OFFDAC_mode)
# 	else:
# 		AFE_modifyRegGlobal(IFS_AMB_OFFDAC_TIA[TIAn-1],IFS_AMB_OFFDAC_mode)
	
		
	if IFS_AMB_OFFDAC_mode == AMB_DAC_FS_15p935uA:
		Full_Scale_AMB_DAC_global[0] = AMB_DAC_mode1x
		
		
	elif IFS_AMB_OFFDAC_mode == AMB_DAC_FS_31p875uA:
		Full_Scale_AMB_DAC_global[0] = AMB_DAC_mode2x
		
		
	elif IFS_AMB_OFFDAC_mode == AMB_DAC_FS_63p75uA:
		Full_Scale_AMB_DAC_global[0] = AMB_DAC_mode4x
		
		
	elif IFS_AMB_OFFDAC_mode == AMB_DAC_FS_127p5uA:
		Full_Scale_AMB_DAC_global[0] = AMB_DAC_mode8x

		
	elif IFS_AMB_OFFDAC_mode == AMB_DAC_FS_255uA:
		Full_Scale_AMB_DAC_global[0] = AMB_DAC_mode16x

		
	AFE_config_RF_ANA_AACMcontrols()
	
	logWindow_wid.settingLogText('Full Scale AMB DAC Current is configured successfully')
	
def AFE_config_pdIOFFDAC(pdIOFFDAC,PdNo):
	
# 	
	
	IOFFDAC_PD = [dev1.Page0.IOFFDAC_PD1, dev1.Page0.IOFFDAC_PD2, dev1.Page0.IOFFDAC_PD3, dev1.Page0.IOFFDAC_PD4]
	# setting IOFFDAC_PD based on pdIOFFDAC current and AMB_DAC_mode
	maxCurr = Full_Scale_AMB_DAC_global[0]
	
	oneLSBCurr = maxCurr/(pow(2,8)-1)
	setPD_IOFFDAC = pdIOFFDAC/oneLSBCurr

	if setPD_IOFFDAC < math.floor(setPD_IOFFDAC) + oneLSBCurr:
		setPD_IOFFDAC = math.floor(setPD_IOFFDAC)
	else:
		setPD_IOFFDAC = math.ceil(setPD_IOFFDAC)
	
	if setPD_IOFFDAC>255:
		AFE_modifyRegGlobal(IOFFDAC_PD[PdNo], 0)
		return

	AFE_modifyRegGlobal(IOFFDAC_PD[PdNo],   setPD_IOFFDAC)
	
	logWindow_wid.settingLogText(str(setPD_IOFFDAC))


def AFE_config_polOFFDAC(polOFFDAC):
	# setting the polarity OFFDAC_AMB
	AFE_modifyRegGlobal(dev1.Page0.POL_IOFFDAC_AMB, polOFFDAC)

	# setting the polarity OFFDAC_LED
	AFE_modifyRegGlobal(dev1.Page0.POL_IOFFDAC_LED, polOFFDAC)
	
	if polOFFDAC== PD_cathode_INP:
		logWindow_wid.settingLogText("PD's Cathode is connected to INP")
	elif polOFFDAC== PD_cathode_INM:
		logWindow_wid.settingLogText("PD's Cathode is connected to INM")
		
def AFE_config_enLEDOFFDAC(enLEDOFFDAC):
	EN_LED_OFFDAC_TIA = [dev1.Page0.EN_LED_OFFDAC_TIA1, dev1.Page0.EN_LED_OFFDAC_TIA2, dev1.Page0.EN_LED_OFFDAC_TIA3, dev1.Page0.EN_LED_OFFDAC_TIA4]
	
	for TIAx in range(4):
		AFE_modifyRegGlobal(EN_LED_OFFDAC_TIA[TIAx],    enLEDOFFDAC)
		
	if enLEDOFFDAC:
		logWindow_wid.settingLogText('LED OFFSET DAC is enabled')
	else:
		logWindow_wid.settingLogText('LED OFFSET DAC is disabled')
		
def AFE_config_iLEDFS(iLEDFSCurrent):
	if iLEDFSCurrent == FS_LED_25mA:
		AFE_modifyRegGlobal(dev1.Page0.ILED_FS,      FS_LED_25mA)
		FS_LED_CURRENT_global[0] = FS_LED_0p5x
		logWindow_wid.settingLogText('0.5X FS Current Mode is configured')
		
	elif iLEDFSCurrent == FS_LED_50mA:
		AFE_modifyRegGlobal(dev1.Page0.ILED_FS,      FS_LED_50mA)
		FS_LED_CURRENT_global[0] = FS_LED_1x
		logWindow_wid.settingLogText('1X FS Current Mode is configured')
		
	elif iLEDFSCurrent == FS_LED_100mA:
		AFE_modifyRegGlobal(dev1.Page0.ILED_FS,      FS_LED_100mA)
		FS_LED_CURRENT_global[0] = FS_LED_2x
		logWindow_wid.settingLogText('2X FS Current Mode is configured')
		
	elif iLEDFSCurrent == FS_LED_125mA:
		AFE_modifyRegGlobal(dev1.Page0.ILED_FS,      FS_LED_125mA)
		FS_LED_CURRENT_global[0] = FS_LED_2p5x
		logWindow_wid.settingLogText('2.5X FS Current Mode is configured')
		
	elif iLEDFSCurrent == FS_LED_167mA:
		AFE_modifyRegGlobal(dev1.Page0.ILED_FS,      FS_LED_167mA)
		FS_LED_CURRENT_global[0] = FS_LED_3p3x
		logWindow_wid.settingLogText('3.3X FS Current Mode is configured')


def AFE_config_overrideBWPre(overrideBWPre):
	AFE_modifyRegGlobal(dev1.Page0.OVERRIDE_BW_PRE,      overrideBWPre)

def AFE_config_filterBWPre(FILT_BW, set):

	FILTER_BW_PRE_SET = [dev1.Page0.FILTER_BW_PRE_SET1, dev1.Page0.FILTER_BW_PRE_SET2]

	AFE_modifyRegGlobal(FILTER_BW_PRE_SET[set-1],    FILT_BW)

def AFE_config_filterBWFine(FILT_BW, set):

	FILTER_BW_FINE_SET = [dev1.Page0.FILTER_BW_FINE_SET1, dev1.Page0.FILTER_BW_FINE_SET2]

	AFE_modifyRegGlobal(FILTER_BW_FINE_SET[set-1],      FILT_BW)

def AFE_config_preChargeWidth(preChargeWidth):
	AFE_modifyRegGlobal(dev1.Page0.REG_TW_FILTER_PRE, preChargeWidth)
	
	

def AFE_config_LEDONTimes(ledOn1,ledOn2):
	
	maxSampSepTime = 0

	if ledOn1>ledOn2:
		maxSampSepTime = ledOn1
	else:
		maxSampSepTime = ledOn2

	if ledOn1 == LED_ON_TIMING_16uS:
		
		LED1_On_Label.setCurrentIndex(1)
		LED1_ON_TIME_GLOBAL[0] = LED_ON_TIMING_16uS
		
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_50KHz,1)
		AFE_config_filterBWFine(FILT_BW_50KHz,1)
		FILT_BW_PRE1[0] = '50 KHz'
		FILT_BW_FINE1[0] = '50 KHz'
		
	elif ledOn1 == LED_ON_TIMING_23uS:
		
		LED1_On_Label.setCurrentIndex(2)
		LED1_ON_TIME_GLOBAL[0] = LED_ON_TIMING_23uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_35KHz,1)
		AFE_config_filterBWFine(FILT_BW_35KHz,1)
		FILT_BW_PRE1[0] = '35 KHz'
		FILT_BW_FINE1[0] = '35 KHz'

	elif ledOn1 == LED_ON_TIMING_31uS:
		
		LED1_On_Label.setCurrentIndex(3)
		LED1_ON_TIME_GLOBAL[0] = LED_ON_TIMING_31uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_25KHz,1)
		AFE_config_filterBWFine(FILT_BW_25KHz,1)
		FILT_BW_PRE1[0] = '25 KHz'
		FILT_BW_FINE1[0] = '25 KHz'
		
	elif ledOn1 == LED_ON_TIMING_39uS:
		
		LED1_On_Label.setCurrentIndex(4)
		LED1_ON_TIME_GLOBAL[0] = LED_ON_TIMING_39uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_50KHz,1)
		AFE_config_filterBWFine(FILT_BW_15KHz,1)
		FILT_BW_PRE1[0] = '50 KHz'
		FILT_BW_FINE1[0] = '15 KHz'
		
	elif ledOn1 == LED_ON_TIMING_47uS:
		
		LED1_On_Label.setCurrentIndex(5)
		LED1_ON_TIME_GLOBAL[0] = LED_ON_TIMING_47uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_50KHz,1)
		AFE_config_filterBWFine(FILT_BW_10KHz,1)
		FILT_BW_PRE1[0] = '50 KHz'
		FILT_BW_FINE1[0] = '10 KHz'
		
	elif ledOn1 ==LED_ON_TIMING_63uS:
		
		LED1_On_Label.setCurrentIndex(6)
		LED1_ON_TIME_GLOBAL[0] = LED_ON_TIMING_63uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_50KHz,1)
		AFE_config_filterBWFine(FILT_BW_7p5KHz,1)
		FILT_BW_PRE1[0] = '50 KHz'
		FILT_BW_FINE1[0] = '7.5 KHz'
		
	elif ledOn1 == LED_ON_TIMING_70uS:
		
		LED1_On_Label.setCurrentIndex(7)
		LED1_ON_TIME_GLOBAL[0] = LED_ON_TIMING_70uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_50KHz,1)
		AFE_config_filterBWFine(FILT_BW_5KHz,1)
		FILT_BW_PRE1[0] = '50 KHz'
		FILT_BW_FINE1[0] = '5 KHz'
		
	elif ledOn1 == LED_ON_TIMING_78uS:
		
		LED1_On_Label.setCurrentIndex(8)
		LED1_ON_TIME_GLOBAL[0] = LED_ON_TIMING_78uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_32p5KHz,1)
		AFE_config_filterBWFine(FILT_BW_5KHz,1)
		FILT_BW_PRE1[0] = '32.5 KHz'
		FILT_BW_FINE1[0] = '5 KHz'
		
	elif ledOn1 == LED_ON_TIMING_94uS:
		
		LED1_On_Label.setCurrentIndex(9)
		LED1_ON_TIME_GLOBAL[0] = LED_ON_TIMING_94uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_32p5KHz,1)
		AFE_config_filterBWFine(FILT_BW_5KHz,1)
		FILT_BW_PRE1[0] = '32.5 KHz'
		FILT_BW_FINE1[0] = '5 KHz'
		
	elif ledOn1 == LED_ON_TIMING_117uS:
		
		LED1_On_Label.setCurrentIndex(10)
		LED1_ON_TIME_GLOBAL[0] = LED_ON_TIMING_117uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_25KHz,1)
		AFE_config_filterBWFine(FILT_BW_2p5KHz,1)
		FILT_BW_PRE1[0] = '25 KHz'
		FILT_BW_FINE1[0] = '2.5 KHz'

	if ledOn2 == LED_ON_TIMING_16uS:
		
		LED2_On_Label.setCurrentIndex(1)
		LED2_ON_TIME_GLOBAL[0] = LED_ON_TIMING_16uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_50KHz,2)
		AFE_config_filterBWFine(FILT_BW_50KHz,2)
		FILT_BW_PRE2[0] = '50 KHz'
		FILT_BW_FINE2[0] = '50 KHz'
		
	elif ledOn2 == LED_ON_TIMING_23uS:
		
		LED2_On_Label.setCurrentIndex(2)
		LED2_ON_TIME_GLOBAL[0] = LED_ON_TIMING_23uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_35KHz,2)
		AFE_config_filterBWFine(FILT_BW_35KHz,2)
		FILT_BW_PRE2[0] = '35 KHz'
		FILT_BW_FINE2[0] = '35 KHz'

	elif ledOn2 == LED_ON_TIMING_31uS:
		
		LED2_On_Label.setCurrentIndex(3)
		LED2_ON_TIME_GLOBAL[0] = LED_ON_TIMING_31uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_25KHz,2)
		AFE_config_filterBWFine(FILT_BW_25KHz,2)
		FILT_BW_PRE2[0] = '25 KHz'
		FILT_BW_FINE2[0] = '25 KHz'

	elif ledOn2 == LED_ON_TIMING_39uS:
		
		LED2_On_Label.setCurrentIndex(4)
		LED2_ON_TIME_GLOBAL[0] = LED_ON_TIMING_39uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_50KHz,2)
		AFE_config_filterBWFine(FILT_BW_15KHz,2)
		FILT_BW_PRE2[0] = '50 KHz'
		FILT_BW_FINE2[0] = '15 KHz'

	elif ledOn2 == LED_ON_TIMING_47uS:
		
		LED2_On_Label.setCurrentIndex(5)
		LED2_ON_TIME_GLOBAL[0] = LED_ON_TIMING_47uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_50KHz,2)
		AFE_config_filterBWFine(FILT_BW_10KHz,2)
		FILT_BW_PRE2[0] = '50 KHz'
		FILT_BW_FINE2[0] = '10 KHz'

	elif ledOn2 == LED_ON_TIMING_63uS:
		
		LED2_On_Label.setCurrentIndex(6)
		LED2_ON_TIME_GLOBAL[0] = LED_ON_TIMING_63uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_50KHz,2)
		AFE_config_filterBWFine(FILT_BW_7p5KHz,2)
		FILT_BW_PRE2[0] = '50 KHz'
		FILT_BW_FINE2[0] = '7.5 KHz'

	elif ledOn2 == LED_ON_TIMING_70uS:
		
		LED2_On_Label.setCurrentIndex(7)
		LED2_ON_TIME_GLOBAL[0] = LED_ON_TIMING_70uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_50KHz,2)
		AFE_config_filterBWFine(FILT_BW_5KHz,2)
		FILT_BW_PRE2[0] = '50 KHz'
		FILT_BW_FINE2[0] = '5 KHz'

	elif ledOn2 == LED_ON_TIMING_78uS:
		
		LED2_On_Label.setCurrentIndex(8)
		LED2_ON_TIME_GLOBAL[0] = LED_ON_TIMING_78uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_32p5KHz,2)
		AFE_config_filterBWFine(FILT_BW_5KHz,2)
		FILT_BW_PRE2[0] = '32.5 KHz'
		FILT_BW_FINE2[0] = '5 KHz'

	elif ledOn2 == LED_ON_TIMING_94uS:
		
		LED2_On_Label.setCurrentIndex(9)
		LED2_ON_TIME_GLOBAL[0] = LED_ON_TIMING_94uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_32p5KHz,2)
		AFE_config_filterBWFine(FILT_BW_5KHz,2)
		FILT_BW_PRE2[0] = '32.5 KHz'
		FILT_BW_FINE2[0] = '5 KHz'

	elif ledOn2 == LED_ON_TIMING_117uS:
		
		LED2_On_Label.setCurrentIndex(10)
		LED2_ON_TIME_GLOBAL[0] = LED_ON_TIMING_117uS
		AFE_config_overrideBWPre(True)     # configuring the override-BW-Pre-bit
		AFE_config_filterBWPre(FILT_BW_25KHz,2)
		AFE_config_filterBWFine(FILT_BW_2p5KHz,2)
		FILT_BW_PRE2[0] = '25 KHz'
		FILT_BW_FINE2[0] = '2.5 KHz'

	if maxSampSepTime<9:
		AFE_config_preChargeWidth(int(0x80))
		PRE_CHARGE_WIDTH[0] = '0'+unichr(int('b5',16))+'s'
	elif maxSampSepTime<20:
		AFE_config_preChargeWidth(int(0x84))
		PRE_CHARGE_WIDTH[0] = '4'+unichr(int('b5',16))+'s'
	elif maxSampSepTime<27:
		AFE_config_preChargeWidth(int(0x86))
		PRE_CHARGE_WIDTH[0] = '6'+unichr(int('b5',16))+'s'
	elif maxSampSepTime==30:
		AFE_config_preChargeWidth(int(0x88))
		PRE_CHARGE_WIDTH[0] = '8'+unichr(int('b5',16))+'s'
	
	if maxSampSepTime==4:
		MAX_TIA_TIME_CONST[0] = '3'+unichr(int('b5',16))+'s'
		Max_time_const_val[0] = 3000 # in nano seconds
	elif maxSampSepTime==6:
		MAX_TIA_TIME_CONST[0] = '4.6'+unichr(int('b5',16))+'s'
		Max_time_const_val[0] = 4600 # in nano seconds
	elif maxSampSepTime==8:
		MAX_TIA_TIME_CONST[0] = '6'+unichr(int('b5',16))+'s'
		Max_time_const_val[0] = 6000 # in nano seconds
	elif maxSampSepTime<20:
		MAX_TIA_TIME_CONST[0] = '3'+unichr(int('b5',16))+'s'
		Max_time_const_val[0] = 3000 # in nano seconds
	elif maxSampSepTime<27:
		MAX_TIA_TIME_CONST[0] = '5'+unichr(int('b5',16))+'s'
		Max_time_const_val[0] = 5000 # in nano seconds
	elif maxSampSepTime<30:
		MAX_TIA_TIME_CONST[0] = '6'+unichr(int('b5',16))+'s'
		Max_time_const_val[0] = 6000 # in nano seconds
	
	logWindow_wid.settingLogText('LED On Times and Filter BWs are assigned')
	





