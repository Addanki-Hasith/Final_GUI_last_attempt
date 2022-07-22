from pyqtgraph.Qt import QtCore
from pyqtgraph.Qt import QtGui
from pyqtgraph.Qt import QtSvg
import sys
class Color(QtGui.QWidget):
	def __init__(self,color):
		super(Color,self).__init__()
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(color))

		self.setPalette(palette)

class LogWindow(QtGui.QWidget):
	def __init__(self):
		super(LogWindow,self).__init__()
		
# 		Required Widgets
		self.title 			= QtGui.QLabel('LOG WINDOW')
		self.logWindow		= QtGui.QTextEdit()
		self.logWindow.setPlainText('This is the log window')
		
# 		Setting ToolTips
		settingToolTip(		self.logWindow,		"This is a LOG Window")
		
# 		Styling of each widget			
		titles_styling(		self.title)
		TextAlignCenter(	self.title)
		self.logWindow.setStyleSheet("background:#aaaaaa; color: white")
		self.logWindow.setReadOnly(True)
		self.logWindow.setAlignment(QtCore.Qt.TextWrapAnywhere)

# 		Resizing 	
		resizingPolicy(		self.title)
		resizingPolicy(		self.logWindow)
# 		self.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
# 		Layouts and Arrangement			
		layout = QtGui.QVBoxLayout()
		layout.addWidget(self.title,1)
		layout.addWidget(self.logWindow,15)
		
# 		setting the widget layout		
		self.setLayout(layout)
# 		Widget Background Styling	
		Widget_Background(self)
	
	def settingLogText(self,s):
		self.logWindow.clear()
		self.logWindow.insertPlainText(s)
		
logWindow_wid = LogWindow()

class RegWindow(QtGui.QWidget):
	def __init__(self):
		super(RegWindow,self).__init__()
# 		Required Widgets
		self.reg_label 				= QtGui.QLabel('Register READ/WRITE')
		self.address_wid 			= QtGui.QLineEdit()
		self.address_wid.setPlaceholderText('hex or dec ->')
		self.dec_wid 				= QtGui.QRadioButton('Dec')
		self.hex_wid 				= QtGui.QRadioButton('Hex')
		self.read_wid				= QtGui.QRadioButton('Read')
		self.write_wid 				= QtGui.QRadioButton('Write')
		self.data_wid 				= QtGui.QLineEdit()
		self.data_wid.setPlaceholderText('DATA')
		self.page 					= QtGui.QComboBox()
		self.page.addItems(['Page-?','Page-0','Page-1'])
		self.reset_wid = QtGui.QPushButton('RESET')

# 		Setting ToolTips
		settingToolTip(		self.dec_wid,		"Address in Decimal from 0 to 255")
		settingToolTip(		self.hex_wid,		"Address in Hexa Decimal from 00 too FF")
		settingToolTip(		self.read_wid,		"Read from the Address Location Specified")
		settingToolTip(		self.write_wid,		"Write at the Address Location Specified")
		settingToolTip(		self.page,			"Select the required page\nPage-0 for Global and \nPage-1 for Per Phase \nParameters")
		settingToolTip		(self.reset_wid,	"RESET all the configurations?")


# 		Styling of each widget			
		titles_styling(				self.reg_label)
		lineEditPolicy(				self.address_wid)
		lineEditPolicy(				self.data_wid)
		normal_radioButton_styling(	self.read_wid)
		normal_radioButton_styling(	self.write_wid)
		normal_radioButton_styling(	self.dec_wid)
		normal_radioButton_styling(	self.hex_wid)
		self.reset_wid.setStyleSheet("color: red;")
		
		TextAlignCenter(		self.reg_label)
		TextAlignCenter(		self.address_wid)
		TextAlignCenter(		self.data_wid)
		
		lineEditStyling(		self.address_wid)
		lineEditStyling(		self.data_wid)
	
		
			
# 		Resizing 		
		resizingPolicy(		self.reg_label)
		resizingPolicy(		self.dec_wid)
		resizingPolicy(		self.hex_wid)
		resizingPolicy(		self.read_wid)
		resizingPolicy(		self.write_wid)
		resizingPolicy(		self.page)
		resizingPolicy(		self.reset_wid)
		lineEditPolicy(		self.address_wid)
		lineEditPolicy(		self.data_wid)

# 		Grouping Radio Buttons			
		self.dec_hex 				= QtGui.QButtonGroup()
		self.dec_hex.addButton(		self.dec_wid)
		self.dec_hex.addButton(		self.hex_wid)
		
		self.read_write 			= QtGui.QButtonGroup()
		self.read_write.addButton(	self.read_wid)
		self.read_write.addButton(	self.write_wid)
		
# 		Layouts and Arrangement			

		self.dec_hexLay 					= QtGui.QVBoxLayout()
		self.dec_hexLay.addWidget(			self.dec_wid)
		self.dec_hexLay.addWidget(			self.hex_wid)
		self.MainLay 						= QtGui.QGridLayout()
		self.MainLay.addWidget(				self.reg_label,				0,0,1,4)
		self.MainLay.addWidget(				self.address_wid,			1,0,1,3)
		self.MainLay.addLayout(				self.dec_hexLay,			1,3,1,1)
		self.MainLay.addWidget(				self.read_wid,				2,0,1,1)
		self.MainLay.addWidget(				self.write_wid,				2,2,1,1)
		self.MainLay.addWidget(				self.data_wid,				3,0,1,3)
		self.MainLay.addWidget(				self.page,					3,3,1,1)
		self.MainLay.addWidget(				self.reset_wid,				4,0,1,4)
		
		
# 		setting the widget layout		
		self.setLayout(self.MainLay)
# 		Widget Background Styling	
		Widget_Background(self)

# 		internal configurations
		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
		self.opacity_effect1.setOpacity(0.5)
		self.data_wid.setGraphicsEffect(self.opacity_effect1)
		
# 		self.read_write.setEnabled(False)
		self.page.setEnabled(False)
		self.address_wid.setEnabled(False)
		self.data_wid.setEnabled(False)
		self.hex_wid.clicked.connect(self.hex_selected)
		self.dec_wid.clicked.connect(self.dec_selected)
		
		self.read_wid.clicked.connect(self.read_selected)
		self.write_wid.clicked.connect(self.write_selected)
		
		self.page.currentIndexChanged.connect(self.page_selected)
		
		self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		self.write_text = 'Enter DATA'
		
		self.hex_dec_selected = False
		
		self.read_wid.setEnabled(False)
		self.write_wid.setEnabled(False)
		
		self.address_wid_val = 0
		self.address_wid.editingFinished.connect(self.address_wid_config)
		self.address_wid.textChanged.connect(self.address_wid_textChanging)
		
		self.data_wid_valid = QtGui.QIntValidator()
		self.data_wid.setValidator(self.data_wid_valid)
		self.data_wid_valid.setRange(0,16777215)
		self.data_wid.setToolTip('Enter values between 0 and 16,777,215(2^24-1)')
		
		self.data_wid.editingFinished.connect(self.data_wid_config)
		self.data_wid.textChanged.connect(self.data_wid_textChanging)
		
		self.data_wid_val = 0
		
		
	def data_wid_textChanging(self):
		self.page.setEnabled(False)
		self.page.setCurrentIndex(0)
		
	def address_wid_textChanging(self):
# 		self.read_wid.setAutoExclusive(False)
		self.read_write.setExclusive(False)
		self.read_wid.setChecked(False)
		self.read_write.setExclusive(True)
# 		self.read_wid.setAutoExclusive(True)
		
		self.read_write.setExclusive(False)
		self.write_wid.setChecked(False)
		self.read_write.setExclusive(True)
# 		
		self.read_wid.setEnabled(False)
		self.write_wid.setEnabled(False)
		self.page.setCurrentIndex(0)
		self.page.setEnabled(False)
		self.data_wid.clear()
		self.data_wid.setEnabled(False)
		
		
		
	def hex_selected(self):
		self.address_wid.clear()
		self.address_wid.setToolTip('Enter hex values between 00 and ff')
		self.address_wid.setPlaceholderText('Enter Address')
		self.address_wid.setEnabled(True)
		
		pattern = QtCore.QRegExp("[0-9a-fA-F][0-9a-fA-F]")
		self.valitor_reg = QtGui.QRegExpValidator(pattern)
		self.address_wid.setValidator(self.valitor_reg)
		self.hex_dec_selected = True
		
		
	
	def dec_selected(self):
		self.address_wid.clear()
		self.address_wid.setToolTip('Enter hex values between 0 and 255')
		self.address_wid.setPlaceholderText('Enter Address')
		self.address_wid.setEnabled(True)
		
		self.onlyInt = QtGui.QIntValidator()
		self.address_wid.setValidator(self.onlyInt)
		self.onlyInt.setRange(0,255)
		self.hex_dec_selected = False
		
		
		
	def address_wid_config(self):
		self.address_wid.clearFocus()
		
		if self.hex_dec_selected:
			self.address_wid_val = int(str(self.address_wid.text()),16)
		else:
			self.address_wid_val = int(str(self.address_wid.text()))
		
		self.read_wid.setEnabled(True)
		self.write_wid.setEnabled(True)
	
		
	def read_selected(self):
		self.data_wid.setPlaceholderText('Select Page')
		self.page.setEnabled(True)
		self.page.setCurrentIndex(0)
		self.opacity_effect1.setEnabled(False)
		self.data_wid.setEnabled(False)
		logWindow_wid.settingLogText('Read Operation is implemented')
# 		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect2.setOpacity(0.6)
# 		self.data_wid.setGraphicsEffect(self.opacity_effect2)
		
		
	def write_selected(self):
		self.data_wid.setPlaceholderText(self.write_text)
		self.data_wid.setReadOnly(False)
		self.data_wid.setEnabled(True)
		self.page.setEnabled(False)
		self.page.setCurrentIndex(0)
		self.opacity_effect1.setEnabled(False)
		logWindow_wid.settingLogText('Write Operation is implemented')
		
		
	def data_wid_config(self):
		self.data_wid.clearFocus()
		self.page.setEnabled(True)
		self.page.setCurrentIndex(0)
		self.data_wid_val = int(str(self.data_wid.text()))
		
		
	def page_selected(self,id):
		if id == 0:
			logWindow_wid.settingLogText('select correct Page')
		else:
			if self.read_wid.isChecked():
				if id == 1:
					val = AFE_readReg(self.address_wid_val)
					logWindow_wid.settingLogText('Data from Page-0\nAddress : '+str(self.address_wid_val)+'\nValue : '+str(val))
				elif id == 2:
					AFE_explicitPageSel(True)
					val = AFE_readReg(self.address_wid_val)
					AFE_explicitPageSel(False)
					logWindow_wid.settingLogText('Data from Page-1\nAddress : '+str(self.address_wid_val)+'\nValue : '+str(val))
			
			
			elif self.write_wid.isChecked():
				if id == 1:
					intial_val = AFE_readReg(self.address_wid_val)
					AFE_writeReg(self.address_wid_val,self.data_wid_val)
					final_val = AFE_readReg(self.address_wid_val)
					
					logWindow_wid.settingLogText('Data writing at Page-0\nAddress : '+str(self.address_wid_val)+'\nInitial Val : '+str(intial_val)+'\nFinal Val : '+str(final_val))
				elif id == 2:
					AFE_explicitPageSel(True)
					intial_val = AFE_readReg(self.address_wid_val)
					AFE_writeReg(self.address_wid_val,self.data_wid_val)
					final_val = AFE_readReg(self.address_wid_val)
					AFE_explicitPageSel(False)
					logWindow_wid.settingLogText('Data writing at Page-1\nAddress : '+str(self.address_wid_val)+'\nInitial Val : '+str(intial_val)+'\nFinal Val : '+str(final_val))

class RegAndLog(QtGui.QWidget):
	def __init__(self):
		super(RegAndLog,self).__init__()
		layout_regNlog = QtGui.QVBoxLayout() 
		self.regWid = RegWindow()
		layout_regNlog.addWidget(self.regWid,3)
		layout_regNlog.addWidget(logWindow_wid,6)		
		
# 		self.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
		self.setLayout(layout_regNlog)
		
class TaskBar(QtGui.QWidget):
	def __init__(self):
		super(TaskBar,self).__init__()

# 		Required Widgets
		self.TexasInst 			= QtGui.QLabel('Texas Instruments')
		
		
		
		self.InnovCreate 		= QtGui.QLabel('INNOVATE. CREATE. MAKE THE DIFFERENCE')
		self.AFEEVMStatus 		= QtGui.QLabel('AFE4460EVM is connected')
		
# 		Setting ToolTips
		settingToolTip(self.AFEEVMStatus,	"Status of AFE Connection")
		
# 		Styling of each widget			
		self.TexasInst.setStyleSheet(		"margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
		
		self.InnovCreate.setStyleSheet(		"margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
		
		self.AFEEVMStatus.setStyleSheet(	"margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
		self.InnovCreate.setAlignment(		QtCore.Qt.AlignCenter | QtCore.Qt.TextWrapAnywhere)
		self.TexasInst.setAlignment(		QtCore.Qt.AlignCenter | QtCore.Qt.TextWrapAnywhere)
		self.AFEEVMStatus.setAlignment(		QtCore.Qt.AlignCenter | QtCore.Qt.TextWrapAnywhere)
		
# 		Resizing 		
		resizingPolicy(		self.TexasInst)
		resizingPolicy(		self.InnovCreate)
		resizingPolicy(		self.AFEEVMStatus)
		self.TexasInst.setWordWrap(True)
		self.InnovCreate.setWordWrap(True)
		self.AFEEVMStatus.setWordWrap(True)
	
# 		Layouts and Arrangement			
		self.MainLay 				= QtGui.QGridLayout()
		self.MainLay.addWidget(		self.TexasInst,			0,0,1,1)
		self.MainLay.addWidget(		self.InnovCreate,		0,1,1,1)
		self.MainLay.addWidget(		self.AFEEVMStatus,		0,2,1,1)
		
# 		setting the widget layout		
		self.setLayout(self.MainLay)
		
# 		Widget Background Styling
		Widget_Background(self)
		

class GlobalLayout(QtGui.QWidget):
	def __init__(self):
		super(GlobalLayout,self).__init__()
		self.ReConv_N_AMB =ReConv_N_AMBCancelScheme()
		self.timingParam = TimingParameters()
		self.clock_m = Clocking()
		self.phase = PhaseTiming()
		self.receiver_N_transmitter = Receiver_transmitter()
		
		self.MainLay = QtGui.QGridLayout()
		self.MainLay.addWidget(self.phase,0,0,3,4)
		self.MainLay.addWidget(self.clock_m,3,0,3,4)
		self.MainLay.addWidget(self.timingParam,6,0,3,4)
		self.MainLay.addWidget(self.ReConv_N_AMB,9,0,2,4)
		self.MainLay.addWidget(self.receiver_N_transmitter,0,4,11,13)

		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('white'))
		self.setPalette(palette)

		self.setLayout(self.MainLay)
		
		self.phase.setEnabled(			False)
		self.clock_m.setEnabled(		False)
		self.timingParam.setEnabled(	False)
		self.ReConv_N_AMB.setEnabled(	False)
	
		self.phase.PhaseTimingEnable()
		self.phase.stagger_mode.clicked.connect(self.clock_enable)
		self.phase.high_prf_mode.clicked.connect(self.clock_enable)
		self.phase.max_amb_rej_mode.clicked.connect(self.clock_enable)
		self.phase.dis_post_amb_rej_mode.clicked.connect(self.clock_enable)
		
		self.clock_m.internal.clicked.connect(self.timingPara_enable)
		self.clock_m.external.clicked.connect(self.timingPara_enable)
		self.clock_m.singleshot.clicked.connect(self.timingPara_enable)
		self.clock_m.mixedclock.clicked.connect(self.timingPara_enable)
		
		self.timingParam.userval1.editingFinished.connect(self.ReConv_N_AMB_enable)
		
		self.ReConv_N_AMB.userVal2.currentIndexChanged.connect(self.receiver_N_transmitter_enable)
	
	def clock_enable(self):
		self.clock_m.ClockingEnable()
	def timingPara_enable(self):
		self.timingParam.TimingParametersEnable()
		
	def ReConv_N_AMB_enable(self):
		self.ReConv_N_AMB.ReConv_N_AMBCancelSchemeEnable()
		
	def receiver_N_transmitter_enable(self,i):
		if i==1:
			self.receiver_N_transmitter.opacity_effect5.setEnabled(True)
			self.receiver_N_transmitter.opacity_effect6.setEnabled(True)
			self.receiver_N_transmitter.opacity_effect7.setEnabled(True)
			self.receiver_N_transmitter.opacity_effect8.setEnabled(True)
			self.receiver_N_transmitter.opacity_effect9.setEnabled(True)
			
			self.receiver_N_transmitter.offdacPD1.setEnabled(False)
			self.receiver_N_transmitter.offdacPD2.setEnabled(False)
			self.receiver_N_transmitter.offdacPD3.setEnabled(False)			
			self.receiver_N_transmitter.offdacPD4.setEnabled(False)
			
		elif i==2:
			self.receiver_N_transmitter.opacity_effect5.setEnabled(False)
			self.receiver_N_transmitter.opacity_effect6.setEnabled(False)
			self.receiver_N_transmitter.opacity_effect7.setEnabled(False)
			self.receiver_N_transmitter.opacity_effect8.setEnabled(False)
			self.receiver_N_transmitter.opacity_effect9.setEnabled(False)
			
			self.receiver_N_transmitter.offdacPD1.setEnabled(True)
			self.receiver_N_transmitter.offdacPD2.setEnabled(True)
			self.receiver_N_transmitter.offdacPD3.setEnabled(True)			
			self.receiver_N_transmitter.offdacPD4.setEnabled(True)
			
		self.receiver_N_transmitter.maxNoTIAs_Enable()
		
class PerPhaseLayout(QtGui.QWidget):
	def __init__(self):
		super(PerPhaseLayout,self).__init__()
		
		self.control_wid = control_layout()
		self.Individual_config_wid = Individual_config_layout()
		self.Summary_config_wid = Summary_config_layout()
		self.config_wid = QtGui.QStackedWidget()
		
		self.config_wid.addWidget(self.Individual_config_wid)
		self.config_wid.addWidget(self.Summary_config_wid)
		
		
		
		self.MainLay 					= QtGui.QGridLayout()
		self.MainLay.addWidget(			self.control_wid,			0,0,2,10)
		self.MainLay.addWidget(			self.config_wid,		2,0,20,10)
		
		self.setLayout(self.MainLay)
		
		
# 		internal configurations
		self.config_wid.setCurrentIndex(0)
		self.control_wid.individual.clicked.connect(self.View_change_individual)
		self.control_wid.summary.clicked.connect(self.View_change_summary)
		
		self.control_wid.userval1.currentIndexChanged.connect(self.Individual_config_wid.Individual_config_layout_Enable)
		
	def View_change_individual(self):
		self.config_wid.setCurrentIndex(0)
	def View_change_summary(self):
		self.config_wid.setCurrentIndex(1)
		
		
class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
		driver_reset()
		Parameters_reset_Global_and_PerPhase()
		Reset_SummaryTable()
		self.setWindowTitle('AFE4460 GUI')		
		
		svgWidget = QtSvg.QSvgWidget(APP_DIR+"/AFE4460_Global.svg")
# 		svgWidget.setGeometry(50,50,759,668)
		svgWidget.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		
		self.get_size = QtSvg.QSvgRenderer(APP_DIR+"/AFE4460_Global.svg")
# 		svgWidget.setFixedSize(self.get_size.defaultSize())
		self.widget_main_Global = GlobalLayout()
		self.widget_main_Global.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
		self.widget_main_PerPhase = PerPhaseLayout()
		self.widget_main_PerPhase.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
		self.widget_main_TimingPower = Color('green')
		self.widget_main_TimingPower.setSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
		tab_widget_lay = QtGui.QVBoxLayout()
		tab_wid = QtGui.QTabWidget()
		tab_wid.addTab(self.widget_main_Global,"GLOBAL CONFIGURATION")
		tab_wid.addTab(self.widget_main_PerPhase,"PER PHASE CONFIGURATION")
		tab_wid.addTab(self.widget_main_TimingPower,"TIMING DIAGRAM AND POWER")
		tab_wid.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		tab_wid.setStyleSheet("QTabBar::tab"
							"{" 
								"width: 350px;" 
								"height: 50px;"
							"}"
							"QTabBar::tab:selected" 
							"{"
								"background-color : #ee0000 ;"
								"color: 'white';"
								"font-weight : bold;"		
							"}"
							"QTabBar::tab:!selected" 
							"{"
								"background-color : #efb9b9 ;"
								"color: 'white';"
							"}"
							)
		
		tab_widget_lay.addWidget(tab_wid)
		
		self.MainWindow_SubLay = QtGui.QHBoxLayout()
		
		self.reg_and_log_Widget = RegAndLog()
		
		self.MainWindow_SubLay.addWidget(self.reg_and_log_Widget,1)
		self.MainWindow_SubLay.addLayout(tab_widget_lay,5)
		
		self.MainWindow_Lay = QtGui.QVBoxLayout()

		self.MainWindow_Lay.addLayout(self.MainWindow_SubLay,10)															
		self.MainWindow_Lay.addWidget(TaskBar(),1)
		
		self.MainWindow_wid = QtGui.QWidget()
		self.MainWindow_wid.setLayout(self.MainWindow_Lay)
		
		
		logWindow_wid.settingLogText('This is Log Window')
		Maximum_no_of_TIAs_global.currentIndexChanged.connect(self.widget_main_PerPhase.Individual_config_wid.receiver.config_noOfTIAs)
		
		LED1_On_Label.currentIndexChanged.connect(self.widget_main_PerPhase.Individual_config_wid.transmitter.LED_ON1_Time_label)
		
		LED2_On_Label.currentIndexChanged.connect(self.widget_main_PerPhase.Individual_config_wid.transmitter.LED_ON2_Time_label)
		
		self.reg_and_log_Widget.regWid.reset_wid.clicked.connect(self.reset_everything)
		
		
		
		self.setCentralWidget(self.MainWindow_wid)
		
	def reset_everything(self):
		reset_window = QtGui.QMessageBox()
		reset_window.setWindowTitle('RESET AFE')
		reset_window.setText('Do you want to RESET?')
		reset_window.setInformativeText('This resets all the configurations made so far!')
		reset_window.setIcon(QtGui.QMessageBox.Critical)
		reset_window.setStandardButtons(QtGui.QMessageBox.Cancel|QtGui.QMessageBox.Ok)
		reset_window.setDefaultButton(QtGui.QMessageBox.Cancel)
		
		reset_window.buttonClicked.connect(self.reset_funcs)
		
		x = reset_window.exec_()
		
	def reset_funcs(self,i):
		if i.text() == 'Cancel':
			logWindow_wid.settingLogText('RESET is Aborted')
		else:
			logWindow_wid.settingLogText('RESET')

window = MainWindow()

window.show()	











# class LogWindow(QtGui.QWidget):
# 	def __init__(self):
# 		super(LogWindow,self).__init__()
# 		self.title = QtGui.QLabel('LOG WINDOW')
# 		self.title.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.title.setAlignment(QtCore.Qt.AlignCenter)
# 		self.logWindow = QtGui.QTextEdit()
# 		self.logWindow.setStyleSheet("background:#aaaaaa; color: white")
# 		self.logWindow.setPlainText('This is the log window')
# 		self.logWindow.setReadOnly(True)
# 		self.logWindow.setAlignment(QtCore.Qt.TextWrapAnywhere)
# 		self.title.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.logWindow.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		layout = QtGui.QVBoxLayout()
# 		layout.addWidget(self.title,1)
# 		layout.addWidget(self.logWindow,15)
# 		
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 		self.setPalette(palette)
# 		self.setLayout(layout)
# 		
# 		self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 	def settingLogText(self,s):
# 		self.logWindow.clear()
# 		self.logWindow.insertPlainText(s)

# class TaskBar(QtGui.QWidget):
# 	def __init__(self):
# 		super(TaskBar,self).__init__()
# 		self.layout = QtGui.QHBoxLayout()
# 		
# 		self.TexasInst = QtGui.QLabel('TEXAS INSTRUMENTS')
# 		self.InnovCreate = QtGui.QLabel('INNOVATE. CREATE. MAKE THE DIFFERENCE')
# 		self.AFEEVMStatus = QtGui.QLabel('AFE4460EVM is connected')
# 		
# 		self.TexasInst.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
# 		self.TexasInst.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.TextWrapAnywhere)
# 		self.InnovCreate.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
# 		self.InnovCreate.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.TextWrapAnywhere)
# 		self.AFEEVMStatus.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: red;")
# 		self.AFEEVMStatus.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.TextWrapAnywhere)
# 		
# 		self.TexasInst.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.InnovCreate.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.AFEEVMStatus.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.TexasInst.setWordWrap(True)
# 		self.InnovCreate.setWordWrap(True)
# 		self.AFEEVMStatus.setWordWrap(True)
# 		
# 		self.layout.addWidget(self.TexasInst,1)
# 		self.layout.addWidget(self.InnovCreate,2)
# 		self.layout.addWidget(self.AFEEVMStatus,1)
# 		
# 		self.layout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
# 		
# 		self.setLayout(self.layout)
# class RegWindow(QtGui.QWidget):
# 	def __init__(self):
# 		super(RegWindow,self).__init__()
# 		self.reg_label = QtGui.QLabel('Register READ/WRITE')
# 		self.reg_label.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")
# 		self.reg_label.setAlignment(QtCore.Qt.AlignCenter)
# 		self.reg_label.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		layout_m = QtGui.QVBoxLayout()		
# 		self.address_wid = QtGui.QLineEdit()
# 		self.address_wid.setPlaceholderText('Address')
# 		self.address_wid.setStyleSheet("QLineEdit"
# 								"{"
# 								"margin-left: 10px; border: 1px solid black; border-radius: 5px; background: white; color: black;"
# 								"}"
# 								"QLineEdit::focus"
# 								"{"
# 								"border-color : red;"
# 								"background-color : #edf7f8;"
# 								"}")
# 		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.address_wid.setSizePolicy(sizePolicy)
# 		self.address_wid.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.address_wid.setAlignment(QtCore.Qt.AlignCenter)
# 		
# 		self.dec_wid = QtGui.QRadioButton('Dec')
# 		self.dec_wid.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.dec_wid.setStyleSheet("QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 		self.hex_wid = QtGui.QRadioButton('Hex')
# 		self.hex_wid.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.hex_wid.setStyleSheet("QRadioButton::indicator:checked" 
# 										"{"
# 										"border:3px solid;"
# 										"border-color: rgb(68,187,85);"
# 										"background-color:rgb(68,187,85,150);"
# 										"border-radius:9px;"
# 										"}")
# 										
# 		self.read_wid = QtGui.QRadioButton('Read')
# 		self.read_wid.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.write_wid = QtGui.QRadioButton('Write')
# 		self.write_wid.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.read_wid.setStyleSheet("QRadioButton::indicator" 
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
# 		self.write_wid.setStyleSheet("QRadioButton::indicator" 
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
# 		self.data_wid = QtGui.QLineEdit()
# 		self.data_wid.setPlaceholderText('DATA')
# 		self.data_wid.setStyleSheet("QLineEdit"
# 								"{"
# 								"margin-left: 10px; border: 1px solid black; border-radius: 5px; background: white; color: black;"
# 								"}"
# 								"QLineEdit::focus"
# 								"{"
# 								"border-color : red;"
# 								"background-color : #edf7f8;"
# 								"}")
# 		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.data_wid.setSizePolicy(sizePolicy)
# 		self.data_wid.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.data_wid.setAlignment(QtCore.Qt.AlignCenter)
# 
# 		self.page = QtGui.QComboBox()
# 		self.page.addItems(['Page-?','Page-0','Page-1'])
# 		self.page.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		
# 		self.reset_wid = QtGui.QPushButton('RESET')
# # 		self.reset_wid.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 10px; background: white; color: black;")
# 		self.reset_wid.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 
# 		
# 		layout_4 = QtGui.QVBoxLayout()											
# 		layout_5 = QtGui.QVBoxLayout()													
# 		layout_6 = QtGui.QHBoxLayout()
# 		layout_7 = QtGui.QHBoxLayout()
# 		
# 		layout_5.addWidget(self.dec_wid)
# 		layout_5.addWidget(self.hex_wid)		
# 												
# 		layout_6.addWidget(self.address_wid,3)
# 		layout_6.addLayout(layout_5,2)
# 		
# 		layout_7.addWidget(self.read_wid)
# 		layout_7.addWidget(self.write_wid)
# 		
# 		self.read_write = QtGui.QWidget()
# 		self.read_write.setLayout(layout_7)
# 		
# 		layout_4.addWidget(self.reg_label)
# 		layout_4.addLayout(layout_6)
# 		layout_4.addWidget(self.read_write)
# 		
# 		layout_m.addLayout(layout_4)
# 		
# 		layout_8 = QtGui.QHBoxLayout()
# 		layout_8.addWidget(self.data_wid)
# 		layout_8.addWidget(self.page)
# 		
# 		layout_m.addLayout(layout_8)
# 		layout_m.addWidget(self.reset_wid)
# 		
# 		self.setAutoFillBackground(True)
# 		palette = self.palette()
# 		palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))
# 		self.setPalette(palette)
# 		self.setLayout(layout_m)
# 		
# 		
# 		self.opacity_effect = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect.setOpacity(0.5)
# 		self.address_wid.setGraphicsEffect(self.opacity_effect)
# 		
# 		self.opacity_effect1 = QtGui.QGraphicsOpacityEffect()
# 		self.opacity_effect1.setOpacity(0.5)
# 		self.data_wid.setGraphicsEffect(self.opacity_effect1)
# 		
# 		self.read_write.setEnabled(False)
# 		self.page.setEnabled(False)
# 		self.address_wid.setEnabled(False)
# 		self.data_wid.setEnabled(False)
# 		self.hex_wid.clicked.connect(self.hex_selected)
# 		self.dec_wid.clicked.connect(self.dec_selected)
# 		
# 		self.read_wid.clicked.connect(self.read_selected)
# 		self.write_wid.clicked.connect(self.write_selected)
# 		
# 		self.page.currentIndexChanged.connect(self.page_selected)
# 		
# 		self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
# 		self.write_text = 'Enter DATA'
# 	def hex_selected(self):
# 		self.address_wid.setEnabled(True)
# 		self.read_write.setEnabled(True)
# 		self.opacity_effect.setEnabled(False)
# 		logWindow_wid.settingLogText('Enter hex values between 00 and ff')
# 	
# 	def dec_selected(self):
# 		self.address_wid.setEnabled(True)
# 		self.read_write.setEnabled(True)
# 		self.opacity_effect.setEnabled(False)
# 		logWindow_wid.settingLogText('Enter hex values between 0 and 255')
# 	
# 	def read_selected(self):
# 		self.data_wid.setPlaceholderText('Select Page')
# 		self.page.setEnabled(True)
# 		self.page.setCurrentIndex(0)
# 		self.opacity_effect1.setEnabled(False)
# 		self.data_wid.setEnabled(False)
# 		logWindow_wid.settingLogText('Read Operation is implemented')
# # 		self.opacity_effect2 = QtGui.QGraphicsOpacityEffect()
# # 		self.opacity_effect2.setOpacity(0.6)
# # 		self.data_wid.setGraphicsEffect(self.opacity_effect2)
# 		
# 		
# 	def write_selected(self):
# 		self.data_wid.setPlaceholderText(self.write_text)
# 		self.data_wid.setReadOnly(False)
# 		self.data_wid.setEnabled(True)
# 		self.page.setEnabled(True)
# 		self.opacity_effect1.setEnabled(False)
# 		logWindow_wid.settingLogText('Write Operation is implemented')
# 		
# 	def page_selected(self,id):
# 		if id == 0:
# 			logWindow_wid.settingLogText('select correct Page')
# 		if self.read_wid.isChecked() and self.page.currentIndex()!=0:
# 			logWindow_wid.settingLogText('Read Operation is implemented')
# 			self.data_wid.setPlaceholderText('Value in REG')
# 		
# 		elif self.write_wid.isChecked() and self.page.currentIndex()!=0 :
# 			logWindow_wid.settingLogText('Write Operation is implemented')
# 			self.data_wid.setPlaceholderText(self.write_text)
# 		
# 		
# 		if id == 1 and self.read_wid.isChecked():
# 			if self.dec_wid.isChecked():
# # 				logWindow_wid.settingLogText(self.address_wid.text())
# 				try:
# 					a2 = self.address_wid.text()
# 					logWindow_wid.settingLogText(7*a2)
# 				except:
# 					logWindow_wid.settingLogText('Please enter only integer type values')
# 			elif self.hex_wid.isChecked():
# 				pass
# 		
# 		elif id == 1 and self.write_wid.isChecked():
# 			if self.dec_wid.isChecked():
# 				pass
# 			elif self.hex_wid.isChecked():
# 				pass
# 		
# 		elif id == 2 and self.read_wid.isChecked():
# 			if self.dec_wid.isChecked():
# 				pass
# 			elif self.hex_wid.isChecked():
# 				pass
# 		
# 		elif id == 2 and self.write_wid.isChecked():
# 			if self.dec_wid.isChecked():
# 				pass
# 			elif self.hex_wid.isChecked():
# 				pass
				
