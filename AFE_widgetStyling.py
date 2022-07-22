def small_radioButton_styling(button_wid):
	button_wid.setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 15px;"
										"height: 15px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:10px;"
										"height: 10px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:8px;"
										"}")

def normal_radioButton_styling(button_wid):
	button_wid.setStyleSheet("QRadioButton::indicator" 
										"{"
										"width: 20px;"
										"height: 20px;"
										"}"
									"QRadioButton::indicator:checked" 
										"{"
										"border:3px solid;"
										"width:12px;"
										"height: 12px;"
										"border-color: rgb(68,187,85);"
										"background-color:rgb(68,187,85,150);"
										"border-radius:9px;"
										"}")
										
def titles_styling(label_wid):
	label_wid.setStyleSheet(" background: #f7f7f7; font-weight:bold;	color: rgba(0,124,140)")										

def Boxedlabel_styling(label_wid):
	label_wid.setStyleSheet("margin-left: 10px; border: 1px solid black; border-radius: 2.5px; background: white; color: rgba(0,124,140);")
	label_wid.setWordWrap(True)
	
def UnderlineLabel_styling(label_wid):
	label_wid.setStyleSheet("background: #f7f7f7; color:  rgba(0,124,140);border-bottom-width: 1px; border-bottom-style: solid; border-radius: 0px")
	
def Widget_Background(main_wid):
	main_wid.setAutoFillBackground(True)
	palette = main_wid.palette()
	palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor('#f7f7f7'))

	main_wid.setPalette(palette)
	
def resizingPolicy(wid):
	wid.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)	
	
def lineEditPolicy(wid):
	sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
	wid.setSizePolicy(sizePolicy)
	
def settingToolTip(wid,text_val):
	wid.setToolTip(text_val)
	
def lineEditStyling(wid):
	wid.setStyleSheet("QLineEdit"
								"{"
								"border :1px solid black;"
								"}"
								"QLineEdit::focus"
								"{"
								"border-color : red ;"
								"background-color : #edf7f8;"
								"}")
								
def TextAlignCenter(wid):
	wid.setAlignment(QtCore.Qt.AlignCenter)								

def AutoAssignedLabel(wid):
	wid.setStyleSheet("margin-left: 10px; border: 1px solid rgba(0,124,140); border-radius: 5px; background: rgba(237,247,248); color: black;")
	
def receiver_transmitterTitle(wid):
	wid.setStyleSheet(" font-weight:bold;	color: rgba(0,124,140)")
	
def checkbox_styling(button_wid):
	button_wid.setStyleSheet("QCheckBox::indicator:checked" 
										"{"
										"background-color:rgb(68,187,85);"
										"}"										
									"QCheckBox::indicator:disabled" 
										"{"
										"background-color:rgb(68,187,85,50);"
										"}"
									)
		
