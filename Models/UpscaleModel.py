from dataclasses import dataclass

@dataclass
class UpscaleModel:
    name: str
    scale: list[int]
