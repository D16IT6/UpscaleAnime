import os
from typing import Tuple

import sys

from PyQt5.QtCore import Qt, QFileInfo, QDir, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QDesktopServices

from Models.UpscaleModel import UpscaleModel
from Utilities.Command import Command
from Utilities.Configuration import Configuration
from Utilities.Constants import REALESRGAN, MODELS, VERSION, COMPARE_HEIGHT, COMPARE_WIDTH
from Windows.MainWindow import Ui_MainWindow

config = Configuration()


def InitForm() -> Tuple[QApplication, Ui_MainWindow, QWidget]:
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    return app, ui, Form


def LoadData(mainWindow: Ui_MainWindow, command: Command):
    combobox = mainWindow.modelComboBox

    upscaleModels = command.LoadModels()

    for upscaleModel in upscaleModels:
        combobox.addItem(upscaleModel.name, upscaleModel)


def ConnectEvents(ui: Ui_MainWindow):
    combobox = ui.modelComboBox
    spinbox = ui.numericUpDown

    def OnComboboxChanged(index):
        selected_model: UpscaleModel = combobox.itemData(index)
        if selected_model:
            spinbox.setMinimum(selected_model.scale[0])
            spinbox.setMaximum(selected_model.scale[-1])
            spinbox.setValue(selected_model.scale[0])
            spinbox.setReadOnly(selected_model.scale[0] == selected_model.scale[-1])

            config.Scale = spinbox.value()

    def OnSpinChanged():
        config.Scale = spinbox.value()

    def OnSelectImage():
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Chọn ảnh anime cần upscale",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )

        if file_path:
            file_info = QFileInfo(file_path)

            if file_info.exists() and file_info.suffix().lower() in ['jpg', 'png', 'webp']:
                pixmap = QPixmap(file_path)

                label_width = ui.imageLabelTop.width()
                label_height = ui.imageLabelTop.height()

                scaled_pixmap = pixmap.scaled(label_width, label_height, aspectRatioMode=Qt.KeepAspectRatio)

                ui.imageLabelTop.setPixmap(scaled_pixmap)
                ui.imageLabelTop.setScaledContents(True)

                config.InputFile = file_path
            else:
                print("Hãy chọn hình ảnh hợp lệ!")

    def AllowExistFile(output_file):
        if os.path.exists(output_file):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Tệp {output_file} đã tồn tại, bạn vẫn muốn tiếp tục chứ?")
            msg.setWindowTitle("Cảnh báo")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            result = msg.exec_()
            return not result == QMessageBox.Cancel

        return True

    def OnOpenFolderClick():

        input_file = config.InputFile

        input_file_info = QFileInfo(input_file)

        allow = ['jpg', 'png', 'webp']
        if not input_file_info.exists() or not input_file_info.suffix().lower() in allow:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Hãy chọn ảnh để lấy đầu ra.")
            msg.setWindowTitle("Cảnh báo")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

        folder_path = QDir(input_file_info.absolutePath())
        QDesktopServices.openUrl(QUrl.fromLocalFile(folder_path.absolutePath()))

    def OnUpscaleClick():

        input_file = config.InputFile
        scale = config.Scale
        current_model = config.CurrentModel

        file_info = QFileInfo(input_file)

        if not file_info.exists() or not file_info.suffix().lower() in ['jpg', 'png', 'webp']:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Vui lòng chọn đầu vào")
            msg.setWindowTitle("Lỗi")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

        config.GenerateOutputFile()
        output_file = config.OutputFile

        if not AllowExistFile(output_file):
            return

        print(f"Input File: {input_file}")
        print(f"Scale: {scale}")
        print(f"Output File: {output_file}")
        print(f"Model: {current_model}")

        args = ["-i", input_file, "-o", output_file, "-s", str(scale), "-n", current_model, "-m", MODELS]

        print(' '.join(args))

        processCallback = lambda status: ui.progressBaUpscaleStatus.setValue(status)

        Command.RunUpscaleCommand(args, processCallback)

        file_info = QFileInfo(output_file)

        print(file_info.size(), file_info.suffix(), file_info.path())

        if file_info.exists() and file_info.suffix().lower() in ['jpg', 'png', 'webp']:
            pixmap = QPixmap(output_file)

            label_width = ui.imageLabelBottom.width()
            label_height = ui.imageLabelBottom.height()

            scaled_pixmap = pixmap.scaled(label_width, label_height, aspectRatioMode=Qt.KeepAspectRatio)

            ui.imageLabelBottom.setPixmap(scaled_pixmap)
            ui.imageLabelBottom.setScaledContents(True)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Hoàn thành upscale")
        msg.setWindowTitle("Thông báo")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def OnCompareClick():

        input_file = config.InputFile
        output_file = config.OutputFile

        input_file_info = QFileInfo(input_file)
        output_file_info = QFileInfo(output_file)

        allow = ['jpg', 'png', 'webp']
        if (
                not input_file_info.exists() or not output_file_info.exists() or not input_file_info.suffix().lower() in allow or not output_file_info.suffix().lower() in allow):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Hãy chọn ảnh và upscale để so sánh.")
            msg.setWindowTitle("Cảnh báo")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

        args = [input_file, output_file, "-w", f"{COMPARE_WIDTH}x{COMPARE_HEIGHT}"]
        Command.RunCompareCommand(args)

    combobox.currentIndexChanged.connect(OnComboboxChanged)
    spinbox.valueChanged.connect(OnSpinChanged)
    ui.selectImageButton.clicked.connect(OnSelectImage)
    ui.upscaleButton.clicked.connect(OnUpscaleClick)
    ui.compareImageButton.clicked.connect(OnCompareClick)
    ui.outputFolderButton.clicked.connect(OnOpenFolderClick)


if __name__ == "__main__":
    command = Command()

    app, mainWindow, form = InitForm()

    form.setWindowTitle(f'Python D16CNPM6 - Vũ Thế Mạnh - Bùi Minh Đức {VERSION}')

    LoadData(mainWindow, command)

    ConnectEvents(mainWindow)

    form.show()

    sys.exit(app.exec_())
