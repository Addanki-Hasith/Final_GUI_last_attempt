class PhaseTiming(QtGui.QWidget):
	def __init__(self):
		super(PhaseTiming,self).__init__()

# 		Required Widgets
		self.title 						= QtGui.QLabel('PHASE TIMING SCHEME')
		self.stagger_mode 				= QtGui.QRadioButton("Stagger Mode")
		self.high_prf_mode 				= QtGui.QRadioButton("High PRF Mode")
		self.max_amb_rej_mode 			= QtGui.QRadioButton("Max AMB Rej Mode")
		self.dis_post_amb_rej_mode 		= QtGui.QRadioButton("Dis-POST AMB Rej ")

# 		Setting ToolTips
		settingToolTip(		self.title,					"Configuration of Phase Timing Scheme required")
		settingToolTip(		self.stagger_mode,			"Selecting Stagger Mode")
		settingToolTip(		self.high_prf_mode,			"Selecting High PRF Mode")
		settingToolTip(		self.max_amb_rej_mode,		"Selecting Maximum Ambient Rejection Mode")
		settingToolTip(		self.dis_post_amb_rej_mode,	"Selecting Disable-Post Ambient Rejection Mode")
		
# 		Styling of each widget			
		titles_styling(					self.title)
		normal_radioButton_styling(		self.stagger_mode)
		normal_radioButton_styling(		self.high_prf_mode)
		normal_radioButton_styling(		self.max_amb_rej_mode)
		normal_radioButton_styling(		self.dis_post_amb_rej_mode)
		
		self.opacity_effect 		= QtGui.QGraphicsOpacityEffect()
		self.opacity_effect.setOpacity(0.5)
		self.title.setGraphicsEffect(self.opacity_effect)
		
# 		Resizing 		
		resizingPolicy(		self.title)
		resizingPolicy(		self.stagger_mode)
		resizingPolicy(		self.high_prf_mode)
		resizingPolicy(		self.max_amb_rej_mode)
		resizingPolicy(		self.dis_post_amb_rej_mode)
		
# 		Grouping Radio Buttons			
		self.main_grp 				= QtGui.QButtonGroup()
		self.main_grp.addButton(	self.stagger_mode)
		self.main_grp.addButton(	self.high_prf_mode)
		self.main_grp.addButton(	self.max_amb_rej_mode)
		self.main_grp.addButton(	self.dis_post_amb_rej_mode)

# 		Layouts and Arrangement			
		self.MainLay 				= QtGui.QGridLayout()
		self.MainLay.addWidget(		self.title,						0,0,1,4)
		self.MainLay.addWidget(		self.stagger_mode,				1,0,1,3)
		self.MainLay.addWidget(		self.high_prf_mode,				2,0,1,3)
		self.MainLay.addWidget(		self.max_amb_rej_mode,			3,0,1,3)
		self.MainLay.addWidget(		self.dis_post_amb_rej_mode,		4,0,1,3)
		
# 		setting the widget layout		
		self.setLayout(self.MainLay)
# 		Widget Background Styling	
		Widget_Background(self)

# 		internal configurations
		self.stagger_mode.clicked.connect(self.mode_0)

		self.high_prf_mode.clicked.connect(self.mode_1)

		self.max_amb_rej_mode.clicked.connect(self.mode_2)

		self.dis_post_amb_rej_mode.clicked.connect(self.mode_3)
		
	def mode_0(self):
# 		self.disable_select()
		AFE_config_phaseTimingScheme(STAGGER_mode)

	def mode_1(self):
# 		self.disable_select()
		AFE_config_phaseTimingScheme(HIGH_PRF_MODE_mode)
		
	def mode_2(self):
# 		self.disable_select()
		AFE_config_phaseTimingScheme(MAX_AMB_REJ_mode)
		
	def mode_3(self):
# 		self.disable_select()		
		AFE_config_phaseTimingScheme(DIS_POST_AMB_MAX_AMB_REJ_mode)

	def PhaseTimingEnable(self):
		self.setEnabled(True)
		self.opacity_effect.setEnabled(False)
	
	def PhaseTimingReset(self):
		self.setEnabled(False)
		self.opacity_effect.setEnabled(True)
		self.stagger_mode.setChecked(False)
		self.high_prf_mode.setChecked(False)
		self.max_amb_rej_mode.setChecked(False)
		self.dis_post_amb_rej_mode.setChecked(False)

class Clocking(QtGui.QWidget):
	def __init__(self):
		super(Clocking,self).__init__()

# 		Required Widgets
		self.title 						= QtGui.QLabel('CLOCKING MODE')
		self.internal 					= QtGui.QRadioButton('CLK_MODE_INT')
		self.external 					= QtGui.QRadioButton('CLC_MODE_EXT')
		self.singleshot 				= QtGui.QRadioButton('CLC_MODE_SS')
		self.mixedclock 				= QtGui.QRadioButton('CLC_MODE_MIX')
		self.ExternalClk 				= QtGui.QLabel('External Clk Frequency')
		self.SelExternal				= QtGui.QComboBox()
		self.SelExternal_Mix 			= QtGui.QComboBox()
		self.SelExternal.addItems(		['256 KHz', '512 KHz', '1024 KHz'])
		self.SelExternal_Mix.addItems(	['32.768 KHz'])
		
# 		Setting ToolTips
		settingToolTip(		self.title,			"Configuration of Clocking Mode Required")
		settingToolTip(		self.internal,		"Selecting Internal Clock")
		settingToolTip(		self.external,		"Selecting External Clock")
		settingToolTip(		self.singleshot,	"Selecting Single Shot Mode Clock")
		settingToolTip(		self.mixedclock,	"Selecting Mixed Clock")
		settingToolTip(		self.ExternalClk,	"Select the external clock required")
		
# 		Styling of each widget		
		titles_styling(					self.title)
		normal_radioButton_styling(		self.internal)
		normal_radioButton_styling(		self.external)
		normal_radioButton_styling(		self.singleshot)
		normal_radioButton_styling(		self.mixedclock)
		UnderlineLabel_styling(			self.ExternalClk)
		
# 		Resizing 		
		resizingPolicy(		self.title)
		resizingPolicy(		self.internal)
		resizingPolicy(		self.external)
		resizingPolicy(		self.singleshot)
		resizingPolicy(		self.mixedclock)
		resizingPolicy(		self.ExternalClk)
		resizingPolicy(		self.SelExternal)
		resizingPolicy(		self.SelExternal_Mix)
		
# 		Grouping Radio Buttons			
		self.main_grp    			= QtGui.QButtonGroup()
		self.main_grp.addButton(	self.internal)
		self.main_grp.addButton(	self.external)
		self.main_grp.addButton(	self.singleshot)
		self.main_grp.addButton(	self.mixedclock)
		
# 		Layouts and Arrangement			
		self.extCLk_wid = QtGui.QStackedWidget()
		self.extCLk_wid.addWidget(self.SelExternal)
		self.extCLk_wid.addWidget(self.SelExternal_Mix)
		
		self.HBox = QtGui.QHBoxLayout()
		self.HBox.addWidget(self.ExternalClk)
		self.HBox.addWidget(self.extCLk_wid)
		
		self.MainLay = QtGui.QGridLayout()
		self.MainLay.addWidget(self.title,0,0,1,4)
		self.MainLay.addWidget(self.internal,1,0,1,3)
		self.MainLay.addWidget(self.external,2,0,1,3)
		self.MainLay.addWidget(self.singleshot,3,0,1,3)
		self.MainLay.addWidget(self.mixedclock,4,0,1,3)
		self.MainLay.addLayout(self.HBox,5,0,1,4)
		
# 		setting the widget layout		
		self.setLayout(self.MainLay)
# 		Widget Background Styling	
		Widget_Background(self)


# 		internal configurations
		self.opacity_effect = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect.setOpacity(0.3)
		self.ExternalClk.setGraphicsEffect(self.opacity_effect)
		self.SelExternal.setEnabled(False)
		self.SelExternal_Mix.setEnabled(False)
		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect1.setOpacity(0.5)
		self.title.setGraphicsEffect(self.opacity_effect1)
		
		self.internal.clicked.connect(self.mode_0)

		self.external.clicked.connect(self.mode_1)

		self.singleshot.clicked.connect(self.mode_2)

		self.mixedclock.clicked.connect(self.mode_3)
		
		self.SelExternal.currentIndexChanged.connect(self.external_clock_index)
		
		
	def mode_0(self):
		self.opacity_effect.setEnabled(True)
		self.SelExternal.setEnabled(False)
		self.SelExternal_Mix.setEnabled(False)
		AFE_config_clockingMode(CLK_MODE_INT)
	def mode_1(self):
		self.extCLk_wid.setCurrentIndex(0)
		self.opacity_effect.setEnabled(False)
		self.SelExternal.setEnabled(True)
		self.SelExternal_Mix.setEnabled(False)
		AFE_config_clockingMode(CLK_MODE_EXT)
	def mode_2(self):
		self.opacity_effect.setEnabled(True)
		self.SelExternal.setEnabled(False)
		self.SelExternal_Mix.setEnabled(False)
		AFE_config_clockingMode(CLK_MODE_SS)
	
	def mode_3(self):
		self.extCLk_wid.setCurrentIndex(1)
		self.opacity_effect.setEnabled(False)
		self.SelExternal.setEnabled(False)
		self.SelExternal_Mix.setEnabled(True)		
		AFE_config_clockingMode(CLK_MODE_MIX)	
	
	def external_clock_index(self,i):
		if i == 0:
			AFE_config_extClkDecimation(external_clk_NoDecimation)
			logWindow_wid.settingLogText('External Clock of 256 KHz is selected')
		elif i == 1:
			AFE_config_extClkDecimation(external_clk_Decimation_2)
			logWindow_wid.settingLogText('External Clock of 512 KHz is selected')
		elif i == 2:
			AFE_config_extClkDecimation(external_clk_Decimation_4) 
			logWindow_wid.settingLogText('External Clock of 1024 KHz is selected')
		
		self.SelExternal.setEnabled(True)
	
	def ClockingEnable(self):
		self.setEnabled(True)
		self.opacity_effect1.setEnabled(False)
	
	def ClockingReset(self):	
		self.setEnabled(False)
		self.opacity_effect1.setEnabled(True)
		self.internal.setChecked(False)
		self.external.setChecked(False)
		self.singleshot.setChecked(False)
		self.mixedclock.setChecked(False)
		
		self.SelExternal.setEnabled(False)
		self.SelExternal_Mix.setEnabled(False)

class TimingParameters(QtGui.QWidget):
	def __init__(self):
		super(TimingParameters,self).__init__()		

# 		Required Widgets
		self.parName1 		= QtGui.QLabel('PRF (Hz)')
		self.parName2 		= QtGui.QLabel('STEP COUNT')
		self.label1 		= QtGui.QLabel('PRPCT value')
		self.label2 		= QtGui.QLabel('Exact PRF assigned')
		self.userval1 		= QtGui.QLineEdit()
		self.userval1.setPlaceholderText('Enter PRF Frequency')
		self.userval2 		= QtGui.QLineEdit()
		self.userval2.setPlaceholderText('Enter Step Count')

# 		Setting ToolTips
		settingToolTip(		self.parName1,	"Configuration of required Step Count")
		settingToolTip(		self.parName2,	"Configuration of requited PRF Frequency")
		settingToolTip(		self.userval1,	"Enter values between 4Hz and 256 KHz")
		settingToolTip(		self.userval2,	"Enter values between 1 and 128")
		settingToolTip(		self.label1,	"Exact PRF that is assigned")
		settingToolTip(		self.label2,	"Assigned PRPCT value")	
		
# 		Styling of each widget			
		titles_styling(			self.parName1)
		titles_styling(			self.parName2)
		AutoAssignedLabel(		self.label1)
		AutoAssignedLabel(		self.label2)
		lineEditStyling(			self.userval1)
		lineEditStyling(			self.userval2)
		
		TextAlignCenter(		self.parName1)
		TextAlignCenter(		self.parName2)
		TextAlignCenter(		self.label1)
		TextAlignCenter(		self.label2)
		TextAlignCenter(		self.userval1)
		TextAlignCenter(		self.userval2)
		
# 		Resizing 		
		resizingPolicy(			self.parName1)
		resizingPolicy(			self.parName2)
		resizingPolicy(			self.label1)
		resizingPolicy(			self.label2)
		lineEditPolicy(			self.userval1)
		lineEditPolicy(			self.userval2)
		
# 		Layouts and Arrangement					
		self.MainLay = QtGui.QGridLayout()
		self.MainLay.addWidget(self.parName2,0,0,1,2)
		self.MainLay.addWidget(self.userval2,0,2,1,2)
		self.MainLay.addWidget(self.parName1,1,0,1,2)
		self.MainLay.addWidget(self.userval1,1,2,1,2)
		self.MainLay.addWidget(self.label1,2,0,1,4)
		self.MainLay.addWidget(self.label2,3,0,1,4)
		
# 		setting the widget layout		
		self.setLayout(self.MainLay)
# 		Widget Background Styling	
		Widget_Background(self)
		
# 		internal configurations
		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect1.setOpacity(0.3)
		
		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect2.setOpacity(0.3)
		self.opacity_effect3 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect3.setOpacity(0.3)
		self.opacity_effect4 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect4.setOpacity(0.3)
		self.parName1.setGraphicsEffect(self.opacity_effect1)
		self.parName2.setGraphicsEffect(self.opacity_effect2)
		
		self.label1.setGraphicsEffect(self.opacity_effect3)
		self.label2.setGraphicsEffect(self.opacity_effect4)
		
		self.userval1.setEnabled(False)
		self.userval2.setEnabled(True)
		self.userval1.editingFinished.connect(self.textChange_1)
		self.userval1.textChanged.connect(self.prf_changing)
		self.userval2.editingFinished.connect(self.textChange_2)
		self.userval2.textChanged.connect(self.stepcount_changing)
		
		self.onlyDouble = QtGui.QDoubleValidator()
		self.userval1.setValidator(self.onlyDouble)
		self.onlyDouble.setNotation(QtGui.QDoubleValidator.StandardNotation)
		self.onlyDouble.setRange(4,256000.000,decimals = 3)
		
		self.onlyInt = QtGui.QIntValidator()
		self.userval2.setValidator(self.onlyInt)
		self.onlyInt.setRange(1,128)
		
		self.prf_assigned = False
		self.stepcount_assigned = False
	
	def prf_changing(self):
		self.opacity_effect3.setEnabled(True)
		self.opacity_effect4.setEnabled(True)	
		self.prf_assigned = False
		
	def stepcount_changing(self):
		self.opacity_effect3.setEnabled(True)
		self.opacity_effect4.setEnabled(True)	
		self.stepcount_assigned = False
	
	def textChange_2(self):
		self.userval2.clearFocus()
		self.stepcount_assigned = True
		if self.prf_assigned:
			self.opacity_effect3.setEnabled(False)
			self.opacity_effect4.setEnabled(False)
		self.opacity_effect1.setEnabled(False)
		self.userval1.setEnabled(True)
		
		val = int(str(self.userval2.text()))
		AFE_config_stepcount(val)
		logWindow_wid.settingLogText('Step Count is assigned with a value of ' + str(val))
		
	def textChange_1(self):
		self.prf_assigned = True
		
		self.opacity_effect3.setEnabled(False)
		self.opacity_effect4.setEnabled(False)	
		
		val2 = float(str(self.userval1.text()))
		
		finalVal = AFE_config_prpct(val2)
		
		self.label1.setText('PRPCT = ' + str(int(finalVal[0])) )
		self.label2.setText('Exact PRF is ' + str(finalVal[1]) + ' Hz')
		logWindow_wid.settingLogText('PRF assignment')
	
	def TimingParametersEnable(self):
		self.setEnabled(True)
		self.opacity_effect2.setEnabled(False)
	
	def TimingParametersReset(self):	
		self.setEnabled(False)
		self.opacity_effect1.setEnabled(True)
		self.opacity_effect2.setEnabled(True)
		self.opacity_effect3.setEnabled(True)
		self.opacity_effect4.setEnabled(True)	
		
		self.userval1.clear()
		self.userval2.clear()
		self.label1.setText('PRPCT value')
		self.label2.setText('Exact PRF assigned')
		
		self.userval1.setEnabled(False)
		
class ReConv_N_AMBCancelScheme(QtGui.QWidget):
	def __init__(self):
		super(ReConv_N_AMBCancelScheme,self).__init__()

# 		Required Widgets
		self.ReConvThre 		= QtGui.QLabel('ReConvergence \nThreshold (V)')
		self.AMBCancel 			= QtGui.QLabel('AMB Cancellation \nScheme')
		self.userVal1 			= QtGui.QLineEdit()
		self.userVal2 			= QtGui.QComboBox()
		self.userVal2.addItems(['None', 'ANA-AACM','MCU Ctrl'])
		self.userVal1.setPlaceholderText('Enter in Volts')
		
# 		Setting ToolTips
		settingToolTip(		self.ReConvThre,		"Configuration of Reconvergence Threshold Voltage")
		settingToolTip(		self.AMBCancel,			"Configuration of Ambient Cancellation Scheme")
		settingToolTip(		self.userVal1,			"Enter values between 0.0 V and 1.2 V")
		
# 		Styling of each widget			
		titles_styling(		self.ReConvThre)
		titles_styling(		self.AMBCancel)
		lineEditStyling(	self.userVal1)
		
		TextAlignCenter(	self.ReConvThre)
		TextAlignCenter(	self.AMBCancel)
		TextAlignCenter(	self.userVal1)
		
# 		Resizing 		
		resizingPolicy(		self.ReConvThre)
		resizingPolicy(		self.AMBCancel)
		resizingPolicy(		self.userVal2)
		lineEditPolicy(		self.userVal1)
		
# 		Layouts and Arrangement			
		self.MainLay = QtGui.QGridLayout()
		self.MainLay.addWidget(self.ReConvThre,0,0,1,1)
		self.MainLay.addWidget(self.userVal1,0,1,1,1)
		self.MainLay.addWidget(self.AMBCancel,1,0,1,1)
		self.MainLay.addWidget(self.userVal2,1,1,1,1)
		
# 		setting the widget layout		
		self.setLayout(self.MainLay)
		
# 		Widget Background Styling	
		Widget_Background(self)
		
# 		internal configurations		
		self.userVal2.currentIndexChanged.connect(self.ABM_index)
		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect1.setOpacity(0.3)
		
		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect2.setOpacity(0.3)
		
		self.ReConvThre.setGraphicsEffect(self.opacity_effect1)
		self.AMBCancel.setGraphicsEffect(self.opacity_effect2)
		
		self.onlyDouble = QtGui.QDoubleValidator()
		self.userVal1.setValidator(self.onlyDouble)
		self.onlyDouble.setNotation(QtGui.QDoubleValidator.StandardNotation)
		self.onlyDouble.setRange(0.0,1.200,decimals = 3)
		
		self.userVal1.editingFinished.connect(self.ReConvTextChanged)
		
		
	def ReConvTextChanged(self):
		self.userVal1.clearFocus()
		self.userVal1.setEnabled(True)
		self.opacity_effect2.setEnabled(False)
		self.userVal2.setEnabled(True)
		
		val = float(str(self.userVal1.text()))
		regVal = AFE_config_ReConvThre(val)
		
		logWindow_wid.settingLogText('Re-Convergence Threshold Voltage is set with REG_RECONV_THR_LED_DC register value at ' + str(int(regVal)))
		
	def ABM_index(self,i):
		self.userVal2.setEnabled(True)
		if i ==0:
			logWindow_wid.settingLogText('Choose correct Ambient Cancellation Scheme')
			AMB_Cancellation_scheme_global.clear()
		elif i==1:
			logWindow_wid.settingLogText('Analog Automatic Ambient Cancellation Mode is chosen')
			AMB_Cancellation_scheme_global[0] = ANA_AACM_scheme
		elif i==2:
			logWindow_wid.settingLogText('MCU control is chosen')
			AMB_Cancellation_scheme_global[0] = MCU_control_scheme
		
	def ReConv_N_AMBCancelSchemeEnable(self):
		self.setEnabled(True)
		self.opacity_effect1.setEnabled(False)
	
	def ReConv_N_AMBCancelSchemeReset(self):	
		self.setEnabled(False)
		self.opacity_effect1.setEnabled(True)	
		self.opacity_effect2.setEnabled(True)	
		self.userVal1.clear()
		self.userVal2.setCurrentIndex(0)
		self.userVal2.setEnabled(False)

class VerticalLabel(QtGui.QLabel):

	def __init__(self, *args):
		QtGui.QLabel.__init__(self, *args)

	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.translate(0, self.height())
		painter.rotate(-90)
		# calculate the size of the font
		fm = QtGui.QFontMetrics(painter.font())
		xoffset = int(fm.boundingRect(self.text()).width()/2)
		yoffset = int(fm.boundingRect(self.text()).height()/2)
		x = int(self.width()/2) + yoffset
		y = int(self.height()/2) - xoffset
		# because we rotated the label, x affects the vertical placement, and y affects the horizontal
		painter.drawText(y, x, self.text())
		painter.end()
		
	def minimumSizeHint(self):
		size = QtGui.QLabel.minimumSizeHint(self)
		return QtCore.QSize(size.height(), size.width())

	def sizeHint(self):
		size = QtGui.QLabel.sizeHint(self)
		return QtCore.QSize(size.height(), size.width())



class Receiver_transmitter(QtGui.QWidget):
	def __init__(self):
		super(Receiver_transmitter,self).__init__()		
		
		self.micro_char 	= unichr(int('b5',16)) # micro
		self.sign_sym = unichr(int('b1',16))  # + -

# 		Required Widgets
		self.maxNoTIAS 						= QtGui.QLabel('Max No. of TIAs')
		self.maxNoTIASVal 					= QtGui.QComboBox()
		self.maxNoTIASVal.addItems(			['None','1','2','3','4'])
		self.commonWid 						= QtGui.QRadioButton('Common')
		self.TIA1 							= QtGui.QRadioButton('TIA1')
		self.TIA2 							= QtGui.QRadioButton('TIA2')
		self.TIA3 							= QtGui.QRadioButton('TIA3')
		self.TIA4 							= QtGui.QRadioButton('TIA4')
		
		self.PPGLabel 						= QtGui.QLabel('4 PPG RX Channels')
		self.LEDsLabel 						= QtGui.QLabel('4x8 LEDs')
		
		self.IFS_OFFDAC 					= QtGui.QLabel('IFS AMB OFFSET DAC')
		self.IFS_OFFDAC_COMBO 				= QtGui.QComboBox()
		
		self.EnableLEDOFFDAC 				= QtGui.QLabel('EN_LED_OFFDAC')
		self.EnableLEDOFFDACYes 			= QtGui.QRadioButton('Yes')
		self.EnableLEDOFFDACNo 				= QtGui.QRadioButton('No')
		
		self.polarity 						= QtGui.QLabel('Polarity of OFFDAC')
		self.polarityForm 					= QtGui.QComboBox()
		self.polarityForm.addItems(			['None',"INP - PD's Cathode","INM - PD's Cathode"])
		
		self.offdacPD 						= QtGui.QLabel('IOFFDAC_PD')
		self.offdacPD1 						= QtGui.QLineEdit()
		self.offdacPD2 						= QtGui.QLineEdit()
		self.offdacPD3 						= QtGui.QLineEdit()		
		self.offdacPD4						= QtGui.QLineEdit()
		
		self.FSLEDCurrent 					= QtGui.QLabel('LED full scale\nCurrent')
		self.FSLEDCurrentCombo 				= QtGui.QComboBox()
		self.FSLEDCurrentCombo.addItems(	['none','25 mA','50 mA','100 mA','125 mA','167 mA'])
		
		self.LEDOnTime 						= QtGui.QLabel('LED ON Time for Filter')
		self.LEDOnTimeCombo 				= QtGui.QComboBox()
		self.LEDOnTimeCombo.addItems(		['none','16'+self.micro_char+'s','23'+self.micro_char+'s','31'+self.micro_char+'s','39'+self.micro_char+'s','47'+self.micro_char+'s','63'+self.micro_char+'s','70'+self.micro_char+'s','78'+self.micro_char+'s','94'+self.micro_char+'s','117'+self.micro_char+'s'])
		
		self.LEDOnTimeCommon 				= QtGui.QRadioButton('Common')
		self.LEDOnTimeSet1 					= QtGui.QRadioButton('Set1')
		self.LEDOnTimeSet2 					= QtGui.QRadioButton('Set2')
		
		self.FIFO_rdy_int 					= QtGui.QLabel('# of PRF in FIFO_RDY INT')
		self.FIFO_rdy_intLabel 				= QtGui.QLineEdit()
		
		self.FIFO_WaterMark 				= VerticalLabel('FIFO Water Mark level')
	
		self.filterBWPre 					= QtGui.QLabel('Filter_BW_PRE')
		self.filterBWFine 					= QtGui.QLabel('Filter_BW_FINE')
		self.MaxTIATimeConst 				= QtGui.QLabel('Max TIA time Const')
		self.FilterPreChargeWidth 			= QtGui.QLabel('Filter PRE Charge Width')
		
		self.svgWidget 						= QtSvg.QSvgWidget(APP_DIR+"/AFE4460_Global.svg")
		
		
# 		Setting ToolTips
		settingToolTip(		self.maxNoTIAS,				"select maximum no. of TIAs required")
		settingToolTip(		self.commonWid,				"common configuration of all TIAs")
		settingToolTip(		self.TIA1,					"configuration of TIA1")
		settingToolTip(		self.TIA2,					"configuration of TIA2")
		settingToolTip(		self.TIA3,					"configuration of TIA3")
		settingToolTip(		self.TIA4,					"configuration of TIA4")
		settingToolTip(		self.offdacPD,				"configuration of OFFSET DAC current in each PD")
		settingToolTip(		self.polarity,				"select the Polarity in which PD to be connected")
		settingToolTip(		self.EnableLEDOFFDACYes,	"Select to Enable LED OFFSET DAC")
		settingToolTip(		self.EnableLEDOFFDACNo,		"Select to Disable LED OFFSET DAC")
		settingToolTip(		self.LEDOnTimeCombo,		"Select the FS Current of Ambient DAC required")
		settingToolTip(		self.FSLEDCurrent,			"Configuration of FS LED Current")
		settingToolTip(		self.FIFO_rdy_int,			"Number of PRD in FIFO Ready")
		settingToolTip(		self.FIFO_WaterMark,		"Assigned FIFO Water Mark Level")
		settingToolTip(		self.filterBWPre,			"Assigned Filter BW in PRE Charge Window")
		settingToolTip(		self.filterBWFine,			"Assigned Filter BW in Fine Settling Window")
		settingToolTip(		self.MaxTIATimeConst,		"Assigned Maximum TIA Time Constant")
		settingToolTip(		self.FilterPreChargeWidth,	"Assigned Pre Charge Width of Filter")

		self.offdacPD1.setPlaceholderText('PD1 (uA)')
		self.offdacPD2.setPlaceholderText('PD2 (uA)')
		self.offdacPD3.setPlaceholderText('PD3 (uA)')
		self.offdacPD4.setPlaceholderText('PD4 (uA)')
		
# 		Styling of each widget			
		receiver_transmitterTitle(		self.maxNoTIAS)
		receiver_transmitterTitle(		self.offdacPD)
		receiver_transmitterTitle(		self.polarity)
		receiver_transmitterTitle(		self.LEDOnTime)
		receiver_transmitterTitle(		self.FSLEDCurrent)
		Boxedlabel_styling(				self.FIFO_rdy_int)
		AutoAssignedLabel(				self.filterBWPre)
		AutoAssignedLabel(				self.filterBWFine)
		AutoAssignedLabel(				self.MaxTIATimeConst)
		AutoAssignedLabel(				self.FilterPreChargeWidth)
# 		AutoAssignedLabel(				self.FIFO_WaterMark)
		self.FIFO_WaterMark.setStyleSheet("margin-left: 10px; border: 1px solid rgba(0,124,140); background: rgba(237,247,248); color: black;")
		self.FIFO_WaterMark.setWordWrap(True)
		
		normal_radioButton_styling(		self.commonWid)
		normal_radioButton_styling(		self.TIA1)
		normal_radioButton_styling(		self.TIA2)
		normal_radioButton_styling(		self.TIA3)
		normal_radioButton_styling(		self.TIA4)
		normal_radioButton_styling(		self.EnableLEDOFFDACYes)
		normal_radioButton_styling(		self.EnableLEDOFFDACNo)
		normal_radioButton_styling(		self.LEDOnTimeCommon)
		normal_radioButton_styling(		self.LEDOnTimeSet1)
		normal_radioButton_styling(		self.LEDOnTimeSet2)
		
		self.LEDsLabel.setStyleSheet(" font-weight:bold;	color: blue")
		self.PPGLabel.setStyleSheet(" font-weight:bold;	color: blue")
		
		lineEditStyling(		self.offdacPD1)
		lineEditStyling(		self.offdacPD2)
		lineEditStyling(		self.offdacPD3)
		lineEditStyling(		self.offdacPD4)
		lineEditStyling(		self.FIFO_rdy_intLabel)

		TextAlignCenter(		self.offdacPD1)
		TextAlignCenter(		self.offdacPD2)
		TextAlignCenter(		self.offdacPD3)
		TextAlignCenter(		self.offdacPD4)
		TextAlignCenter(		self.FIFO_rdy_int)
		TextAlignCenter(		self.FIFO_rdy_intLabel)
		
		self.opacity_effect1		= QtGui.QGraphicsOpacityEffect()
		self.opacity_effect1.setOpacity(0.5)
		self.TIA1.setGraphicsEffect(self.opacity_effect1)
		
		self.opacity_effect2 		= QtGui.QGraphicsOpacityEffect()
		self.opacity_effect2.setOpacity(0.5)
		self.TIA2.setGraphicsEffect(self.opacity_effect2)
		
		self.opacity_effect3		= QtGui.QGraphicsOpacityEffect()
		self.opacity_effect3.setOpacity(0.5)
		self.TIA3.setGraphicsEffect(self.opacity_effect3)
		
		self.opacity_effect4		= QtGui.QGraphicsOpacityEffect()
		self.opacity_effect4.setOpacity(0.5)
		self.TIA4.setGraphicsEffect(self.opacity_effect4)
		
		self.opacity_effect5		= QtGui.QGraphicsOpacityEffect()
		self.opacity_effect5.setOpacity(0.5)
		self.offdacPD.setGraphicsEffect(self.opacity_effect5)
		
		self.opacity_effect6 		= QtGui.QGraphicsOpacityEffect()
		self.opacity_effect6.setOpacity(0.5)
		self.offdacPD1.setGraphicsEffect(self.opacity_effect6)
		
		self.opacity_effect7		= QtGui.QGraphicsOpacityEffect()
		self.opacity_effect7.setOpacity(0.5)
		self.offdacPD2.setGraphicsEffect(self.opacity_effect7)
		
		self.opacity_effect8		= QtGui.QGraphicsOpacityEffect()
		self.opacity_effect8.setOpacity(0.5)
		self.offdacPD3.setGraphicsEffect(self.opacity_effect8)
		
		self.opacity_effect9		= QtGui.QGraphicsOpacityEffect()
		self.opacity_effect9.setOpacity(0.5)
		self.offdacPD4.setGraphicsEffect(self.opacity_effect9)
		
		
# 		Grouping Radio Buttons		
		self.tiaGroup 				= QtGui.QButtonGroup()
		self.tiaGroup.addButton(	self.commonWid)
		self.tiaGroup.addButton(	self.TIA1)
		self.tiaGroup.addButton(	self.TIA2)
		self.tiaGroup.addButton(	self.TIA3)
		self.tiaGroup.addButton(	self.TIA4)
		
		self.ledOnGroup   			= QtGui.QButtonGroup()
		self.ledOnGroup.addButton(	self.LEDOnTimeCommon)
		self.ledOnGroup.addButton(	self.LEDOnTimeSet1)
		self.ledOnGroup.addButton(	self.LEDOnTimeSet2)
		
		self.EnableLEDGroup 			= QtGui.QButtonGroup()
		self.EnableLEDGroup.addButton(	self.EnableLEDOFFDACYes)
		self.EnableLEDGroup.addButton(	self.EnableLEDOFFDACNo)
	
# 		Layouts and Arrangement			
		self.EnableLEDOFFDACLay 				= QtGui.QVBoxLayout()
		self.EnableLEDOFFDACLay.addWidget(		self.EnableLEDOFFDACYes)
		self.EnableLEDOFFDACLay.addWidget(		self.EnableLEDOFFDACNo)
		
		self.polarityLay 						= QtGui.QFormLayout()
		self.polarityLay.addRow(				self.polarity,self.polarityForm)
		
		self.FSLEDCurrentLay 					= QtGui.QHBoxLayout()
		self.FSLEDCurrentLay.addWidget(			self.FSLEDCurrent)
		self.FSLEDCurrentLay.addWidget(			self.FSLEDCurrentCombo)
		
		self.FIFO_rdy_intLay  					= QtGui.QVBoxLayout()
		self.FIFO_rdy_intLay.addWidget(			self.FIFO_rdy_int)
		self.FIFO_rdy_intLay.addWidget(			self.FIFO_rdy_intLabel)
		
		self.tempLay 							= QtGui.QVBoxLayout()
		self.tempLay.addWidget(					self.filterBWPre)
		self.tempLay.addWidget(					self.filterBWFine)
		self.tempLay.addWidget(					self.MaxTIATimeConst)
		self.tempLay.addWidget(					self.FilterPreChargeWidth)
		
		self.PDLay 								= QtGui.QVBoxLayout()
		self.PDLay.addWidget(					self.offdacPD)
		self.PDLay.addWidget(					self.offdacPD1)
		self.PDLay.addWidget(					self.offdacPD2)
		self.PDLay.addWidget(					self.offdacPD3)
		self.PDLay.addWidget(					self.offdacPD4)
		
		self.MainLay2 				= QtGui.QGridLayout()
		self.MainLay2.addWidget(	self.svgWidget,					0,0,21,25)
		self.MainLay2.addWidget(	self.LEDsLabel,					0,11,1,3)
		self.MainLay2.addLayout(	self.FSLEDCurrentLay,			3,11,2,4)
		self.MainLay2.addLayout(	self.polarityLay,				7,0,1,7)
		self.MainLay2.addWidget(	self.LEDOnTime,					9,8,1,3)
		self.MainLay2.addWidget(	self.LEDOnTimeCombo,			9,11,1,1)
		self.MainLay2.addWidget(	self.LEDOnTimeCommon,			9,12,1,2)
		self.MainLay2.addWidget(	self.LEDOnTimeSet1,				10,12,1,2)
		self.MainLay2.addWidget(	self.LEDOnTimeSet2,				11,12,1,2)
		self.MainLay2.addLayout(	self.EnableLEDOFFDACLay,		10,6,1,2)
		self.MainLay2.addWidget(	self.IFS_OFFDAC_COMBO,			11,8,1,1)
		self.MainLay2.addLayout(	self.FIFO_rdy_intLay,			7,16,2,4)
		self.MainLay2.addWidget(	self.FIFO_WaterMark,			7,20,5,3)
		self.MainLay2.addLayout(	self.tempLay,					16,11,2,3)
		self.MainLay2.addLayout(	self.PDLay,						17,14,2,3)
		self.MainLay2.addWidget(	self.PPGLabel,					18,11,1,3)
		self.MainLay2.addWidget(	self.maxNoTIAS,					19,4,1,3)
		self.MainLay2.addWidget(	self.maxNoTIASVal,				19,7,1,1)
		self.MainLay2.addWidget(	self.commonWid,					19,8,1,2)
		self.MainLay2.addWidget(	self.TIA1,						19,10,1,1)
		self.MainLay2.addWidget(	self.TIA2,						19,11,1,1)
		self.MainLay2.addWidget(	self.TIA3,						19,12,1,1)
		self.MainLay2.addWidget(	self.TIA4,						19,13,1,1)
		
		
# 		setting the widget layout		
		self.setLayout(self.MainLay2)

# 		Widget Background Styling	
		Widget_Background(self)

# 		internal configurations		
		
# 		self.maxNoTIAS.setVisible(		False)
# 		self.maxNoTIASVal.setVisible(	False)
		self.TIAn_combo		= 5
		
		self.commonWid.setVisible(		False)
		
# 		self.TIA1.setVisible(			False)
# 		self.TIA2.setVisible(			False)
# 		self.TIA3.setVisible(			False)
# 		self.TIA4.setVisible(			False)
		
		self.TIA1.setEnabled(			False)
		self.TIA2.setEnabled(			False)
		self.TIA3.setEnabled(			False)
		self.TIA4.setEnabled(			False)
		self.maxNoTIASVal.currentIndexChanged.connect(self.MaximumTIA_config)
		self.TIA1.clicked.connect(self.TIA1_FS_AMBconfig)
		self.TIA2.clicked.connect(self.TIA2_FS_AMBconfig)
		self.TIA3.clicked.connect(self.TIA3_FS_AMBconfig)
		self.TIA4.clicked.connect(self.TIA4_FS_AMBconfig)
		self.commonWid.clicked.connect(self.TIA5_FS_AMBconfig)
		
		
		self.IFS_OFFDAC_COMBO.addItem('None')
		self.ifsList = ['15.935','31.875','63.75','127.5','255']
			
		for i in range(5):
			self.ifsList[i] = self.sign_sym + self.ifsList[i] + self.micro_char + 'A'
		self.IFS_OFFDAC_COMBO.addItems(self.ifsList)
		
		self.IFS_OFFDAC_COMBO.currentIndexChanged.connect(self.FullScale_AMBDAC_config)
# 		self.IFS_OFFDAC_COMBO.setVisible(False)
		
# 		self.offdacPD.setVisible(False)
# 		self.offdacPD1.setVisible(False)
# 		self.offdacPD2.setVisible(False)
# 		self.offdacPD3.setVisible(False)
# 		self.offdacPD4.setVisible(False)
# 		
		self.offdacPD1.setEnabled(False)
		self.offdacPD2.setEnabled(False)
		self.offdacPD3.setEnabled(False)
		self.offdacPD4.setEnabled(False)
		
		self.offdacPD1.textChanged.connect(self.iOffDac1_textChanging)
		self.offdacPD2.textChanged.connect(self.iOffDac2_textChanging)
		self.offdacPD3.textChanged.connect(self.iOffDac3_textChanging)
		self.offdacPD4.textChanged.connect(self.iOffDac4_textChanging)
		
		self.offdacPD1.editingFinished.connect(self.iOffDac1_PD)
		self.offdacPD2.editingFinished.connect(self.iOffDac2_PD)
		self.offdacPD3.editingFinished.connect(self.iOffDac3_PD)		
		self.offdacPD4.editingFinished.connect(self.iOffDac4_PD)
		
# 		self.polarity.setVisible(False)
# 		self.polarityForm.setVisible(False)
		
		self.NoOfPDsChecked = [0,0,0,0]
		self.requiredCheck = [1,1,1,1]
		
		self.polarityForm.currentIndexChanged.connect(self.polarity_config)
		
# 		self.EnableLEDOFFDACYes.setVisible(False)
# 		self.EnableLEDOFFDACNo.setVisible(False)
		
		self.EnableLEDOFFDACYes.clicked.connect(self.enabledLEDOFFDAC_config_Yes)
		self.EnableLEDOFFDACNo.clicked.connect(self.enabledLEDOFFDAC_config_No)
		
# 		self.FSLEDCurrent.setVisible(False)
# 		self.FSLEDCurrentCombo.setVisible(False)
		self.FSLEDCurrentCombo.currentIndexChanged.connect(self.FS_LED_Current_config)
		
# 		self.LEDOnTime.setVisible(False)
# 		self.LEDOnTimeCombo.setVisible(False)
# 		self.LEDOnTimeCommon.setVisible(False)
# 		self.LEDOnTimeSet1.setVisible(False)
# 		self.LEDOnTimeSet2.setVisible(False)
# 		
# 		self.filterBWPre.setVisible(False)
# 		self.filterBWFine.setVisible(False)
# 		self.MaxTIATimeConst.setVisible(False)
# 		self.FilterPreChargeWidth.setVisible(False)
		
		self.LEDOnTimeCombo.setEnabled(False)
		
		self.combo_set_sel = 3
		
		self.LEDOnTimeCommon.clicked.connect(self.LEDOnTime_combo_sel)
		self.LEDOnTimeSet1.clicked.connect(self.LEDOnTime_combo_set1)
		self.LEDOnTimeSet2.clicked.connect(self.LEDOnTime_combo_set2)
		self.LEDOnTimeCombo.currentIndexChanged.connect(self.LEDCombo_config)
		
# 		self.FIFO_rdy_int.setVisible(False)
# 		self.FIFO_rdy_intLabel.setVisible(False)
# 		self.FIFO_WaterMark.setVisible(False)
# 		self.PPGLabel.setVisible(False)
		
		self.opacity_effect_main		= QtGui.QGraphicsOpacityEffect()
		self.opacity_effect_main.setOpacity(0.5)
		self.setGraphicsEffect(self.opacity_effect_main)
		self.setEnabled(False)
	def maxNoTIAs_Enable(self):
		self.opacity_effect_main.setEnabled(False)
		self.setEnabled(True)
		self.maxNoTIAS.setVisible(		True)
		self.maxNoTIASVal.setVisible(	True)
		
	def TIA1_FS_AMBconfig(self):
		self.TIAn_combo = 1
	def TIA2_FS_AMBconfig(self):
		self.TIAn_combo = 2
	def TIA3_FS_AMBconfig(self):
		self.TIAn_combo = 3
	def TIA4_FS_AMBconfig(self):
		self.TIAn_combo = 4
	def TIA5_FS_AMBconfig(self):
		self.TIAn_combo = 5
	
	def MaximumTIA_config(self,i):
		self.IFS_OFFDAC_COMBO.setCurrentIndex(0)
# 		self.offdacPD1.clear()
# 		self.offdacPD2.clear()
# 		self.offdacPD3.clear()
# 		self.offdacPD4.clear()
		
		if i==0:
			self.commonWid.setVisible(		False)
			self.TIA1.setVisible(			False)
			self.TIA2.setVisible(			False)
			self.TIA3.setVisible(			False)
			self.TIA4.setVisible(			False)
			
			self.opacity_effect1.setEnabled(True)
			self.opacity_effect2.setEnabled(True)			
			self.opacity_effect3.setEnabled(True)
			self.opacity_effect4.setEnabled(True)
			self.IFS_OFFDAC_COMBO.setVisible(False)
			
		else:
			self.PPGLabel.setVisible(True)
			AFE_config_maxNoOfTIAs(	i )
			
			self.commonWid.setVisible(		True)
			self.TIA1.setVisible(			True)
			self.TIA2.setVisible(			True)
			self.TIA3.setVisible(			True)
			self.TIA4.setVisible(			True)
# 			
# 			self.IFS_OFFDAC_COMBO.setVisible(True)
# 			self.commonWid.setChecked(True)
			
			if i>0:
				self.opacity_effect1.setEnabled(False)
				self.TIA1.setEnabled(			True)	
				
				self.opacity_effect2.setEnabled(True)			
				self.opacity_effect3.setEnabled(True)
				self.opacity_effect4.setEnabled(True)	
				
				self.TIA2.setEnabled(			False)
				self.TIA3.setEnabled(			False)
				self.TIA4.setEnabled(			False)
			if i>1:
				self.opacity_effect2.setEnabled(False)
				self.TIA2.setEnabled(			True)	
				
				self.opacity_effect3.setEnabled(True)
				self.opacity_effect4.setEnabled(True)
				
				self.TIA3.setEnabled(			False)
				self.TIA4.setEnabled(			False)
			if i>2:
				self.opacity_effect3.setEnabled(False)
				self.TIA3.setEnabled(			True)	
						
				self.opacity_effect4.setEnabled(True)
				
				self.TIA4.setEnabled(			False)
			if i>3:
				self.opacity_effect4.setEnabled(False)
				self.TIA4.setEnabled(			True)	
				
			self.IFS_OFFDAC_COMBO.setVisible(True)
			self.commonWid.setChecked(True)
		
	def FullScale_AMBDAC_config(self,i):
		if i == 0:
			logWindow_wid.settingLogText('Select correct Full Scale AMB DAC Current')
			str = ''
			range = 0
		elif i == 1:
			logWindow_wid.settingLogText('1x correct Full Scale AMB DAC Current')
			AFE_config_fullScaleAMBDAC(		AMB_DAC_FS_15p935uA)
			str_var = 'Enter values between 0 and 15.935 '+ self.micro_char +'A'
			range = 15.935
			
		elif i == 2:
			AFE_config_fullScaleAMBDAC(		AMB_DAC_FS_31p875uA)
			str_var = 'Enter values between 0 and 31.875 '+ self.micro_char +'A'
			range = 31.875
		elif i == 3:
			AFE_config_fullScaleAMBDAC(		AMB_DAC_FS_63p75uA)
			str_var = 'Enter values between 0 and 63.75 '+ self.micro_char +'A'
			range = 63.75
		elif i == 4:
			AFE_config_fullScaleAMBDAC(		AMB_DAC_FS_127p5uA)
			str_var = 'Enter values between 0 and 127.5 '+ self.micro_char +'A'
			range = 127.5
		elif i == 5:
			AFE_config_fullScaleAMBDAC(		AMB_DAC_FS_255uA)
			str_var = 'Enter values between 0 and 255 '+ self.micro_char +'A'
			range = 255
		
		self.offdacPD1.setToolTip(str_var)
		self.offdacPD2.setToolTip(str_var)
		self.offdacPD3.setToolTip(str_var)
		self.offdacPD4.setToolTip(str_var)
		
		self.onlyDouble1 = QtGui.QDoubleValidator()
		self.offdacPD1.setValidator(self.onlyDouble1)
		self.onlyDouble1.setNotation(QtGui.QDoubleValidator.StandardNotation)
		self.onlyDouble1.setRange(0,range,decimals = 3)
		
		self.onlyDouble2 = QtGui.QDoubleValidator()
		self.offdacPD2.setValidator(self.onlyDouble2)
		self.onlyDouble2.setNotation(QtGui.QDoubleValidator.StandardNotation)
		self.onlyDouble2.setRange(0,range,decimals = 3)
		
		self.onlyDouble3 = QtGui.QDoubleValidator()
		self.offdacPD3.setValidator(self.onlyDouble3)
		self.onlyDouble3.setNotation(QtGui.QDoubleValidator.StandardNotation)
		self.onlyDouble3.setRange(0,range,decimals = 3)
		
		self.onlyDouble4 = QtGui.QDoubleValidator()
		self.offdacPD4.setValidator(self.onlyDouble4)
		self.onlyDouble4.setNotation(QtGui.QDoubleValidator.StandardNotation)
		self.onlyDouble4.setRange(0,range,decimals = 3)
		
		self.offdacPD1.clear()
		self.offdacPD2.clear()
		self.offdacPD3.clear()
		self.offdacPD4.clear()
		
		if AMB_Cancellation_scheme_global[0]==1:
			self.offdacPD1.setEnabled(True)
			self.offdacPD2.setEnabled(True)
			self.offdacPD3.setEnabled(True)
			self.offdacPD4.setEnabled(True)
		
		if AMB_Cancellation_scheme_global[0]==0:
			self.polarity.setVisible(True)
			self.polarityForm.setVisible(True)
		
		self.offdacPD.setVisible(True)
		self.offdacPD1.setVisible(True)
		self.offdacPD2.setVisible(True)
		self.offdacPD3.setVisible(True)
		self.offdacPD4.setVisible(True)
	
	def iOffDac1_textChanging(self):
		self.opacity_effect7.setEnabled(True)
		self.opacity_effect8.setEnabled(True)
		self.opacity_effect9.setEnabled(True)
		self.offdacPD2.setEnabled(False)
		self.offdacPD3.setEnabled(False)
		self.offdacPD4.setEnabled(False)
		
		
	def iOffDac2_textChanging(self):
		self.opacity_effect6.setEnabled(True)
		self.opacity_effect8.setEnabled(True)
		self.opacity_effect9.setEnabled(True)
		self.offdacPD1.setEnabled(False)
		self.offdacPD3.setEnabled(False)
		self.offdacPD4.setEnabled(False)
		
		
	def iOffDac3_textChanging(self):
		self.opacity_effect7.setEnabled(True)
		self.opacity_effect6.setEnabled(True)
		self.opacity_effect9.setEnabled(True)
		self.offdacPD1.setEnabled(False)
		self.offdacPD2.setEnabled(False)
		self.offdacPD4.setEnabled(False)

		
	def iOffDac4_textChanging(self):
		self.opacity_effect7.setEnabled(True)
		self.opacity_effect8.setEnabled(True)
		self.opacity_effect6.setEnabled(True)
		self.offdacPD1.setEnabled(False)
		self.offdacPD2.setEnabled(False)
		self.offdacPD3.setEnabled(False)	

			
	def iOffDac1_PD(self):
		self.offdacPD1.clearFocus()
		
		val = float(str(self.offdacPD1.text()))
		AFE_config_pdIOFFDAC(val,0)
		
		self.NoOfPDsChecked[0] = 1
		
		self.opacity_effect7.setEnabled(False)
		self.opacity_effect8.setEnabled(False)
		self.opacity_effect9.setEnabled(False)
		self.offdacPD2.setEnabled(True)
		self.offdacPD3.setEnabled(True)
		self.offdacPD4.setEnabled(True)
		
		if self.NoOfPDsChecked == self.requiredCheck:
			self.polarity.setVisible(True)
			self.polarityForm.setVisible(True)
		
	def iOffDac2_PD(self):
		self.offdacPD2.clearFocus()
		val = float(str(self.offdacPD2.text()))
		AFE_config_pdIOFFDAC(val,1)
		
		self.NoOfPDsChecked[1] = 1
		
		self.opacity_effect6.setEnabled(False)
		self.opacity_effect8.setEnabled(False)
		self.opacity_effect9.setEnabled(False)
		self.offdacPD1.setEnabled(True)
		self.offdacPD3.setEnabled(True)
		self.offdacPD4.setEnabled(True)
		
		if self.NoOfPDsChecked == self.requiredCheck:
			self.polarity.setVisible(True)
			self.polarityForm.setVisible(True)
			
	def iOffDac3_PD(self):
		self.offdacPD3.clearFocus()
		val = float(str(self.offdacPD3.text()))
		AFE_config_pdIOFFDAC(val,2)
		
		self.NoOfPDsChecked[2] = 1		
		
		self.opacity_effect7.setEnabled(False)
		self.opacity_effect6.setEnabled(False)
		self.opacity_effect9.setEnabled(False)
		self.offdacPD1.setEnabled(True)
		self.offdacPD2.setEnabled(True)
		self.offdacPD4.setEnabled(True)
		
		if self.NoOfPDsChecked == self.requiredCheck:
			self.polarity.setVisible(True)
			self.polarityForm.setVisible(True)
			
	def iOffDac4_PD(self):
		self.offdacPD4.clearFocus()
		val = float(str(self.offdacPD4.text()))
		AFE_config_pdIOFFDAC(val,3)
		
		self.NoOfPDsChecked[3] = 1
		
		self.opacity_effect7.setEnabled(False)
		self.opacity_effect8.setEnabled(False)
		self.opacity_effect6.setEnabled(False)
		self.offdacPD1.setEnabled(True)
		self.offdacPD2.setEnabled(True)
		self.offdacPD3.setEnabled(True)
		
		if self.NoOfPDsChecked == self.requiredCheck:
			self.polarity.setVisible(True)
			self.polarityForm.setVisible(True)
		
		
	def polarity_config(self,i):
		if i == 0:
			logWindow_wid.settingLogText('Choose correct polarity')
		elif i == 1:
			AFE_config_polOFFDAC(PD_cathode_INP)
			self.EnableLEDOFFDACYes.setVisible(True)
			self.EnableLEDOFFDACNo.setVisible(True)
		elif i == 2:
			AFE_config_polOFFDAC(PD_cathode_INM)
			self.EnableLEDOFFDACYes.setVisible(True)
			self.EnableLEDOFFDACNo.setVisible(True)
	
	def enabledLEDOFFDAC_config_Yes(self):
		AFE_config_enLEDOFFDAC(True)
		self.FSLEDCurrent.setVisible(True)
		self.FSLEDCurrentCombo.setVisible(True)
		
	def enabledLEDOFFDAC_config_No(self):
		AFE_config_enLEDOFFDAC(False)
		self.FSLEDCurrent.setVisible(True)
		self.FSLEDCurrentCombo.setVisible(True)
	
	def FS_LED_Current_config(self,i):
		if i == 0:
			logWindow_wid.settingLogText('Choose corect option')
			
		else:
			if i==1:
				AFE_config_iLEDFS(FS_LED_25mA)
			elif i==2:
				AFE_config_iLEDFS(FS_LED_50mA)
			elif i==3:
				AFE_config_iLEDFS(FS_LED_100mA)
			elif i==4:
				AFE_config_iLEDFS(FS_LED_125mA)
			elif i==5:
				AFE_config_iLEDFS(FS_LED_167mA)
				
		self.LEDOnTime.setVisible(True)
		self.LEDOnTimeCombo.setVisible(True)
		self.LEDOnTimeCommon.setVisible(True)
		self.LEDOnTimeSet1.setVisible(True)
		self.LEDOnTimeSet2.setVisible(True)
	
	def LEDOnTime_combo_sel(self):
		self.combo_set_sel = 0
		self.LEDOnTimeCombo.setEnabled(True)
	def LEDOnTime_combo_set1(self):
		self.combo_set_sel = 1
		self.LEDOnTimeCombo.setEnabled(True)
	def LEDOnTime_combo_set2(self):
		self.combo_set_sel = 2
		self.LEDOnTimeCombo.setEnabled(True)
		
	def LEDCombo_config(self,i):
		
		self.val = 0
		
		if i==0:
			logWindow_wid.settingLogText('Select correct LED ON time')
			
		else:
			if i == 1:
				self.val = LED_ON_TIMING_16uS
			elif i == 2:
				self.val = LED_ON_TIMING_23uS
			elif i == 3:
				self.val = LED_ON_TIMING_31uS
			elif i == 4:
				self.val = LED_ON_TIMING_39uS
			elif i == 5:
				self.val = LED_ON_TIMING_47uS
			elif i == 6:
				self.val = LED_ON_TIMING_63uS
			elif i == 7:
				self.val = LED_ON_TIMING_70uS
			elif i == 8:
				self.val = LED_ON_TIMING_78uS
			elif i == 9:
				self.val = LED_ON_TIMING_94uS
			elif i == 10:
				self.val = LED_ON_TIMING_117uS
				
			if self.combo_set_sel == 0:
				LED1_ON_TIME_GLOBAL[0] = self.val
				LED2_ON_TIME_GLOBAL[0] = self.val
				AFE_config_LEDONTimes(LED1_ON_TIME_GLOBAL[0],LED2_ON_TIME_GLOBAL[0])
				self.filterBWPre.setVisible(True)
				self.filterBWFine.setVisible(True)
				self.FilterPreChargeWidth.setVisible(True)
				self.MaxTIATimeConst.setVisible(True)
				self.filterBWPre.setText('Filter_BW_Pre-1,2 :'+FILT_BW_PRE1[0])
				self.filterBWFine.setText('Filter_BW_Fine-1,2 :'+FILT_BW_FINE1[0])
				self.FilterPreChargeWidth.setText('Pre Charge Width :'+PRE_CHARGE_WIDTH[0])
				self.MaxTIATimeConst.setText('Max TIA time constant :'+ MAX_TIA_TIME_CONST[0])
				
			elif self.combo_set_sel == 1:
				LED1_ON_TIME_GLOBAL[0] = self.val
				if LED1_ON_TIME_GLOBAL[0]>0 and LED2_ON_TIME_GLOBAL[0]>0:
					AFE_config_LEDONTimes(LED1_ON_TIME_GLOBAL[0],LED2_ON_TIME_GLOBAL[0])
					self.filterBWPre.setVisible(True)
					self.filterBWFine.setVisible(True)
					self.FilterPreChargeWidth.setVisible(True)
					self.MaxTIATimeConst.setVisible(True)
					self.filterBWPre.setText('Filter_BW_Pre-1 :'+FILT_BW_PRE1[0])
					self.filterBWFine.setText('Filter_BW_Fine-1 :'+FILT_BW_FINE1[0])
					self.FilterPreChargeWidth.setText('Pre Charge Width :'+PRE_CHARGE_WIDTH[0])
					self.MaxTIATimeConst.setText('Max TIA time constant :'+ MAX_TIA_TIME_CONST[0])
				
				if LED2_ON_TIME_GLOBAL[0] == 0:
					logWindow_wid.settingLogText('Configure LED2 ON Time')
				
			elif self.combo_set_sel == 2:
				LED2_ON_TIME_GLOBAL[0] = self.val
				if LED1_ON_TIME_GLOBAL[0]>0 and LED2_ON_TIME_GLOBAL[0]>0:
					AFE_config_LEDONTimes(LED1_ON_TIME_GLOBAL[0],LED2_ON_TIME_GLOBAL[0])
					self.filterBWPre.setVisible(True)
					self.filterBWFine.setVisible(True)
					self.FilterPreChargeWidth.setVisible(True)
					self.MaxTIATimeConst.setVisible(True)
					self.filterBWPre.setText('Filter_BW_Pre-2 :'+FILT_BW_PRE2[0])
					self.filterBWFine.setText('Filter_BW_Fine-2 :'+FILT_BW_FINE2[0])
					self.FilterPreChargeWidth.setText('Pre Charge Width :'+PRE_CHARGE_WIDTH[0])
					self.MaxTIATimeConst.setText('Max TIA time constant :'+ MAX_TIA_TIME_CONST[0])
				
				if LED1_ON_TIME_GLOBAL[0] == 0:
					logWindow_wid.settingLogText('Configure LED1 ON Time')
					
					
			
			
		self.FIFO_rdy_int.setVisible(True)
		self.FIFO_rdy_intLabel.setVisible(True)
		self.FIFO_WaterMark.setVisible(True)
		
		
# class PhaseTiming(QtGui.QWidget):
# 	def __init__(self,clock_m):
# 		super(PhaseTiming,self).__init__()
# 		
# 		self.clk_m = clock_m
# 		
# 		self.layout = QtGui.QVBoxLayout()
# 		self.title = QtGui.QLabel('PHASE TIMING SCHEME')
# # 		margin-left: 10px; border: 1px solid black; border-radius: 10px;
# 		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		
# 		self.title.setFixedSize(QtCore.QSize(225,25))
# 		self.title.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.opacity_effect = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect.setOpacity(0.5)
# 		self.title.setGraphicsEffect(self.opacity_effect)
# 		
# 		self.stagger_mode = QtGui.QRadioButton("Stagger Mode")
# 		self.high_prf_mode = QtGui.QRadioButton("High PRF Mode")
# 		self.max_amb_rej_mode = QtGui.QRadioButton("Max AMB Rej Mode")
# 		self.dis_post_amb_rej_mode = QtGui.QRadioButton("Dis-POST AMB Rej ")
# 		
# 		self.stagger_mode.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.high_prf_mode.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.max_amb_rej_mode.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.dis_post_amb_rej_mode.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 																		
# 		self.layout.addWidget(self.title)
# 		self.layout.addWidget(self.stagger_mode)
# 		self.layout.addWidget(self.high_prf_mode)
# 		self.layout.addWidget(self.max_amb_rej_mode)
# 		self.layout.addWidget(self.dis_post_amb_rej_mode)
# 		
# 		self.stagger_mode.setToolTip('Selecting Stagger Mode')
# 		self.high_prf_mode.setToolTip('Selecting High PRF Mode')
# 		self.max_amb_rej_mode.setToolTip('Selecting Maximum Ambient Rejection Mode')
# 		self.dis_post_amb_rej_mode.setToolTip('Selecting Disable-Post Ambient Rejection Mode')
# 		
# 		self.setLayout(self.layout)		
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 		self.setPalette(palette)
# 		
# 		self.stagger_mode.clicked.connect(self.mode_0)
# 
# 		self.high_prf_mode.clicked.connect(self.mode_1)
# 
# 		self.max_amb_rej_mode.clicked.connect(self.mode_2)
# 
# 		self.dis_post_amb_rej_mode.clicked.connect(self.mode_3)
# 		
# 	def mode_0(self):
# # 		self.disable_select()
# 		AFE_config_phaseTimingScheme(STAGGER_mode)
# 		self.clk_m.setEnabled(True)
# 		self.clk_m.opacity_effect1.setEnabled(False)
# 
# 	def mode_1(self):
# # 		self.disable_select()
# 		AFE_config_phaseTimingScheme(HIGH_PRF_MODE_mode)
# 		self.clk_m.setEnabled(True)
# 		self.clk_m.opacity_effect1.setEnabled(False)
# 		
# 	def mode_2(self):
# # 		self.disable_select()
# 		AFE_config_phaseTimingScheme(MAX_AMB_REJ_mode)
# 		self.clk_m.setEnabled(True)
# 		self.clk_m.opacity_effect1.setEnabled(False)
# 		
# 	def mode_3(self):
# # 		self.disable_select()		
# 		AFE_config_phaseTimingScheme(DIS_POST_AMB_MAX_AMB_REJ_mode)
# 		self.clk_m.setEnabled(True)
# 		self.clk_m.opacity_effect1.setEnabled(False)
# # 	def disable_select(self):
# # 		
# # 		self.clk_m.setEnabled(True)
# # 		
# # # 		self.clk_m.opacity_effect1.setEnabled(False)
# # # 		self.stagger_mode.setDisabled(True)
# # # 		self.high_prf_mode.setDisabled(True)
# # # 		self.max_amb_rej_mode.setDisabled(True)
# # # 		self.dis_post_amb_rej_mode.setDisabled(True)
# 	
# 	def PhaseEnable(self):
# 		self.setEnabled(True)
# 		self.opacity_effect.setEnabled(False)
# class Clocking(QtGui.QWidget):
# 	def __init__(self,timePar):
# 		super(Clocking,self).__init__()
# 		
# 		self.timingParameter = timePar
# 		
# 		self.title = QtGui.QLabel('CLOCKING MODE')
# # 		margin-left: 10px; border: 1px solid black; border-radius: 10px;
# 		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.title.setFixedSize(QtCore.QSize(225,25))
# 		self.title.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.internal = QtGui.QRadioButton('CLK_MODE_INT')
# 		self.external = QtGui.QRadioButton('CLC_MODE_EXT')
# 		self.singleshot = QtGui.QRadioButton('CLC_MODE_SS')
# 		self.mixedclock = QtGui.QRadioButton('CLC_MODE_MIX')
# 		
# 		self.internal.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.external.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.singleshot.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.mixedclock.setStyleSheet("QRadioButton::indicator" 
# 										"{"
# 										"width: 20px;"
# 										"height: 20px;"
# 										"}"
# 									"QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"width:12px;"
# 										"height: 12px;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 																																	
# 		self.opacity_effect = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect.setOpacity(0.3)
# 		
# 		self.internal.setToolTip('Selecting Internal Clock')
# 		self.external.setToolTip('Selecting External Clock')
# 		self.singleshot.setToolTip('Selecting Single Shot Mode Clock')
# 		self.mixedclock.setToolTip('Selecting Mixed Clock')
# 		
# 		self.HBox = QtGui.QHBoxLayout()
# 		self.ExternalClk = QtGui.QLabel('External Clk Frequency')
# # 		self.ExternalClk.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: rgba(0,124,140);")
# 		self.ExternalClk.setStyleSheet("background: white; color: rgba(0,124,140);")
# # 		self.extCLk_lay = QtGui.QStackedLayout()
# 		self.extCLk_wid = QtGui.QStackedWidget()
# # 		self.extCLk_wid.setLayout(self.extCLk_lay)
# 		
# 		self.SelExternal = QtGui.QComboBox()
# 		self.SelExternal_Mix = QtGui.QComboBox()
# 		
# 		self.extCLk_wid.addWidget(self.SelExternal)
# 		self.extCLk_wid.addWidget(self.SelExternal_Mix)
# 		self.SelExternal.addItems(['256 KHz', '512 KHz', '1024 KHz'])
# 		self.SelExternal_Mix.addItems(['32.768 KHz'])
# 		
# 		self.ExternalClk.setGraphicsEffect(self.opacity_effect)
# 		self.SelExternal.setEnabled(False)
# 		
# 		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect1.setOpacity(0.5)
# 		
# 		self.title.setGraphicsEffect(self.opacity_effect1)
# 		
# 		self.HBox.addWidget(self.ExternalClk)
# 		self.HBox.addWidget(self.extCLk_wid)
# 
# 		self.layout = QtGui.QVBoxLayout()
# 		self.layout.addWidget(self.title)
# 		self.layout.addWidget(self.internal)
# 		self.layout.addWidget(self.external)
# 		self.layout.addWidget(self.singleshot)
# 		self.layout.addWidget(self.mixedclock)
# 		self.layout.addLayout(self.HBox)
# 		
# 		self.internal.clicked.connect(self.mode_0)
# 		self.internal.clicked.connect(self.timingParEnable)
# 
# 		self.external.clicked.connect(self.mode_1)
# 		self.external.clicked.connect(self.timingParEnable)
# 
# 		self.singleshot.clicked.connect(self.mode_2)
# 		self.singleshot.clicked.connect(self.timingParEnable)
# 
# 		self.mixedclock.clicked.connect(self.mode_3)
# 		self.mixedclock.clicked.connect(self.timingParEnable)
# 		
# 		self.setLayout(self.layout)		
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 		self.setPalette(palette)
# 		
# 		self.SelExternal.currentIndexChanged.connect(self.external_clock_index)
# # 		self.SelExternal_Mix.currentIndexChanged.connect(self.mixed_clock_index)
# 		self.setLayout(self.layout)
# 
# 	def mode_0(self):
# 		self.opacity_effect.setEnabled(True)
# 		self.SelExternal.setEnabled(False)
# 		self.SelExternal_Mix.setEnabled(False)
# # 		self.disable_select()
# 		AFE_config_clockingMode(CLK_MODE_INT)
# 	def mode_1(self):
# 		self.extCLk_wid.setCurrentIndex(0)
# 		self.opacity_effect.setEnabled(False)
# 		self.SelExternal.setEnabled(True)
# 		self.SelExternal_Mix.setEnabled(False)
# 		self.SelExternal.currentIndexChanged.connect(self.timingParEnable)
# # 		self.disable_select()
# 		AFE_config_clockingMode(CLK_MODE_EXT)
# 	def mode_2(self):
# 		self.opacity_effect.setEnabled(True)
# 		self.SelExternal.setEnabled(False)
# 		self.SelExternal_Mix.setEnabled(False)
# 		AFE_config_clockingMode(CLK_MODE_SS)
# # 		self.disable_select()
# 	
# 	def mode_3(self):
# 		self.extCLk_wid.setCurrentIndex(1)
# 		self.opacity_effect.setEnabled(False)
# 		self.SelExternal.setEnabled(False)
# 		self.SelExternal_Mix.setEnabled(True)		
# 		self.timingParEnable()
# # 		self.disable_select()		
# 		AFE_config_clockingMode(CLK_MODE_MIX)
# 	def disable_select(self):
# 		
# 		self.internal.setDisabled(True)
# 		self.external.setDisabled(True)
# 		self.singleshot.setDisabled(True)
# 		self.mixedclock.setDisabled(True)
# 		
# 	def external_clock_index(self,i):
# 		if i == 0:
# 			AFE_config_extClkDecimation(external_clk_NoDecimation)
# 			logWindow_wid.settingLogText('External Clock of 256 KHz is selected')
# 		elif i == 1:
# 			AFE_config_extClkDecimation(external_clk_Decimation_2)
# 			logWindow_wid.settingLogText('External Clock of 512 KHz is selected')
# 		elif i == 2:
# 			AFE_config_extClkDecimation(external_clk_Decimation_4) 
# 			logWindow_wid.settingLogText('External Clock of 1024 KHz is selected')
# 		
# 		self.SelExternal.setEnabled(True)
# 
# # 	def mixed_clock_index(self,i):
# # 		self.SelExternal.setEnabled(True)
# 	
# 	def timingParEnable(self):
# 		self.timingParameter.setEnabled(True)
# 		self.timingParameter.opacity_effect2.setEnabled(False)

# class TimingParameters(QtGui.QWidget):
# 	def __init__(self,ReConvAMB):
# 		super(TimingParameters,self).__init__()
# 		
# 		self.ReConAmbScheme = ReConvAMB
# 		
# 		self.layout = QtGui.QVBoxLayout()
# # 		self.layout = QtGui.QGridLayout()
# 		self.hbox1 = QtGui.QHBoxLayout()
# 		self.hbox2 = QtGui.QHBoxLayout()
# 		
# 		self.label1 = QtGui.QLabel('PRPCT value')
# 		self.label2 = QtGui.QLabel('Exact PRF assigned')
# 		
# 		self.parName1 = QtGui.QLabel('PRF (Hz)')
# 		self.parName2 = QtGui.QLabel('STEP COUNT')
# 		self.parName2.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.parName1.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# # 		self.parName1.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 5px; background: white; color: blue;")
# # 		self.parName2.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 5px; background: white; color: blue;")
# 		
# 		self.parName1.setAlignment(QtCore.Qt.AlignCenter)
# 		self.parName2.setAlignment(QtCore.Qt.AlignCenter)
# 		self.userval1 = QtGui.QLineEdit()
# 		self.userval1.setPlaceholderText('Enter PRF Frequency')
# 		self.userval1.setToolTip('Enter values between 4Hz and 256 KHz')
# 		self.userval1.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.userval2 = QtGui.QLineEdit()
# 		self.userval2.setPlaceholderText('Enter Step Count')
# 		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
# 		self.userval2.setSizePolicy(sizePolicy)
# 		self.userval1.setSizePolicy(sizePolicy)
# 		self.userval2.setToolTip('Enter values between 1 and 128')
# 		self.userval2.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.hbox1.addWidget(self.parName1)
# 		
# 		self.hbox1.addWidget(self.userval1)
# 		
# 		self.hbox2.addWidget(self.parName2)
# 		self.hbox2.addWidget(self.userval2)
# 
# 		self.layout.addLayout(self.hbox2)
# 		self.layout.addLayout(self.hbox1)
# 		
# 		
# 		self.label1.setStyleSheet("margin-left: 10px; border: 1px solid rgba(0,124,140); border-radius: 5px; background: rgba(237,247,248); color: black;")
# 		self.label2.setStyleSheet("margin-left: 10px; border: 1px solid rgba(0,124,140); border-radius: 5px; background: rgba(237,247,248); color: black;")
# 		
# 		self.label1.setAlignment(QtCore.Qt.AlignCenter)
# 		self.label2.setAlignment(QtCore.Qt.AlignCenter)
# 		self.layout.addWidget(self.label1)
# 		self.layout.addWidget(self.label2)
# 		
# 		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect1.setOpacity(0.3)
# 		
# 		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect2.setOpacity(0.3)
# 		self.opacity_effect3 = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect3.setOpacity(0.3)
# 		self.opacity_effect4 = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect4.setOpacity(0.3)
# 		self.parName1.setGraphicsEffect(self.opacity_effect1)
# 		self.parName2.setGraphicsEffect(self.opacity_effect2)
# 		
# 		self.label1.setGraphicsEffect(self.opacity_effect3)
# 		self.label2.setGraphicsEffect(self.opacity_effect4)
# 		
# 		self.userval1.setEnabled(False)
# 		self.userval2.setEnabled(True)
# 		self.userval1.editingFinished.connect(self.textChange_1)
# 		self.userval1.textChanged.connect(self.prf_changing)
# 		self.userval2.editingFinished.connect(self.textChange_2)
# 		self.userval2.textChanged.connect(self.stepcount_changing)
# 		
# 		self.onlyDouble = QtGui.QDoubleValidator()
# 		self.userval1.setValidator(self.onlyDouble)
# 		self.onlyDouble.setNotation(QtGui.QDoubleValidator.StandardNotation)
# 		self.onlyDouble.setRange(4,256000.000,decimals = 3)
# 		
# 		self.userval1.setStyleSheet("QLineEdit"
# 								"{"
# 								"border :1px solid black;"
# 								"}"
# 								"QLineEdit::focus"
# 								"{"
# 								"border-color : red ;"
# 								"background-color : #edf7f8;"
# 								"}")
# 		self.userval2.setStyleSheet("QLineEdit"
# 								"{"
# 								"border :1px solid black;"
# 								"}"
# 								"QLineEdit::focus"
# 								"{"
# 								"border-color : red;"
# 								"background-color : #edf7f8;"
# 								"}")		
# # 		
# 		self.onlyInt = QtGui.QIntValidator()
# 		self.userval2.setValidator(self.onlyInt)
# 		self.onlyInt.setRange(1,128)
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 		self.setPalette(palette)
# 		self.setLayout(self.layout)
# 		
# 		self.prf_assigned = False
# 		self.stepcount_assigned = False
# 	
# 	def prf_changing(self):
# 		self.opacity_effect3.setEnabled(True)
# 		self.opacity_effect4.setEnabled(True)	
# 		self.prf_assigned = False
# 		
# 	def stepcount_changing(self):
# 		self.opacity_effect3.setEnabled(True)
# 		self.opacity_effect4.setEnabled(True)	
# 		self.stepcount_assigned = False
# 	
# 	def textChange_2(self):
# 		self.userval2.clearFocus()
# 		self.stepcount_assigned = True
# 		if self.prf_assigned:
# 			self.opacity_effect3.setEnabled(False)
# 			self.opacity_effect4.setEnabled(False)
# 		self.opacity_effect1.setEnabled(False)
# 		self.userval1.setEnabled(True)
# 		
# 		val = int(str(self.userval2.text()))
# 		AFE_config_stepcount(val)
# 		logWindow_wid.settingLogText('Step Count is assigned with a value of ' + str(val))
# 		
# 	def textChange_1(self):
# 		self.prf_assigned = True
# 		
# 		self.opacity_effect3.setEnabled(False)
# 		self.opacity_effect4.setEnabled(False)	
# 		self.ReConAmbScheme.opacity_effect1.setEnabled(False)
# 		self.ReConAmbScheme.setEnabled(True)
# 		
# 		val2 = float(str(self.userval1.text()))
# 		
# 		finalVal = AFE_config_prpct(val2)
# 		
# 		self.label1.setText('PRPCT = ' + str(int(finalVal[0])) )
# 		self.label2.setText('Exact PRF is ' + str(finalVal[1]) + ' Hz')
# 		logWindow_wid.settingLogText('PRF assignment')
# 
# class ReConv_N_AMBCancelScheme(QtGui.QWidget):
# 	def __init__(self):
# 		super(ReConv_N_AMBCancelScheme,self).__init__()
# 		
# 		self.layout = QtGui.QVBoxLayout()
# 		
# 		self.Hbox1 = QtGui.QHBoxLayout()
# 		self.Hbox2 = QtGui.QHBoxLayout()
# 		
# 		self.ReConvThre = QtGui.QLabel('ReConvergence \nThreshold (V)')
# 		self.AMBCancel = QtGui.QLabel('AMB Cancellation \nScheme')
# 		
# 		self.ReConvThre.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.AMBCancel.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# # 		self.ReConvThre.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: blue;")
# # 		self.AMBCancel.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: blue;")
# 		self.ReConvThre.setAlignment(QtCore.Qt.AlignCenter)
# 		self.AMBCancel.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.userVal1 = QtGui.QLineEdit()
# 		self.userVal2 = QtGui.QComboBox()
# 		self.userVal1.setAlignment(QtCore.Qt.AlignCenter)
# 		self.userVal2.addItems(['None', 'ANA-AACM','MCU Ctrl'])
# 		
# 		self.userVal1.setPlaceholderText('Enter in Volts')
# 		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
# 		self.userVal1.setSizePolicy(sizePolicy)
# 
# 		self.userVal2.currentIndexChanged.connect(self.ABM_index)
# 		
# # 		self.userVal1.setDisabled(True)
# 		self.userVal2.setEnabled(False)
# 		self.Hbox1.addWidget(self.ReConvThre)
# 		self.Hbox1.addWidget(self.userVal1)
# 		
# 		self.Hbox2.addWidget(self.AMBCancel)
# 		self.Hbox2.addWidget(self.userVal2)
# 		
# 		self.layout.addLayout(self.Hbox1)
# 		self.layout.addLayout(self.Hbox2)
# # 		self.layout.addWidget(ColorQLineEdit('one'))
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 		self.setPalette(palette)
# 		
# 		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect1.setOpacity(0.3)
# 		
# 		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect2.setOpacity(0.3)
# 		
# 		self.ReConvThre.setGraphicsEffect(self.opacity_effect1)
# 		self.AMBCancel.setGraphicsEffect(self.opacity_effect2)
# 		
# 		self.setLayout(self.layout)
# 		self.userVal1.setStyleSheet("QLineEdit"
# 								"{"
# 								"border :1px solid black;"
# 								"}"
# 								"QLineEdit::focus"
# 								"{"
# # 								"border :2px solid"
# 								"border-color : red ;"
# 								"background-color : #edf7f8;"
# 								"}")
# 		
# 		self.onlyDouble = QtGui.QDoubleValidator()
# 		self.userVal1.setValidator(self.onlyDouble)
# 		self.onlyDouble.setNotation(QtGui.QDoubleValidator.StandardNotation)
# 		self.onlyDouble.setRange(0.0,1.200,decimals = 3)
# 		self.userVal1.setToolTip('Enter values between 0.0 V and 1.2 V')
# 		
# 		self.userVal1.editingFinished.connect(self.ReConvTextChanged)
# 		
# 		
# 	def ReConvTextChanged(self):
# 		self.userVal1.clearFocus()
# 		self.userVal1.setEnabled(True)
# 		self.opacity_effect2.setEnabled(False)
# 		self.userVal2.setEnabled(True)
# 		
# 		val = float(str(self.userVal1.text()))
# 		regVal = AFE_config_ReConvThre(val)
# 		
# 		logWindow_wid.settingLogText('Re-Convergence Threshold Voltage is set with REG_RECONV_THR_LED_DC register value at ' + str(int(regVal)))
# 		
# 	def ABM_index(self,i):
# 		
# 		self.userVal2.setEnabled(True)
