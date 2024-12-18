# Form implementation generated from reading ui file './Windows/MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 750)
        self.mainGridLayout = QtWidgets.QGridLayout(MainWindow)
        self.mainGridLayout.setObjectName("mainGridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=MainWindow)
        self.tabWidget.setObjectName("tabWidget")
        self.tabImageUpscale = QtWidgets.QWidget()
        self.tabImageUpscale.setObjectName("tabImageUpscale")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabImageUpscale)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topGridLayout = QtWidgets.QGridLayout()
        self.topGridLayout.setObjectName("topGridLayout")
        self.selectImageButton = QtWidgets.QPushButton(parent=self.tabImageUpscale)
        self.selectImageButton.setFlat(False)
        self.selectImageButton.setObjectName("selectImageButton")
        self.topGridLayout.addWidget(self.selectImageButton, 0, 0, 1, 1)
        self.imageLabelTop = QtWidgets.QLabel(parent=self.tabImageUpscale)
        self.imageLabelTop.setText("")
        self.imageLabelTop.setScaledContents(True)
        self.imageLabelTop.setObjectName("imageLabelTop")
        self.topGridLayout.addWidget(self.imageLabelTop, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.topGridLayout)
        self.middleGridLayout = QtWidgets.QGridLayout()
        self.middleGridLayout.setObjectName("middleGridLayout")
        self.scaleLabel = QtWidgets.QLabel(parent=self.tabImageUpscale)
        self.scaleLabel.setObjectName("scaleLabel")
        self.middleGridLayout.addWidget(self.scaleLabel, 1, 0, 1, 1)
        self.numericUpDown = QtWidgets.QSpinBox(parent=self.tabImageUpscale)
        self.numericUpDown.setMinimum(2)
        self.numericUpDown.setMaximum(4)
        self.numericUpDown.setProperty("value", 4)
        self.numericUpDown.setObjectName("numericUpDown")
        self.middleGridLayout.addWidget(self.numericUpDown, 1, 1, 1, 1)
        self.modelLabel = QtWidgets.QLabel(parent=self.tabImageUpscale)
        self.modelLabel.setObjectName("modelLabel")
        self.middleGridLayout.addWidget(self.modelLabel, 0, 0, 1, 1)
        self.progressBaUpscaleStatus = QtWidgets.QProgressBar(parent=self.tabImageUpscale)
        self.progressBaUpscaleStatus.setProperty("value", 0)
        self.progressBaUpscaleStatus.setObjectName("progressBaUpscaleStatus")
        self.middleGridLayout.addWidget(self.progressBaUpscaleStatus, 2, 0, 1, 2)
        self.modelComboBox = QtWidgets.QComboBox(parent=self.tabImageUpscale)
        self.modelComboBox.setObjectName("modelComboBox")
        self.middleGridLayout.addWidget(self.modelComboBox, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.upscaleButton = QtWidgets.QPushButton(parent=self.tabImageUpscale)
        self.upscaleButton.setFlat(False)
        self.upscaleButton.setObjectName("upscaleButton")
        self.gridLayout.addWidget(self.upscaleButton, 0, 0, 1, 1)
        self.outputFolderButton = QtWidgets.QPushButton(parent=self.tabImageUpscale)
        self.outputFolderButton.setObjectName("outputFolderButton")
        self.gridLayout.addWidget(self.outputFolderButton, 0, 1, 1, 1)
        self.middleGridLayout.addLayout(self.gridLayout, 4, 0, 1, 2)
        self.middleGridLayout.setColumnStretch(0, 2)
        self.middleGridLayout.setColumnStretch(1, 10)
        self.verticalLayout.addLayout(self.middleGridLayout)
        self.bottomGridLayout = QtWidgets.QGridLayout()
        self.bottomGridLayout.setObjectName("bottomGridLayout")
        self.imageLabelBottom = QtWidgets.QLabel(parent=self.tabImageUpscale)
        self.imageLabelBottom.setText("")
        self.imageLabelBottom.setScaledContents(True)
        self.imageLabelBottom.setObjectName("imageLabelBottom")
        self.bottomGridLayout.addWidget(self.imageLabelBottom, 0, 0, 1, 1)
        self.compareImageButton = QtWidgets.QPushButton(parent=self.tabImageUpscale)
        self.compareImageButton.setFlat(False)
        self.compareImageButton.setObjectName("compareImageButton")
        self.bottomGridLayout.addWidget(self.compareImageButton, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.bottomGridLayout)
        self.tabWidget.addTab(self.tabImageUpscale, "")
        self.tabVideoUpscale = QtWidgets.QWidget()
        self.tabVideoUpscale.setObjectName("tabVideoUpscale")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabVideoUpscale)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.tabVideoUpscale)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.listWidgetLog = QtWidgets.QListWidget(parent=self.tabVideoUpscale)
        self.listWidgetLog.setObjectName("listWidgetLog")
        self.verticalLayout_2.addWidget(self.listWidgetLog)
        self.selectVideoButton = QtWidgets.QPushButton(parent=self.tabVideoUpscale)
        self.selectVideoButton.setObjectName("selectVideoButton")
        self.verticalLayout_2.addWidget(self.selectVideoButton)
        self.gridOptions = QtWidgets.QGridLayout()
        self.gridOptions.setObjectName("gridOptions")
        self.modelComboBoxVideo = QtWidgets.QComboBox(parent=self.tabVideoUpscale)
        self.modelComboBoxVideo.setObjectName("modelComboBoxVideo")
        self.gridOptions.addWidget(self.modelComboBoxVideo, 0, 1, 1, 1)
        self.numericUpDownVideo = QtWidgets.QSpinBox(parent=self.tabVideoUpscale)
        self.numericUpDownVideo.setMinimum(2)
        self.numericUpDownVideo.setMaximum(4)
        self.numericUpDownVideo.setProperty("value", 4)
        self.numericUpDownVideo.setObjectName("numericUpDownVideo")
        self.gridOptions.addWidget(self.numericUpDownVideo, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.tabVideoUpscale)
        self.label.setObjectName("label")
        self.gridOptions.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.upscaleButtonVideo = QtWidgets.QPushButton(parent=self.tabVideoUpscale)
        self.upscaleButtonVideo.setObjectName("upscaleButtonVideo")
        self.gridLayout_2.addWidget(self.upscaleButtonVideo, 0, 0, 1, 1)
        self.outputFolderButtonVideo = QtWidgets.QPushButton(parent=self.tabVideoUpscale)
        self.outputFolderButtonVideo.setObjectName("outputFolderButtonVideo")
        self.gridLayout_2.addWidget(self.outputFolderButtonVideo, 0, 1, 1, 1)
        self.compareButtonVideo = QtWidgets.QPushButton(parent=self.tabVideoUpscale)
        self.compareButtonVideo.setObjectName("compareButtonVideo")
        self.gridLayout_2.addWidget(self.compareButtonVideo, 1, 0, 1, 2)
        self.gridOptions.addLayout(self.gridLayout_2, 3, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(parent=self.tabVideoUpscale)
        self.label_2.setObjectName("label_2")
        self.gridOptions.addWidget(self.label_2, 1, 0, 1, 1)
        self.gridOptions.setColumnStretch(0, 2)
        self.gridOptions.setColumnStretch(1, 10)
        self.verticalLayout_2.addLayout(self.gridOptions)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tabVideoUpscale, "")
        self.mainGridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.selectImageButton.setText(_translate("MainWindow", "Select image"))
        self.scaleLabel.setText(_translate("MainWindow", "Scale"))
        self.numericUpDown.setToolTip(_translate("MainWindow", "Mức độ scale (chỉ model đầu mới có thể tuỳ chỉnh)"))
        self.modelLabel.setText(_translate("MainWindow", "Model"))
        self.modelComboBox.setToolTip(_translate("MainWindow", "Model để upscale"))
        self.upscaleButton.setText(_translate("MainWindow", "Upscale"))
        self.outputFolderButton.setText(_translate("MainWindow", "Output Folder"))
        self.compareImageButton.setText(_translate("MainWindow", "Compare image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabImageUpscale), _translate("MainWindow", "Image Upscale"))
        self.label_3.setText(_translate("MainWindow", "Log"))
        self.selectVideoButton.setToolTip(_translate("MainWindow", "Chọn video đầu vào"))
        self.selectVideoButton.setText(_translate("MainWindow", "Select video"))
        self.modelComboBoxVideo.setToolTip(_translate("MainWindow", "Model để upscale"))
        self.numericUpDownVideo.setToolTip(_translate("MainWindow", "Mức độ scale (chỉ model đầu mới có thể tuỳ chỉnh)"))
        self.label.setText(_translate("MainWindow", "Model"))
        self.upscaleButtonVideo.setToolTip(_translate("MainWindow", "Bấm để tăng chất lượng video"))
        self.upscaleButtonVideo.setText(_translate("MainWindow", "Upscale"))
        self.outputFolderButtonVideo.setToolTip(_translate("MainWindow", "Folder chứa dữ liệu đầu ra"))
        self.outputFolderButtonVideo.setText(_translate("MainWindow", "Output Folder"))
        self.compareButtonVideo.setText(_translate("MainWindow", "Compare"))
        self.label_2.setText(_translate("MainWindow", "Scale"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabVideoUpscale), _translate("MainWindow", "Video Upscale"))
