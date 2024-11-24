import os


class Configuration:
    def __init__(self):
        self.Scale = 2
        self.CurrentModel = "realesr-animevideov3"
        self.InputFile = ""
        self.OutputFile = ""

    def GenerateOutputFile(self):
        file_name, file_extension = os.path.splitext(self.InputFile)
        self.OutputFile = f"{file_name}_x{self.Scale}{file_extension}"