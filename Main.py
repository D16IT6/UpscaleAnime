import os
import threading
from typing import Tuple

import sys

from PyQt6.QtCore import Qt, QDir, QUrl, QFileInfo, QTimer
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap, QDesktopServices

from Models.UpscaleModel import UpscaleModel
from Utilities.Command import Command
from Utilities.Configuration import Configuration
from Utilities.Constants import  MODELS, VERSION, COMPARE_HEIGHT, COMPARE_WIDTH
from Windows.MainWindow import Ui_MainWindow

config = Configuration()

allowed_image_extensions = ['jpg', 'png', 'webp']
allowed_video_extensions = ['mp4', 'mkv', 'webm']


def InitForm() -> Tuple[QApplication, Ui_MainWindow, QWidget]:
    app = QApplication(sys.argv)
    form = QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(form)
    return app, ui, form


def AllowExistFile(output_file):
    if os.path.exists(output_file):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(f"Tệp {output_file} đã tồn tại, bạn vẫn muốn tiếp tục chứ?")
        msg.setWindowTitle("Cảnh báo")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

        result = msg.exec()

        return result != QMessageBox.StandardButton.Cancel
    else:
        return True


def LoadData(mainWindow: Ui_MainWindow, command: Command):
    upscale_models = command.LoadModels()

    for upscaleModel in upscale_models:
        mainWindow.modelComboBox.addItem(upscaleModel.name, upscaleModel)
        mainWindow.modelComboBoxVideo.addItem(upscaleModel.name, upscaleModel)


def ConnectEventsImageTab(ui: Ui_MainWindow):
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
            "Image Files (*.png *.jpg *.jpeg *.webp)"
        )

        if file_path:
            file_info = QFileInfo(file_path)

            if IsValidImage(file_info, allowed_image_extensions):
                pixmap = QPixmap(file_path)

                label_width = ui.imageLabelTop.width()
                label_height = ui.imageLabelTop.height()

                scaled_pixmap = pixmap.scaled(label_width, label_height, Qt.AspectRatioMode.KeepAspectRatio)

                ui.imageLabelTop.setPixmap(scaled_pixmap)
                ui.imageLabelTop.setScaledContents(True)

                config.InputFile = file_path
            else:
                print("Hãy chọn hình ảnh hợp lệ!")

    def OnOpenFolderClick():

        input_file = config.InputFile

        input_file_info = QFileInfo(input_file)

        if not IsValidImage(input_file_info, allowed_image_extensions):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText(f"Hãy chọn ảnh để lấy đầu ra.")
            msg.setWindowTitle("Cảnh báo")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        folder_path = QDir(input_file_info.absolutePath())
        QDesktopServices.openUrl(QUrl.fromLocalFile(folder_path.absolutePath()))

    def OnUpscaleClick():

        input_file = config.InputFile
        scale = config.Scale
        current_model = config.CurrentModel

        output_file_info = QFileInfo(input_file)

        if not IsValidImage(output_file_info, allowed_image_extensions):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText(f"Vui lòng chọn đầu vào là ")
            msg.setWindowTitle("Lỗi")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        config.GenerateOutputFile()
        output_file = config.OutputFile

        if not AllowExistFile(output_file):
            return

        config.ShowLogInfo()

        args = ["-i", input_file, "-o", output_file, "-s", str(scale), "-n", current_model, "-m", MODELS]

        process_callback = lambda status: ui.progressBaUpscaleStatus.setValue(status)

        Command.RunUpscaleCommand(args, process_callback)

        output_file_info = QFileInfo(output_file)

        if IsValidImage(output_file_info, allowed_image_extensions):
            pixmap = QPixmap(output_file)

            label_width = ui.imageLabelBottom.width()
            label_height = ui.imageLabelBottom.height()

            scaled_pixmap = pixmap.scaled(label_width, label_height, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)

            ui.imageLabelBottom.setPixmap(scaled_pixmap)
            ui.imageLabelBottom.setScaledContents(True)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Hoàn thành upscale")
        msg.setWindowTitle("Thông báo")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def IsValidImage(file_info, allowed_extensions):
        return file_info.exists() and file_info.suffix().lower() in allowed_extensions

    def OnCompareClick():

        input_file = config.InputFile
        output_file = config.OutputFile

        input_file_info = QFileInfo(input_file)
        output_file_info = QFileInfo(output_file)

        if not IsValidImage(input_file_info, allowed_image_extensions) or not IsValidImage(output_file_info,
                                                                                           allowed_image_extensions):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Hãy chọn ảnh và upscale để so sánh.")
            msg.setWindowTitle("Cảnh báo")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        args = [input_file, output_file, "-w", f"{COMPARE_WIDTH}x{COMPARE_HEIGHT}"]
        Command.RunCompareCommand(args)

    combobox.currentIndexChanged.connect(OnComboboxChanged)
    spinbox.valueChanged.connect(OnSpinChanged)
    ui.selectImageButton.clicked.connect(OnSelectImage)
    ui.upscaleButton.clicked.connect(OnUpscaleClick)
    ui.compareImageButton.clicked.connect(OnCompareClick)
    ui.outputFolderButton.clicked.connect(OnOpenFolderClick)

def IsValidVideo(file_info):
    return file_info.exists() and file_info.suffix().lower() in allowed_video_extensions

def ConnectEventsVideoTab(ui: Ui_MainWindow):

    combobox = ui.modelComboBoxVideo
    spinbox = ui.numericUpDownVideo

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

    def OnSelectVideo():
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Chọn video anime cần upscale",
            "",
            "Video Files (*.mp4 *.mkv *.webm)"
        )

        if file_path:
            file_info = QFileInfo(file_path)

            if IsValidVideo(file_info):
                config.InputFile = file_path
            else:
                print("Hãy chọn video hợp lệ!")

    def OnUpscaleVideoClick():

        output_file_info = QFileInfo(config.InputFile)

        if not IsValidVideo(output_file_info):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText(f"Vui lòng chọn video để upscale.")
            msg.setWindowTitle("Lỗi")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        config.GenerateOutputFile()
        output_file = config.OutputFile

        if not AllowExistFile(output_file):
            return

        config.ShowLogInfo()

        log_callback = lambda log: (
            ui.listWidgetLog.clear() if ui.listWidgetLog.count() > 5 else None,
            ui.listWidgetLog.addItem(log)
        )

        t = threading.Thread(target=command.UpscaleVideo, args=(config, log_callback),
                         daemon=True)
        t.start()

    def OnCompareClick():

        input_file = config.InputFile
        output_file = config.OutputFile

        input_file_info = QFileInfo(input_file)
        output_file_info = QFileInfo(output_file)

        if not IsValidVideo(input_file_info) or not IsValidVideo(output_file_info):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Hãy chọn video và upscale để so sánh.")
            msg.setWindowTitle("Cảnh báo")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return

        args = [input_file, output_file, "-w", f"{COMPARE_WIDTH}x{COMPARE_HEIGHT}"]
        Command.RunCompareCommand(args)

    combobox.currentIndexChanged.connect(OnComboboxChanged)
    spinbox.valueChanged.connect(OnSpinChanged)

    mainWindow.selectVideoButton.clicked.connect(OnSelectVideo)
    mainWindow.upscaleButtonVideo.clicked.connect(OnUpscaleVideoClick)

    mainWindow.compareButtonVideo.clicked.connect(OnCompareClick)


if __name__ == "__main__":
    command = Command()

    app, mainWindow, form = InitForm()

    form.setWindowTitle(f'Python D16CNPM6 - Vũ Thế Mạnh - Bùi Minh Đức {VERSION}')

    LoadData(mainWindow, command)

    ConnectEventsImageTab(mainWindow)
    ConnectEventsVideoTab(mainWindow)

    form.show()

    sys.exit(app.exec())
