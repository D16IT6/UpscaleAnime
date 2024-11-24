# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 750)
        self.mainGridLayout = QtWidgets.QGridLayout(MainWindow)
        self.mainGridLayout.setObjectName("mainGridLayout")
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setObjectName("tabWidget")
        self.tabImageUpscale = QtWidgets.QWidget()
        self.tabImageUpscale.setObjectName("tabImageUpscale")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabImageUpscale)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topGridLayout = QtWidgets.QGridLayout()
        self.topGridLayout.setObjectName("topGridLayout")
        self.selectImageButton = QtWidgets.QPushButton(self.tabImageUpscale)
        self.selectImageButton.setFlat(False)
        self.selectImageButton.setObjectName("selectImageButton")
        self.topGridLayout.addWidget(self.selectImageButton, 0, 0, 1, 1)
        self.imageLabelTop = QtWidgets.QLabel(self.tabImageUpscale)
        self.imageLabelTop.setText("")
        self.imageLabelTop.setScaledContents(True)
        self.imageLabelTop.setObjectName("imageLabelTop")
        self.topGridLayout.addWidget(self.imageLabelTop, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.topGridLayout)
        self.middleGridLayout = QtWidgets.QGridLayout()
        self.middleGridLayout.setObjectName("middleGridLayout")
        self.scaleLabel = QtWidgets.QLabel(self.tabImageUpscale)
        self.scaleLabel.setObjectName("scaleLabel")
        self.middleGridLayout.addWidget(self.scaleLabel, 1, 0, 1, 1)
        self.numericUpDown = QtWidgets.QSpinBox(self.tabImageUpscale)
        self.numericUpDown.setMinimum(2)
        self.numericUpDown.setMaximum(4)
        self.numericUpDown.setObjectName("numericUpDown")
        self.middleGridLayout.addWidget(self.numericUpDown, 1, 1, 1, 1)
        self.modelLabel = QtWidgets.QLabel(self.tabImageUpscale)
        self.modelLabel.setObjectName("modelLabel")
        self.middleGridLayout.addWidget(self.modelLabel, 0, 0, 1, 1)
        self.progressBaUpscaleStatus = QtWidgets.QProgressBar(self.tabImageUpscale)
        self.progressBaUpscaleStatus.setProperty("value", 0)
        self.progressBaUpscaleStatus.setObjectName("progressBaUpscaleStatus")
        self.middleGridLayout.addWidget(self.progressBaUpscaleStatus, 2, 0, 1, 2)
        self.modelComboBox = QtWidgets.QComboBox(self.tabImageUpscale)
        self.modelComboBox.setObjectName("modelComboBox")
        self.middleGridLayout.addWidget(self.modelComboBox, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.upscaleButton = QtWidgets.QPushButton(self.tabImageUpscale)
        self.upscaleButton.setFlat(False)
        self.upscaleButton.setObjectName("upscaleButton")
        self.gridLayout.addWidget(self.upscaleButton, 0, 0, 1, 1)
        self.outputFolderButton = QtWidgets.QPushButton(self.tabImageUpscale)
        self.outputFolderButton.setObjectName("outputFolderButton")
        self.gridLayout.addWidget(self.outputFolderButton, 0, 1, 1, 1)
        self.middleGridLayout.addLayout(self.gridLayout, 4, 0, 1, 2)
        self.middleGridLayout.setColumnStretch(0, 2)
        self.middleGridLayout.setColumnStretch(1, 10)
        self.verticalLayout.addLayout(self.middleGridLayout)
        self.bottomGridLayout = QtWidgets.QGridLayout()
        self.bottomGridLayout.setObjectName("bottomGridLayout")
        self.imageLabelBottom = QtWidgets.QLabel(self.tabImageUpscale)
        self.imageLabelBottom.setText("")
        self.imageLabelBottom.setScaledContents(True)
        self.imageLabelBottom.setObjectName("imageLabelBottom")
        self.bottomGridLayout.addWidget(self.imageLabelBottom, 0, 0, 1, 1)
        self.compareImageButton = QtWidgets.QPushButton(self.tabImageUpscale)
        self.compareImageButton.setFlat(False)
        self.compareImageButton.setObjectName("compareImageButton")
        self.bottomGridLayout.addWidget(self.compareImageButton, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.bottomGridLayout)
        self.tabWidget.addTab(self.tabImageUpscale, "")
        self.tabVideoUpscale = QtWidgets.QWidget()
        self.tabVideoUpscale.setObjectName("tabVideoUpscale")
        self.tabWidget.addTab(self.tabVideoUpscale, "")
        self.mainGridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.selectImageButton.setText(_translate("MainWindow", "Select image"))
        self.scaleLabel.setText(_translate("MainWindow", "Scale"))
        self.modelLabel.setText(_translate("MainWindow", "Model"))
        self.upscaleButton.setText(_translate("MainWindow", "Upscale"))
        self.outputFolderButton.setText(_translate("MainWindow", "Output Folder"))
        self.compareImageButton.setText(_translate("MainWindow", "Compare image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabImageUpscale), _translate("MainWindow", "Image Upscale"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVideoUpscale), _translate("MainWindow", "Video Upscale"))