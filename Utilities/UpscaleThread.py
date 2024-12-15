import os
import shutil
import cv2
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import QThread
from Utilities.Configuration import Configuration

class UpscaleThread(QThread):
    log_signal = pyqtSignal(str)
    progress_signal = pyqtSignal(int)
    done_signal = pyqtSignal()

    def __init__(self, config: Configuration, log_callback=None, progress_callback=None, done_callback=None):
        super(UpscaleThread,self).__init__()
        self.config = config

        # Nếu callback được truyền vào, gắn kết chúng với tín hiệu
        if log_callback:
            self.log_callback = log_callback
            self.log_signal.connect(self.log_callback)
        if progress_callback:
            self.progress_callback = progress_callback
            self.progress_signal.connect(self.progress_callback)

        if done_callback:
            self.done_callback = done_callback
            self.done_signal.connect(self.done_callback)


    def run(self):
        try:
            # self.extract_frame_from_video(self.config)
            print('UpscaleThread')
            self.progress_signal.emit(100)

        except Exception as e:
            print(e)

    def extract_frame_from_video(self, config: Configuration):
        try:
            output_folder = "tmp_frames"

            if os.path.exists(output_folder):
                shutil.rmtree(output_folder)
            os.makedirs(output_folder)

            cap = cv2.VideoCapture(config.InputFile)

            if not cap.isOpened():
                self.log_signal.emit(f'Lỗi: không mở được video {config.InputFile}')
                return

            frame_count = 0
            while True:
                success, frame = cap.read()
                if not success:
                    break

                frame_filename = os.path.join(output_folder, f"frame_{frame_count:06d}.jpg")
                cv2.imwrite(frame_filename, frame)

                frame_count += 1
                self.log_signal.emit(f'Đã tách frame {frame_count}')

                progress = int(frame_count / cap.get(cv2.CAP_PROP_FRAME_COUNT) * 100)
                self.progress_signal.emit(progress)

            cap.release()
            self.log_signal.emit(f"Đã tách thành công {frame_count} frames tới '{output_folder}'")
            self.progress_signal.emit(100)
            self.log_signal.emit("Đã hoàn thành tách frame")

            self.done_signal.emit()
        except Exception as e:
            print(e)
