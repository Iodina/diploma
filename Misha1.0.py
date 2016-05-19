# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Misha1.0.ui'
#
# Created: Wed May 18 22:51:19 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

global preferences 
preferences = {}

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(847, 600)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Purisa"))
        font.setPointSize(10)
        font.setItalic(True)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_2.toggled.connect(lambda:self.btnstate())
        self.gridLayout_3.addWidget(self.radioButton_2, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox.setEnabled(False)
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.path_to_file = QtGui.QLineEdit(self.groupBox)
        self.path_to_file.setObjectName(_fromUtf8("path_to_file"))
        self.gridLayout_2.addWidget(self.path_to_file, 1, 1, 1, 1)
        self.chooser_button = QtGui.QPushButton(self.groupBox)
        self.chooser_button.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.chooser_button.setCheckable(False)
        self.chooser_button.setDefault(False)
        self.chooser_button.setFlat(False)
        self.chooser_button.setObjectName(_fromUtf8("chooser_button"))
        self.chooser_button.clicked.connect(self.select_file)
        self.gridLayout_2.addWidget(self.chooser_button, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.movies_list_widget = QtGui.QListWidget(self.centralwidget)
        self.movies_list_widget.setObjectName(_fromUtf8("movies_list_widget"))
        self.verticalLayout_5.addWidget(self.movies_list_widget)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 1, 1, 4, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_6.addWidget(self.label_4)
        self.movies_list_widget_2 = QtGui.QListWidget(self.centralwidget)
        self.movies_list_widget_2.setObjectName(_fromUtf8("movies_list_widget_2"))
        self.verticalLayout_6.addWidget(self.movies_list_widget_2)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 1, 2, 4, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 2, 0, 1, 1)
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton.toggled.connect(lambda:self.btnstate())

        self.gridLayout_3.addWidget(self.radioButton, 3, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox_2.setEnabled(False)
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.path_to_file_2 = QtGui.QLineEdit(self.groupBox_2)
        self.path_to_file_2.setObjectName(_fromUtf8("path_to_file_2"))
        self.gridLayout.addWidget(self.path_to_file_2, 3, 2, 1, 2)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.movie_line = QtGui.QLineEdit(self.groupBox_2)
        self.movie_line.setObjectName(_fromUtf8("movie_line"))
        self.gridLayout.addWidget(self.movie_line, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.add_movie_button = QtGui.QPushButton(self.groupBox_2)
        self.add_movie_button.setObjectName(_fromUtf8("add_movie_button"))
        self.add_movie_button.clicked.connect(self.add_movie_score)
        self.gridLayout.addWidget(self.add_movie_button, 1, 3, 1, 1)
        self.score_line = QtGui.QLineEdit(self.groupBox_2)
        self.score_line.setObjectName(_fromUtf8("score_line"))
        self.gridLayout.addWidget(self.score_line, 2, 2, 1, 1)
        self.chooser_button_2 = QtGui.QPushButton(self.groupBox_2)
        self.chooser_button_2.setObjectName(_fromUtf8("chooser_button_2"))
        self.gridLayout.addWidget(self.chooser_button_2, 3, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 4, 0, 2, 1)
        self.recommend_button = QtGui.QPushButton(self.centralwidget)
        self.recommend_button.setObjectName(_fromUtf8("recommend_button"))
        self.gridLayout_3.addWidget(self.recommend_button, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie Recommender System", None))
        self.radioButton_2.setText(_translate("MainWindow", "Load it!", None))
        self.groupBox.setTitle(_translate("MainWindow", "Get data from file", None))
        self.chooser_button.setText(_translate("MainWindow", "Choose file", None))
        self.label_3.setText(_translate("MainWindow", "Movie Preferences", None))
        self.label_4.setText(_translate("MainWindow", "Recommendation", None))
        self.radioButton.setText(_translate("MainWindow", "Create and save it!", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Create new dataset", None))
        self.label.setText(_translate("MainWindow", "Movie Title", None))
        self.label_2.setText(_translate("MainWindow", "Movie score", None))
        self.add_movie_button.setText(_translate("MainWindow", "Add Movie", None))
        self.chooser_button_2.setText(_translate("MainWindow", "Save to", None))
        self.recommend_button.setText(_translate("MainWindow", "Recommend!", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
    def btnstate(self):
        """Enable and disable groupboxed according to radiobuttons """
        self.groupBox.setEnabled(self.radioButton_2.isChecked())
        self.groupBox_2.setEnabled(self.radioButton.isChecked())
	 	
    def add_movie_score(self):
    	global preferences
        if self.movie_line.text() and \
           self.score_line.text():
            preferences[self.movie_line.text()] = self.score_line.text()
        self.movie_line.clear()
        self.score_line.clear()
        self.fill_list(self.movies_list_widget, preferences) 
        
    def fill_list(self, list_widget, movies_dict):
        list_widget.clear()
        for key, value in movies_dict.iteritems():
            item = QtGui.QListWidgetItem("%s with  %s" % (key, value)) 
            list_widget.addItem(item)	   

    def select_file(self):
        self.path_to_file.setText(QtGui.QFileDialog.getOpenFileName())

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

