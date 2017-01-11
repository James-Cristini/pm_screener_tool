# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pm_screener.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_pm_screener(object):
    def setupUi(self, pm_screener):
        pm_screener.setObjectName(_fromUtf8("pm_screener"))
        pm_screener.resize(1032, 684)
        font = QtGui.QFont()
        font.setPointSize(9)
        pm_screener.setFont(font)
        pm_screener.setStyleSheet(_fromUtf8("QWidget{\n"
"background-color: rgb(225, 225, 225);\n"
"}\n"
"QCheckBox{\n"
"width:130%;\n"
"}\n"
"QTableWidget{\n"
"background-color: rgb(240, 240, 240);\n"
"border: 2px solid rgb(200, 200, 200);\n"
"}\n"
"QTableWidget:hover, QTableWidget:focus{\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"QProgressBar{\n"
"background-color: rgb(215, 215, 215);;\n"
"color:white;\n"
"}\n"
"QProgressBar:bar {\n"
"background-color: grey;\n"
"width: 10px;\n"
"margin: 1px;\n"
"}\n"
"QRadioButton:hover{\n"
"color:rgb(100,100,100);\n"
"}\n"
"QTextEdit, QPlainTextEdit{\n"
"border: 2px solid rgb(180, 180, 180);\n"
"border-radius: 6px;\n"
"padding: 5px;\n"
"background-color: rgb(240, 240, 240);\n"
"}\n"
"QLineEdit{\n"
"border: 2px solid rgb(180, 180, 180);\n"
"border-radius: 4px;\n"
"background-color: rgb(240, 240, 240);\n"
"}\n"
"QLineEdit:hover, QLineEdit:focus, QTextEdit:hover, QTextEdit:focus, QPlainTextEdit:hover, QPlainTextEdit:focus{\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"QLabel{\n"
"padding-top:5px;\n"
"color: black;\n"
"font: bold;\n"
"}\n"
"QPushButton {\n"
"color: black;\n"
"border: 2px solid rgb(190, 190, 190);\n"
"border-radius: 11px;\n"
"padding: 5px;\n"
"background: qradialgradient(cx: 0.2, cy: 1.3,\n"
"fx: 1.0, fy: 0.5,\n"
"radius: 1.35, stop: 0 rgb(228, 228, 228), stop: 1 rgb(208, 208, 208));\n"
"min-width: 80px;\n"
"font: bold;\n"
"}\n"
"QPushButton:pressed {\n"
"color:blue;\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 rgb(245, 245, 245));\n"
"font:italic;\n"
"}\n"
"QPushButton:hover{\n"
"color:rgb(100,100,100);\n"
"}\n"
"QScrollBar::horizontal {\n"
"max-height: 7px;\n"
"}\n"
"QScrollBar::vertical {\n"
"max-width: 7px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background-color:rgb(200, 200, 200);\n"
"max-width: 4px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"background-color:rgb(200, 200, 200);\n"
"max-height: 4px;\n"
"}"))
        self.MainWindow = QtGui.QWidget(pm_screener)
        self.MainWindow.setStyleSheet(_fromUtf8("opacity: 0;"))
        self.MainWindow.setObjectName(_fromUtf8("MainWindow"))
        self.gridLayout = QtGui.QGridLayout(self.MainWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.exit_btn = QtGui.QPushButton(self.MainWindow)
        self.exit_btn.setObjectName(_fromUtf8("exit_btn"))
        self.horizontalLayout_7.addWidget(self.exit_btn)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.pm_screener_tab = QtGui.QTabWidget(self.MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pm_screener_tab.setFont(font)
        self.pm_screener_tab.setObjectName(_fromUtf8("pm_screener_tab"))
        self.stem_filter = QtGui.QWidget()
        self.stem_filter.setObjectName(_fromUtf8("stem_filter"))
        self.gridLayout_2 = QtGui.QGridLayout(self.stem_filter)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 3, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.stem_filter)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.filter_names_input = QtGui.QPlainTextEdit(self.stem_filter)
        self.filter_names_input.setObjectName(_fromUtf8("filter_names_input"))
        self.verticalLayout.addWidget(self.filter_names_input)
        self.filter_ignore_line = QtGui.QLineEdit(self.stem_filter)
        self.filter_ignore_line.setObjectName(_fromUtf8("filter_ignore_line"))
        self.verticalLayout.addWidget(self.filter_ignore_line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.filter_inn_radio = QtGui.QRadioButton(self.stem_filter)
        self.filter_inn_radio.setObjectName(_fromUtf8("filter_inn_radio"))
        self.verticalLayout_2.addWidget(self.filter_inn_radio)
        self.filter_pharma_radio = QtGui.QRadioButton(self.stem_filter)
        self.filter_pharma_radio.setObjectName(_fromUtf8("filter_pharma_radio"))
        self.verticalLayout_2.addWidget(self.filter_pharma_radio)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.filter_build_doc_btn = QtGui.QPushButton(self.stem_filter)
        self.filter_build_doc_btn.setObjectName(_fromUtf8("filter_build_doc_btn"))
        self.horizontalLayout.addWidget(self.filter_build_doc_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.pm_screener_tab.addTab(self.stem_filter, _fromUtf8(""))
        self.google_searcher = QtGui.QWidget()
        self.google_searcher.setObjectName(_fromUtf8("google_searcher"))
        self.gridLayout_3 = QtGui.QGridLayout(self.google_searcher)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_2 = QtGui.QLabel(self.google_searcher)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_2)
        self.google_names_input = QtGui.QPlainTextEdit(self.google_searcher)
        self.google_names_input.setObjectName(_fromUtf8("google_names_input"))
        self.verticalLayout_5.addWidget(self.google_names_input)
        self.google_key_input = QtGui.QLineEdit(self.google_searcher)
        self.google_key_input.setObjectName(_fromUtf8("google_key_input"))
        self.verticalLayout_5.addWidget(self.google_key_input)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.google_just_names_radio = QtGui.QRadioButton(self.google_searcher)
        self.google_just_names_radio.setObjectName(_fromUtf8("google_just_names_radio"))
        self.horizontalLayout_2.addWidget(self.google_just_names_radio)
        self.google_with_key_radio = QtGui.QRadioButton(self.google_searcher)
        self.google_with_key_radio.setObjectName(_fromUtf8("google_with_key_radio"))
        self.horizontalLayout_2.addWidget(self.google_with_key_radio)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.google_search_btn = QtGui.QPushButton(self.google_searcher)
        self.google_search_btn.setObjectName(_fromUtf8("google_search_btn"))
        self.horizontalLayout_3.addWidget(self.google_search_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(234, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(240, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)
        self.pm_screener_tab.addTab(self.google_searcher, _fromUtf8(""))
        self.micromedexer = QtGui.QWidget()
        self.micromedexer.setObjectName(_fromUtf8("micromedexer"))
        self.gridLayout_4 = QtGui.QGridLayout(self.micromedexer)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_3 = QtGui.QLabel(self.micromedexer)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_7.addWidget(self.label_3)
        self.micro_names_input = QtGui.QPlainTextEdit(self.micromedexer)
        self.micro_names_input.setObjectName(_fromUtf8("micro_names_input"))
        self.verticalLayout_7.addWidget(self.micro_names_input)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.micro_search_btn = QtGui.QPushButton(self.micromedexer)
        self.micro_search_btn.setObjectName(_fromUtf8("micro_search_btn"))
        self.horizontalLayout_6.addWidget(self.micro_search_btn)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.micro_username_input = QtGui.QLineEdit(self.micromedexer)
        self.micro_username_input.setObjectName(_fromUtf8("micro_username_input"))
        self.verticalLayout_8.addWidget(self.micro_username_input)
        self.micro_password_input = QtGui.QLineEdit(self.micromedexer)
        self.micro_password_input.setObjectName(_fromUtf8("micro_password_input"))
        self.verticalLayout_8.addWidget(self.micro_password_input)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 1, 3, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(self.micromedexer)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.micro_table = QtGui.QTableWidget(self.micromedexer)
        self.micro_table.setObjectName(_fromUtf8("micro_table"))
        self.micro_table.setColumnCount(0)
        self.micro_table.setRowCount(0)
        self.verticalLayout_3.addWidget(self.micro_table)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.micro_progress_bar = QtGui.QProgressBar(self.micromedexer)
        self.micro_progress_bar.setProperty("value", 24)
        self.micro_progress_bar.setObjectName(_fromUtf8("micro_progress_bar"))
        self.horizontalLayout_8.addWidget(self.micro_progress_bar)
        spacerItem5 = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.micro_to_excel_btn = QtGui.QPushButton(self.micromedexer)
        self.micro_to_excel_btn.setObjectName(_fromUtf8("micro_to_excel_btn"))
        self.horizontalLayout_8.addWidget(self.micro_to_excel_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 2, 3, 1)
        self.pm_screener_tab.addTab(self.micromedexer, _fromUtf8(""))
        self.gridLayout.addWidget(self.pm_screener_tab, 0, 1, 1, 1)
        pm_screener.setCentralWidget(self.MainWindow)
        self.statusbar = QtGui.QStatusBar(pm_screener)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        pm_screener.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(pm_screener)
        self.actionExit.setShortcut(_fromUtf8(""))
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionView_pharma_avoids = QtGui.QAction(pm_screener)
        self.actionView_pharma_avoids.setObjectName(_fromUtf8("actionView_pharma_avoids"))
        self.actionView_inn_avoids = QtGui.QAction(pm_screener)
        self.actionView_inn_avoids.setObjectName(_fromUtf8("actionView_inn_avoids"))
        self.actionProject_avoids = QtGui.QAction(pm_screener)
        self.actionProject_avoids.setObjectName(_fromUtf8("actionProject_avoids"))
        self.actionInternal_names = QtGui.QAction(pm_screener)
        self.actionInternal_names.setObjectName(_fromUtf8("actionInternal_names"))
        self.actionPresented_names = QtGui.QAction(pm_screener)
        self.actionPresented_names.setObjectName(_fromUtf8("actionPresented_names"))
        self.actionCompetitor_names = QtGui.QAction(pm_screener)
        self.actionCompetitor_names.setObjectName(_fromUtf8("actionCompetitor_names"))
        self.actionOptions = QtGui.QAction(pm_screener)
        self.actionOptions.setObjectName(_fromUtf8("actionOptions"))
        self.actionTool_1 = QtGui.QAction(pm_screener)
        self.actionTool_1.setObjectName(_fromUtf8("actionTool_1"))
        self.actionTool_style = QtGui.QAction(pm_screener)
        self.actionTool_style.setObjectName(_fromUtf8("actionTool_style"))
        self.actionTool_3 = QtGui.QAction(pm_screener)
        self.actionTool_3.setObjectName(_fromUtf8("actionTool_3"))
        self.actionTool_4 = QtGui.QAction(pm_screener)
        self.actionTool_4.setObjectName(_fromUtf8("actionTool_4"))
        self.actionTool_5 = QtGui.QAction(pm_screener)
        self.actionTool_5.setObjectName(_fromUtf8("actionTool_5"))
        self.actionSave_names = QtGui.QAction(pm_screener)
        self.actionSave_names.setObjectName(_fromUtf8("actionSave_names"))
        self.actionSort_names = QtGui.QAction(pm_screener)
        self.actionSort_names.setObjectName(_fromUtf8("actionSort_names"))
        self.actionFind_conflicts = QtGui.QAction(pm_screener)
        self.actionFind_conflicts.setObjectName(_fromUtf8("actionFind_conflicts"))
        self.actionClear_avoids = QtGui.QAction(pm_screener)
        self.actionClear_avoids.setObjectName(_fromUtf8("actionClear_avoids"))
        self.actionView_stripped_names = QtGui.QAction(pm_screener)
        self.actionView_stripped_names.setObjectName(_fromUtf8("actionView_stripped_names"))
        self.actionINN_avoids_password_required = QtGui.QAction(pm_screener)
        self.actionINN_avoids_password_required.setObjectName(_fromUtf8("actionINN_avoids_password_required"))
        self.actionPharma_Avoids_password_req = QtGui.QAction(pm_screener)
        self.actionPharma_Avoids_password_req.setObjectName(_fromUtf8("actionPharma_Avoids_password_req"))
        self.actionINN_avoids = QtGui.QAction(pm_screener)
        self.actionINN_avoids.setObjectName(_fromUtf8("actionINN_avoids"))
        self.actionPharma_avoids = QtGui.QAction(pm_screener)
        self.actionPharma_avoids.setObjectName(_fromUtf8("actionPharma_avoids"))
        self.actionAdd_avoids = QtGui.QAction(pm_screener)
        self.actionAdd_avoids.setObjectName(_fromUtf8("actionAdd_avoids"))

        self.retranslateUi(pm_screener)
        self.pm_screener_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(pm_screener)

    def retranslateUi(self, pm_screener):
        pm_screener.setWindowTitle(_translate("pm_screener", "PM Screener", None))
        self.exit_btn.setStatusTip(_translate("pm_screener", "Exit the program", None))
        self.exit_btn.setText(_translate("pm_screener", "Exit", None))
        self.label.setStatusTip(_translate("pm_screener", "Stem Filter Names", None))
        self.label.setText(_translate("pm_screener", "Stem Filter Names", None))
        self.filter_names_input.setStatusTip(_translate("pm_screener", "Stem Filter names", None))
        self.filter_ignore_line.setStatusTip(_translate("pm_screener", "Enter a stem to ignore", None))
        self.filter_ignore_line.setPlaceholderText(_translate("pm_screener", "Enter stem to ignore...", None))
        self.filter_inn_radio.setStatusTip(_translate("pm_screener", "Get results for an INN project (includes USAN avoids)", None))
        self.filter_inn_radio.setText(_translate("pm_screener", "INN Project", None))
        self.filter_pharma_radio.setStatusTip(_translate("pm_screener", "Get results for a pharma project (ignores USAN avoids)", None))
        self.filter_pharma_radio.setText(_translate("pm_screener", "Pharma Project", None))
        self.filter_build_doc_btn.setStatusTip(_translate("pm_screener", "Get Stem Filter results (will build an excel document)", None))
        self.filter_build_doc_btn.setText(_translate("pm_screener", "Get INN avoids", None))
        self.pm_screener_tab.setTabText(self.pm_screener_tab.indexOf(self.stem_filter), _translate("pm_screener", "Stem Filter", None))
        self.label_2.setStatusTip(_translate("pm_screener", "Google Searcher Names", None))
        self.label_2.setText(_translate("pm_screener", "Google Searcher Names", None))
        self.google_names_input.setStatusTip(_translate("pm_screener", "Google Searcher Names", None))
        self.google_key_input.setStatusTip(_translate("pm_screener", "Enter a keyword to search with", None))
        self.google_key_input.setPlaceholderText(_translate("pm_screener", "Enter keyword to searh with here...", None))
        self.google_just_names_radio.setStatusTip(_translate("pm_screener", "Search the above names alone", None))
        self.google_just_names_radio.setText(_translate("pm_screener", "Just Names", None))
        self.google_with_key_radio.setStatusTip(_translate("pm_screener", "Search the above names with a keyword", None))
        self.google_with_key_radio.setText(_translate("pm_screener", "With Keyword", None))
        self.google_search_btn.setStatusTip(_translate("pm_screener", "Open google search results for these names in browser", None))
        self.google_search_btn.setText(_translate("pm_screener", "Open Pages", None))
        self.pm_screener_tab.setTabText(self.pm_screener_tab.indexOf(self.google_searcher), _translate("pm_screener", "Google Searcher", None))
        self.label_3.setStatusTip(_translate("pm_screener", "Micromedex Names", None))
        self.label_3.setText(_translate("pm_screener", "Micromedex Names", None))
        self.micro_names_input.setStatusTip(_translate("pm_screener", "Enter names to be searched on Micromedex", None))
        self.micro_search_btn.setStatusTip(_translate("pm_screener", "Search the above names on Micromedex", None))
        self.micro_search_btn.setText(_translate("pm_screener", "Search Micromedex", None))
        self.micro_username_input.setStatusTip(_translate("pm_screener", "Enter Micromedex username", None))
        self.micro_username_input.setPlaceholderText(_translate("pm_screener", "Username", None))
        self.micro_password_input.setStatusTip(_translate("pm_screener", "Enter Micromedex password", None))
        self.micro_password_input.setPlaceholderText(_translate("pm_screener", "Password", None))
        self.label_4.setStatusTip(_translate("pm_screener", "Micromedex Data Table", None))
        self.label_4.setText(_translate("pm_screener", "Micromedex Data Table", None))
        self.micro_table.setStatusTip(_translate("pm_screener", "Micromedex Data Table", None))
        self.micro_to_excel_btn.setStatusTip(_translate("pm_screener", "See results in Excel", None))
        self.micro_to_excel_btn.setText(_translate("pm_screener", "See all data in Excel", None))
        self.pm_screener_tab.setTabText(self.pm_screener_tab.indexOf(self.micromedexer), _translate("pm_screener", "Micromedex-er", None))
        self.actionExit.setText(_translate("pm_screener", "Leave", None))
        self.actionView_pharma_avoids.setText(_translate("pm_screener", "View Pharma Avoids", None))
        self.actionView_pharma_avoids.setStatusTip(_translate("pm_screener", "View Pharma Avoids", None))
        self.actionView_inn_avoids.setText(_translate("pm_screener", "View INN Avoids", None))
        self.actionProject_avoids.setText(_translate("pm_screener", "Project Avoids", None))
        self.actionInternal_names.setText(_translate("pm_screener", "Internal Names", None))
        self.actionPresented_names.setText(_translate("pm_screener", "Presented Names", None))
        self.actionCompetitor_names.setText(_translate("pm_screener", "Competitor Names", None))
        self.actionOptions.setText(_translate("pm_screener", "Options", None))
        self.actionOptions.setStatusTip(_translate("pm_screener", "View Options", None))
        self.actionTool_1.setText(_translate("pm_screener", "Tool 1", None))
        self.actionTool_style.setText(_translate("pm_screener", "Tool 2", None))
        self.actionTool_3.setText(_translate("pm_screener", "Tool 3", None))
        self.actionTool_4.setText(_translate("pm_screener", "Tool 4", None))
        self.actionTool_5.setText(_translate("pm_screener", "Tool 5", None))
        self.actionSave_names.setText(_translate("pm_screener", "Commit Names", None))
        self.actionSort_names.setText(_translate("pm_screener", "Sort Names (A-Z)", None))
        self.actionFind_conflicts.setText(_translate("pm_screener", "Find Conflicts", None))
        self.actionClear_avoids.setText(_translate("pm_screener", "Clear All Avoids", None))
        self.actionView_stripped_names.setText(_translate("pm_screener", "View names without rationale", None))
        self.actionINN_avoids_password_required.setText(_translate("pm_screener", "INN avoids (password req.)", None))
        self.actionPharma_Avoids_password_req.setText(_translate("pm_screener", "Pharma Avoids (password req.)", None))
        self.actionINN_avoids.setText(_translate("pm_screener", "INN Avoids", None))
        self.actionPharma_avoids.setText(_translate("pm_screener", "Pharma Avoids", None))
        self.actionAdd_avoids.setText(_translate("pm_screener", "Add Avoids", None))

