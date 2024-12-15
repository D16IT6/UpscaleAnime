import os
import re
import shutil
import subprocess
import time
from typing import List

import cv2
from watchdog.observers import Observer

from Models.UpscaleModel import UpscaleModel
from Utilities import Configuration
from Utilities.Constants import REALESRGAN, COMPARE, MODELS, FFMPEG, FFPROBE
from Utilities.NewFileWatchHandler import NewFileWatchHandler


class Command:
    def LoadModels(self) -> List[UpscaleModel]:
        model = [
            UpscaleModel(name="realesr-animevideov3", scale=[2, 3, 4]),
            UpscaleModel(name="realesrgan-x4plus", scale=[4]),
            UpscaleModel(name="realesrgan-x4plus-anime", scale=[4]),
        ]
        return model

    def RunUpscaleCommand(args: List[str], callback=None):
        full_command = [REALESRGAN] + args
        print('----------------------Cmd Command----------------------')
        print(' '.join(full_command))
        print('----------------------Cmd Command----------------------')

        process = subprocess.Popen(
            full_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
            text=True
        )

        for line in process.stderr:
            matches = re.findall(r"(\d+,\d+)", line)

            if matches:
                percent_str = matches[0].replace(",", ".")
                try:
                    percent = int(float(percent_str))

                    if callback:
                        callback(percent)

                except ValueError as e:
                    print(f"Error converting percentage: {e}")

        process.stdout.close()
        process.wait()

        if callback:
            callback(100)

    def RunCompareCommand(args: List[str]):
        full_command = [COMPARE] + args
        print('----------------------Cmd Command----------------------')
        print(' '.join(full_command))
        print('----------------------Cmd Command----------------------')

        process = subprocess.Popen(
            full_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
            text=True
        )
        process.wait()

    def UpscaleVideo(self, config: Configuration, log_callback=None):

        log_callback = log_callback or (lambda status: print(f"Log: {status}"))

        tmp_frames = self.ExtractFrame(config, log_callback)

        upscale_frames = "upscale_frames"
        if os.path.exists(upscale_frames):
            try:
                shutil.rmtree(upscale_frames)
                log_callback(f'Đã xóa thư mục cũ: {upscale_frames}')
            except Exception as e:
                log_callback(f'Không thể xóa thư mục {upscale_frames}. Lỗi: {e}')
                return

        os.makedirs(upscale_frames)

        args = ["-i", tmp_frames, "-o", upscale_frames, "-n", config.CurrentModel, "-m", MODELS, "-s",
                str(config.Scale), "-f", "jpg"]

        self.RunUpscaleFolderCommand(args=args,config=config, output_folder=upscale_frames, log_callback=log_callback)

        log_callback(f"Đã upscale xong các frames")

        log_callback(f"Chuẩn bị merge video")


        cap = cv2.VideoCapture(config.InputFile)

        fps = cap.get(cv2.CAP_PROP_FPS)

        log_callback(f"FPS: {fps}")
        args = ["-r", str(fps),
                "-i", f'{upscale_frames}/frame_%08d.jpg',
                "-i", config.InputFile,
                "-map", "0:v:0",
                "-map", "1:a?",
                "-map", "1:s?",
                "-c:v", "h264_nvenc",
                "-c:a", "copy",
                "-r", str(fps),

                "-pix_fmt", "yuv420p",
                config.OutputFile]
        self.MergeVideo(args, config, log_callback)

        log_callback(f"Đã merge video xong, hãy compare để trải nghiệm")

    def ExtractFrame(self, config: Configuration, log_callback=None):
        output_folder = "tmp_frames"
        if os.path.exists(output_folder):
            try:
                shutil.rmtree(output_folder)
                log_callback(f'Đã xóa thư mục cũ: {output_folder}')
            except Exception as e:
                log_callback(f'Không thể xóa thư mục {output_folder}. Lỗi: {e}')
                return

        os.makedirs(output_folder)

        log_callback(f'Đã tạo folder mới: {output_folder}')

        cap = cv2.VideoCapture(config.InputFile)

        if not cap.isOpened():
            log_callback(f'Lỗi: không mở được video {config.InputFile}')
            return

        frame_extract = 0
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        try:
            while True:
                success, frame = cap.read()

                if not success or frame is None:
                    break

                frame_filename = os.path.join(output_folder, f"frame_{frame_extract:08d}.jpg")
                cv2.imwrite(frame_filename, frame)

                frame_extract += 1
                log_callback(f'Đã tách frame {frame_extract} / {frame_count}')

                if frame_count < 1000:
                    time.sleep(0.1)

        except Exception as e:
            log_callback(f'Lỗi khi tách frame: {e}')

        print(f"Đã tách thành công {frame_count} frames tới '{output_folder}'")
        log_callback(f"Đã tách thành công {frame_count} frames tới '{output_folder}'")


        cap.release()

        return output_folder

    def RunUpscaleFolderCommand(self, args: List[str], config:Configuration,output_folder, log_callback):
        full_command = [REALESRGAN] + args
        print('----------------------Cmd Command----------------------')
        print(' '.join(full_command))
        print('----------------------Cmd Command----------------------')

        cap = cv2.VideoCapture(config.InputFile)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        event_handler = NewFileWatchHandler(log_callback,total_frames)
        event_handler = NewFileWatchHandler(log_callback,total_frames)
        observer = Observer()
        observer.schedule(event_handler, output_folder, recursive=False)
        observer.start()
        try:
            process = subprocess.Popen(
                full_command,
                creationflags=subprocess.CREATE_NO_WINDOW
            )

            process.wait()

        except Exception as e:
            print(f"Error running command: {e}")
        finally:
            observer.stop()
            observer.join()

    def MergeVideo(self, args: List[str], config, log_callback):
        cap = cv2.VideoCapture(config.InputFile)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        full_command = [FFMPEG] + args
        print('----------------------Cmd Command----------------------')
        print(' '.join(full_command))
        print('----------------------Cmd Command----------------------')

        process = subprocess.Popen(
            full_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
            text=True
        )

        try:
            for line in process.stderr:
                print(f"Output line: {line.strip()}")
                frame_match = re.search(r"frame=\s*(\d+)", line)

                if frame_match and total_frames:
                    current_frame = int(frame_match.group(1))

        except Exception as e:
            log_callback(f"Lỗi khi merge video: {e}")

        process.stdout.close()
        process.wait()

