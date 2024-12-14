import os


class Configuration:
    def __init__(self):
        self.Scale = 2
        self.CurrentModel = "realesr-animevideov3"
        self.InputFile = ""
        self.OutputFile = ""

    def GenerateOutputFile(self):

        print("--------------Generating output file...------------------")
        file_name, file_extension = os.path.splitext(self.InputFile)
        self.OutputFile = f"{file_name}_x{self.Scale}{file_extension}"
        print("Output file: " + self.OutputFile)
        print("-------------Generated output file...--------------------")

    def ShowLogInfo(self):
        print('---------------Information---------------')
        print(f"Input File: {self.InputFile}")
        print(f"Scale: {self.Scale}")
        print(f"Output File: {self.OutputFile}")
        print(f"Model: {self.CurrentModel}")
        print('-----------------------------------------')
