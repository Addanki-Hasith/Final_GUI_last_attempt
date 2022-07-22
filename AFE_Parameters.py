# phaseTimingScheme {STAGGER, HIGH_PRF_MODE, MAX_AMB_REJ, DIS_POST_AMB_MAX_AMB_REJ}

micro_char 	= unichr(int('b5',16)) # micro

phaseTiming_mode 				= [5]
STAGGER_mode 					= 0
HIGH_PRF_MODE_mode 				= 1
MAX_AMB_REJ_mode 				= 2
DIS_POST_AMB_MAX_AMB_REJ_mode 	= 3

# external clock decimation factor
external_clk_NoDecimation = 0	
external_clk_Decimation_2 = 1
external_clk_Decimation_4 = 2

# clocking modes {internal , external , single shot , mixed clock modes}
CLK_MODE_INT	= 0
CLK_MODE_EXT 	= 1
CLK_MODE_SS 	= 2
CLK_MODE_MIX 	= 3

# Ambient Cancellation Scheme
ANA_AACM_scheme 		= 0
MCU_control_scheme 		= 1
AMB_Cancellation_scheme_global = [2]

# Maximum Number of TIAs
Maximum_no_of_TIAs_global = QtGui.QComboBox()
Maximum_no_of_TIAs_global.addItems(['0','1','2','3','4'])



# full scale Ambient DAC Current
Full_Scale_AMB_DAC_global 	= [0]
AMB_DAC_mode1x 				= 15.9375
AMB_DAC_mode2x 				= 31.875
AMB_DAC_mode4x 				= 63.75
AMB_DAC_mode8x 				= 127.5
AMB_DAC_mode16x 			= 255
AMB_DAC_FS_15p935uA 		= 0
AMB_DAC_FS_31p875uA 		= 1
AMB_DAC_FS_63p75uA 			= 3
AMB_DAC_FS_127p5uA 			= 5
AMB_DAC_FS_255uA 			= 7

# polarity
PD_cathode_INP = 0
PD_cathode_INM = 1

# full scale for led current

FS_LED_CURRENT_global = [0]
FS_LED_0p5x 	= 25
FS_LED_1x 		= 50
FS_LED_2x		= 100
FS_LED_2p5x		= 125
FS_LED_3p3x 	= 167
FS_LED_25mA 	= 0
FS_LED_50mA 	= 1
FS_LED_100mA 	= 2
FS_LED_125mA	= 3
FS_LED_167mA 	= 5

# LED ON Times

LED_ON_TIMING_16uS = 4
LED_ON_TIMING_23uS = 6
LED_ON_TIMING_31uS = 8
LED_ON_TIMING_39uS = 10
LED_ON_TIMING_47uS = 12
LED_ON_TIMING_63uS = 16
LED_ON_TIMING_70uS = 18
LED_ON_TIMING_78uS = 20
LED_ON_TIMING_94uS = 24
LED_ON_TIMING_117uS = 30

LED1_ON_TIME_GLOBAL = [0]
LED2_ON_TIME_GLOBAL = [0]

LED_ON_TImings_Labels = ['None',
						'16 '+micro_char+'s',
						'23'+micro_char+'s',
						'31'+micro_char+'s',
						'39'+micro_char+'s',
						'47'+micro_char+'s',
						'63'+micro_char+'s',
						'70'+micro_char+'s',
						'78'+micro_char+'s',
						'94'+micro_char+'s',
						'117'+micro_char+'s']


LED1_On_Label = QtGui.QComboBox()
LED2_On_Label = QtGui.QComboBox()

for i in range(11):
	LED1_On_Label.addItem(str(i))
	LED2_On_Label.addItem(str(i))

# filter bandwidths
FILT_BW_2p5KHz = 5
FILT_BW_5KHz = 6
FILT_BW_7p5KHz = 7
FILT_BW_10KHz = 0
FILT_BW_15KHz = 2       # added
FILT_BW_20KHz = 12
FILT_BW_25KHz = 14       # added
FILT_BW_30KHz = 8
FILT_BW_32p5KHz = 9      # added
FILT_BW_35KHz = 10       # added
FILT_BW_50KHz = 16

FILT_BW_PRE1 = ['']
FILT_BW_PRE2 = ['']
FILT_BW_FINE1 = ['']
FILT_BW_FINE2 = ['']

PRE_CHARGE_WIDTH = ['']
MAX_TIA_TIME_CONST = ['']
Max_time_const_val = [0]

# # # # Per Phase Parameters
No_of_Phases_PerPhase = [0]

# Driver Parameters
AMB_PH_TXP = 0
LED_PH_TXP1 = 1
LED_PH_TXP2 = 2
LED_PH_TXP3 = 4
LED_PH_TXP4 = 8

AMB_PH_TXN = 0
LED_PH_TXN1 = 1
LED_PH_TXN2 = 2
LED_PH_TXN3 = 4
LED_PH_TXN4 = 8
LED_PH_TXN5 = 16
LED_PH_TXN6 = 32
LED_PH_TXN7 = 64
LED_PH_TXN8 = 128

#  number of averages
NUMAV_1 = 1
NUMAV_2 = 2
NUMAV_3 = 3
NUMAV_4 = 4
NUMAV_8 = 8

# AACM Scheme
AACM_OFF_perPhase = 1
AACM_EstNCan_ANA_perPhase = 2
AACM_CAN_ANA_perPhase = 3

# FIFO Controls


#  Masking factor
MASK_NEVER = 0
MASK_2X_mode = 1
MASK_4X_mode = 2
MASK_8X_mode = 3
MASK_16X_mode = 4
MASK_32X_mode = 5
MASK_64X_mode = 6
MASK_128X_mode = 7
MASK_256X_mode = 8
MASK_512X_mode = 9
MASK_1024X_mode = 10
MASK_ALWAYS = 15

# PPG Decimation Factor
PPG_No_Decimation = 0
PPG_Decimation_2 = 1
PPG_Decimation_4 = 2
PPG_Decimation_8 = 3
PPG_Decimation_16 = 4
PPG_Decimation_32 = 5

# Number of TIAs
PerPhase_no_of_TIAs_common = [0]
PerPhase_no_of_TIAs_common_configured = []

# FeedBack Resistance or TIA Gain
TIA_Gain_3p7KOhm = 1
TIA_Gain_5KOhm  = 2
TIA_Gain_10KOhm = 3
TIA_Gain_25KOhm = 4
TIA_Gain_33p3KOhm = 5
TIA_Gain_50KOhm = 6
TIA_Gain_71p5KOhm = 7
TIA_Gain_100KOhm = 8
TIA_Gain_142KOhm = 9
TIA_Gain_166KOhm = 10
TIA_Gain_200KOhm = 11
TIA_Gain_250KOhm = 12
TIA_Gain_500KOhm = 13
TIA_Gain_1MOhm = 14

# FeedBack Capacitance
TIA_CF_2p5pF = 0
TIA_CF_5pF = 1
TIA_CF_7p5pF = 2
TIA_CF_10pF = 3
TIA_CF_17p5pF = 4
TIA_CF_20pF = 5
TIA_CF_22p5pF = 6
TIA_CF_25pF = 7




# Summary table column numbers

summary_phase_num 			= 0
summary_phase_type 			= 1
summary_DRV_TXP				= 2
summary_DRV_TXN1			= 3
summary_DRV_TXN2			= 4
summary_LED_ON_Time			= 5
summary_ILED_DRV1			= 6
summary_ILED_DRV2			= 7
summary_NUMAV				= 8
summary_DRE					= 9
summary_AUTO_AMB_INSERT		= 10
summary_NumOf_TIAS			= 11
summary_FILT_BW_SEL			= 12
summary_USE_ANA_AACM		= 13
summary_UPDATE_BASELINE_AMB	= 14
summary_DEC_FACTOR			= 15
summary_FIFO_DATA_CTRL		= 16
summary_MASK_FACTOR			= 17
summary_IN_TIA				= 18
summary_LED_DC_ENABLE		= 19
summary_IOFFDAC_LED			= 20
summary_RF					= 21
summary_CF					= 22


def Parameters_reset_Global_and_PerPhase():	
	FILT_BW_PRE1[0] = ''
	FILT_BW_PRE2[0] = ''
	FILT_BW_FINE1[0] = ''
	FILT_BW_FINE2[0] = ''
	
	PRE_CHARGE_WIDTH[0] = ''
	MAX_TIA_TIME_CONST[0] = ''
	Max_time_const_val[0] = 0
	
	# # # # Per Phase Parameters
	No_of_Phases_PerPhase[0] = 0
	
	LED1_ON_TIME_GLOBAL[0] = 0
	LED2_ON_TIME_GLOBAL[0] = 0
	
	FS_LED_CURRENT_global[0] = 0
	Full_Scale_AMB_DAC_global[0] = 0
	
	AMB_Cancellation_scheme_global[0] = 2
	Maximum_no_of_TIAs_global.setCurrentIndex(0)
	phaseTiming_mode[0] = 5
	
	LED1_On_Label.setCurrentIndex(0)
	LED2_On_Label.setCurrentIndex(0)
	
