import re
import subprocess
from typing import List

from Models.UpscaleModel import UpscaleModel
from Utilities.Constants import REALESRGAN, COMPARE


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
        print(f"Full command: {' '.join(full_command)}")

        process = subprocess.Popen(
            full_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
            text=True
        )

        for line in process.stderr:
            # (f"Output line: {line.strip()}")
            matches = re.findall(r"(\d+,\d+)", line)

            if matches:
                # print(f"Matches found: {matches}")

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

    def RunCompareCommand(args:List[str]):
        full_command = [COMPARE] + args
        print(f"Full command: {' '.join(full_command)}")

        process = subprocess.Popen(
            full_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NO_WINDOW,
            text=True
        )
        process.wait()
